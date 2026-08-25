#!/usr/bin/env python3
"""Prepare and explicitly publish a local resume to an Overleaf Git mirror."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Set, Tuple


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MIRROR = ROOT / ".overleaf-sync" / "repo"
ALLOWED_TARGETS = (
    "main_algorithm.tex",
    "main_backend.tex",
    "main_frontend.tex",
    "main_testdevelop.tex",
)
IMAGE_REF = re.compile(r"(?:\\(?:includegraphics|graphicspath)\s*\{)?(images/[A-Za-z0-9_.-]+)")
COMMAND_IMAGE_REF = re.compile(
    r"\\newcommand\{\\(?:ResumePhoto|ResumeHeaderImage)\}\{([^}]+)\}"
)
PRIVATE_TEX_PATHS = {
    Path("tex/data/profile.tex"),
    Path("tex/data/education.tex"),
}
PRIVATE_IMAGE_PATHS = {
    Path("images/me.jpg"),
    Path("images/photo_mine.jpg"),
}
PUBLIC_IMAGE_PATHS = {
    Path("images/foot.png"),
    Path("images/kun.png"),
}


class PublishError(Exception):
    pass


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="将本地简历准备到隔离 Overleaf Git 镜像；默认不 push。"
    )
    parser.add_argument("--init", metavar="OVERLEAF_GIT_URL", help="首次初始化隔离镜像")
    parser.add_argument(
        "--mirror-dir",
        default=str(DEFAULT_MIRROR.relative_to(ROOT)),
        help="隔离镜像目录，默认 .overleaf-sync/repo",
    )
    parser.add_argument(
        "--include-private",
        action="store_true",
        help="明确包含 profile.tex、education.tex 和实际引用的个人图片",
    )
    parser.add_argument("--push", action="store_true", help="提交并推送到 Overleaf；默认不推送")
    parser.add_argument("--zip", metavar="PATH", help="生成可手动上传到 Overleaf 的 ZIP")
    parser.add_argument("--message", default="sync local resume", help="Overleaf 提交消息")
    parser.add_argument("--branch", help="目标分支；默认使用镜像当前分支")
    return parser.parse_args(argv)


def run_git(
    args: Sequence[str], cwd: Path, capture: bool = False
) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ["git", *args],
            cwd=str(cwd),
            text=True,
            capture_output=capture,
            check=False,
        )
    except FileNotFoundError as error:
        raise PublishError("找不到 git，请先安装 Git。") from error


def require_git_success(result: subprocess.CompletedProcess[str], action: str) -> None:
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        raise PublishError(f"{action}失败。{detail}")


def resolve_mirror(value: str) -> Path:
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = ROOT / candidate
    mirror = candidate.resolve()
    try:
        mirror.relative_to(ROOT)
    except ValueError as error:
        raise PublishError("隔离镜像必须位于仓库目录内，避免脚本写入未知位置。") from error
    return mirror


def init_mirror(mirror: Path, url: str) -> None:
    if mirror.exists() and any(mirror.iterdir()):
        raise PublishError(f"镜像目录已存在且非空：{mirror}；请换目录或先人工检查。")
    mirror.parent.mkdir(parents=True, exist_ok=True)
    result = run_git(["clone", url, str(mirror)], ROOT)
    require_git_success(result, "克隆 Overleaf 项目")
    origin = run_git(["remote", "get-url", "origin"], mirror, capture=True)
    if origin.returncode == 0:
        rename = run_git(["remote", "rename", "origin", "overleaf"], mirror, capture=True)
        require_git_success(rename, "将远程别名改为 overleaf")


def ensure_mirror(mirror: Path) -> None:
    if not (mirror / ".git").exists():
        raise PublishError(
            f"找不到 Overleaf Git 镜像：{mirror}\n首次使用请加 --init <Overleaf Git URL>。"
        )
    remote = run_git(["remote", "get-url", "overleaf"], mirror, capture=True)
    if remote.returncode != 0:
        origin = run_git(["remote", "get-url", "origin"], mirror, capture=True)
        if origin.returncode == 0:
            rename = run_git(["remote", "rename", "origin", "overleaf"], mirror, capture=True)
            require_git_success(rename, "将远程别名改为 overleaf")
        else:
            raise PublishError("镜像没有 overleaf 远程仓库，请先在镜像中配置正确的 Overleaf Git URL。")


def read_tex_sources(include_private: bool = False) -> Iterable[Path]:
    for name in ALLOWED_TARGETS:
        path = ROOT / name
        if path.is_file():
            yield path
    for directory in (ROOT / "tex" / "shared", ROOT / "tex" / "data"):
        if directory.is_dir():
            for path in sorted(directory.rglob("*.tex")):
                relative = path.relative_to(ROOT)
                if include_private or relative not in PRIVATE_TEX_PATHS:
                    yield path


def collect_image_refs(include_private: bool = False) -> Set[str]:
    refs: Set[str] = set()
    for path in read_tex_sources(include_private):
        text = path.read_text(encoding="utf-8")
        for match in IMAGE_REF.finditer(text):
            refs.add(match.group(1))
        for match in COMMAND_IMAGE_REF.finditer(text):
            value = match.group(1).strip()
            if value.startswith("images/"):
                refs.add(value)
    return refs


def collect_managed_paths(include_private: bool) -> Tuple[List[Path], List[Path]]:
    public: Set[Path] = {Path(name) for name in ALLOWED_TARGETS}
    public_images = PUBLIC_IMAGE_PATHS | {
        Path(image) for image in collect_image_refs(False)
    }
    public_images -= PRIVATE_IMAGE_PATHS
    public.update(public_images)

    for directory in (ROOT / "tex" / "shared", ROOT / "tex" / "data"):
        if directory.is_dir():
            for path in directory.rglob("*"):
                relative = path.relative_to(ROOT)
                if (
                    path.is_file()
                    and path.suffix in (".tex", ".sty", ".cls")
                    and (include_private or relative not in PRIVATE_TEX_PATHS)
                ):
                    public.add(relative)

    fonts = ROOT / "fonts"
    if fonts.is_dir():
        for path in fonts.rglob("*"):
            if path.is_file() and path.suffix.lower() in (".otf", ".ttf", ".ttc"):
                public.add(path.relative_to(ROOT))

    private: Set[Path] = set(PRIVATE_TEX_PATHS) | PRIVATE_IMAGE_PATHS
    if include_private:
        private.update(
            Path(image)
            for image in collect_image_refs(True)
            if Path(image) not in public_images
        )

    existing_private = {path for path in private if (ROOT / path).is_file()}
    all_paths = sorted(public | (existing_private if include_private else set()))
    return all_paths, sorted(existing_private)


def copy_sources(mirror: Path, paths: Iterable[Path]) -> List[Path]:
    missing: List[Path] = []
    copied: List[Path] = []
    for relative in paths:
        source = ROOT / relative
        destination = mirror / relative
        if not source.is_file():
            missing.append(relative)
            continue
        if source.is_symlink():
            raise PublishError(f"不复制符号链接，请改用普通文件：{relative}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied.append(relative)
    if missing:
        details = "\n".join(f"  - {item}" for item in missing)
        raise PublishError(f"编译依赖文件不存在：\n{details}")
    return copied


def git_status_paths(mirror: Path) -> Set[str]:
    result = run_git(
        ["status", "--porcelain=v1", "--untracked-files=all"], mirror, capture=True
    )
    require_git_success(result, "读取镜像状态")
    paths: Set[str] = set()
    for line in result.stdout.splitlines():
        if len(line) >= 4:
            value = line[3:]
            if " -> " in value:
                value = value.split(" -> ", 1)[1]
            paths.add(value)
    return paths


def show_status(mirror: Path) -> None:
    result = run_git(
        ["status", "--short", "--untracked-files=all"], mirror, capture=True
    )
    require_git_success(result, "读取镜像状态")
    print(result.stdout.rstrip() or "[OK] 镜像工作区没有待提交变更。")


def current_branch(mirror: Path, requested: Optional[str]) -> str:
    branch = requested
    if branch is None:
        result = run_git(["branch", "--show-current"], mirror, capture=True)
        require_git_success(result, "读取镜像分支")
        branch = result.stdout.strip()
    if branch not in ("main", "master"):
        raise PublishError("Overleaf Git 不支持分支协作；目标分支只允许 main 或 master。")
    return branch


def check_remote_ahead(mirror: Path, branch: str) -> None:
    fetch = run_git(["fetch", "overleaf", branch], mirror, capture=True)
    if fetch.returncode != 0:
        detail = (fetch.stderr or fetch.stdout or "").strip()
        raise PublishError(f"拉取 Overleaf 远程状态失败，未执行 push。{detail}")

    remote_ref = f"refs/remotes/overleaf/{branch}"
    exists = run_git(["rev-parse", "--verify", remote_ref], mirror, capture=True)
    if exists.returncode != 0:
        return

    counts = run_git(
        ["rev-list", "--left-right", "--count", f"HEAD...overleaf/{branch}"],
        mirror,
        capture=True,
    )
    require_git_success(counts, "检查 Overleaf 分歧")
    values = counts.stdout.split()
    if len(values) != 2:
        raise PublishError("无法判断 Overleaf 远程分支是否有未同步修改。")
    ahead, behind = (int(values[0]), int(values[1]))
    if behind:
        raise PublishError(
            f"Overleaf 远程分支领先本地 {behind} 个提交；请先人工检查并执行：\n"
            f"git -C {mirror} pull --rebase overleaf {branch}\n"
            "确认无冲突后再重新准备发布。"
        )
    if not ahead:
        print("[INFO] 本地与 Overleaf 当前提交一致，将只检查工作区变更。")


def ensure_private_for_publish(include_private: bool, private_paths: Sequence[Path], action: str) -> None:
    if action in ("push", "zip") and not include_private:
        raise PublishError(
            f"{action} 前必须显式传入 --include-private；个人信息文件不会从 GitHub 主仓库自动带入。"
        )
    required = {Path("tex/data/profile.tex"), Path("tex/data/education.tex")}
    missing = sorted(required - set(private_paths))
    if action in ("push", "zip") and missing:
        details = "\n".join(f"  - {item}" for item in missing)
        raise PublishError(f"缺少 Overleaf 编译所需的私有文件：\n{details}")


def stage_and_push(mirror: Path, managed: Sequence[Path], branch: str, message: str) -> None:
    check_remote_ahead(mirror, branch)
    managed_strings = [path.as_posix() for path in managed]
    status_paths = git_status_paths(mirror)
    unknown = sorted(status_paths - set(managed_strings))
    if unknown:
        details = "\n".join(f"  - {item}" for item in unknown)
        raise PublishError(
            "隔离镜像存在不属于本次发布白名单的变更，已停止以免误推送：\n" + details
        )

    if managed_strings:
        add = run_git(["add", "--", *managed_strings], mirror, capture=True)
        require_git_success(add, "暂存发布文件")
    staged = run_git(["diff", "--cached", "--quiet", "--", *managed_strings], mirror)
    if staged.returncode == 0:
        print("[OK] 没有需要推送到 Overleaf 的变更。")
        return
    if staged.returncode != 1:
        raise PublishError("无法检查已暂存的发布变更。")

    commit = run_git(["commit", "-m", message], mirror, capture=True)
    require_git_success(commit, "提交 Overleaf 发布镜像")
    push = run_git(["push", "overleaf", f"HEAD:{branch}"], mirror, capture=True)
    require_git_success(push, "推送到 Overleaf")
    print(f"[OK] 已推送到 Overleaf：{branch}")


def make_zip(mirror: Path, paths: Sequence[Path], output: str) -> Path:
    destination = Path(output)
    if not destination.is_absolute():
        destination = ROOT / destination
    destination = destination.resolve()
    try:
        destination.relative_to(ROOT)
    except ValueError as error:
        raise PublishError("ZIP 输出路径必须位于仓库目录内。") from error
    destination.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in paths:
            source = mirror / relative
            if source.is_file():
                archive.write(source, relative.as_posix())
    return destination


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    try:
        action = "push" if args.push else "zip" if args.zip else "prepare"
        mirror: Optional[Path] = None
        if action != "zip" or args.push or args.init:
            mirror = resolve_mirror(args.mirror_dir)
            if args.init:
                init_mirror(mirror, args.init)
            ensure_mirror(mirror)

        managed, private_paths = collect_managed_paths(args.include_private)
        ensure_private_for_publish(args.include_private, private_paths, action)
        if args.include_private:
            print("[WARN] 本次发布包含本地个人信息文件；这些文件只写入被忽略的隔离镜像或临时 ZIP 目录。")

        if action == "zip" and not args.push:
            with tempfile.TemporaryDirectory(prefix="resume-overleaf-zip-") as directory:
                staging = Path(directory)
                copied = copy_sources(staging, managed)
                output = make_zip(staging, managed, args.zip or "overleaf-resume.zip")
            print(f"[OK] 已准备 {len(copied)} 个文件到临时 ZIP 目录。")
            print(f"[OK] 已生成 ZIP：{output.relative_to(ROOT)}")
            return 0

        if mirror is None:
            raise PublishError("缺少 Overleaf 隔离镜像，请先使用 --init 初始化。")
        copied = copy_sources(mirror, managed)
        print(f"[OK] 已准备 {len(copied)} 个文件到隔离镜像：{mirror.relative_to(ROOT)}")
        show_status(mirror)

        if args.zip:
            output = make_zip(mirror, managed, args.zip)
            print(f"[OK] 已生成 ZIP：{output.relative_to(ROOT)}")

        if args.push:
            branch = current_branch(mirror, args.branch)
            stage_and_push(mirror, managed, branch, args.message)
        else:
            print("[DRY-RUN] 未执行 git commit 或 git push；确认差异后再加 --push。")
        return 0
    except (PublishError, OSError) as error:
        print(f"[ERROR] {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
