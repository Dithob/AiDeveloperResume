#!/usr/bin/env python3
"""把 skills/ 下的技能挂载到 .codebuddy/skills/，供 CodeBuddy 加载。

Windows 使用 Junction（目录联接，无需管理员权限），macOS/Linux 使用符号链接。
挂载点是链接而非副本：修改 skills/ 下的源文件后立即生效，无需重新挂载。
.codebuddy/ 已被 .gitignore 忽略，克隆仓库或清理 IDE 缓存后重新运行本脚本即可。
"""

from __future__ import annotations

import argparse
import os
import stat
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Sequence, Set

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "skills"
DEFAULT_TARGET = ROOT / ".codebuddy" / "skills"


class LinkError(Exception):
    """可以被用户直接修正的挂载错误。"""


def print_usage() -> None:
    print(
        "用法:\n"
        "  python scripts/link_skills.py                 挂载 skills/ 下所有技能到 .codebuddy/skills/\n"
        "  python scripts/link_skills.py --dry-run        只显示将要执行的动作，不修改磁盘\n"
        "  python scripts/link_skills.py --force          覆盖指向其它位置的旧链接\n"
        "  python scripts/link_skills.py --prune          清理 .codebuddy/skills 中已失效的链接\n"
        "\n"
        "挂载点指向 skills/<技能名>；源目录本身不会被修改或删除。"
    )


# ---------- 链接识别与操作（Windows Junction 与 POSIX 符号链接统一处理） ----------


def _decode(raw: bytes) -> str:
    encodings = ("mbcs", "utf-8") if os.name == "nt" else ("utf-8",)
    for encoding in encodings:
        try:
            return raw.decode(encoding)
        except (LookupError, UnicodeDecodeError):
            continue
    return raw.decode("utf-8", errors="replace")


def _is_reparse_point(path: Path) -> bool:
    """Python 3.12 之前 os.path.islink() 认不出 Junction，需要看文件属性。"""
    flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    if not flag:
        return False
    try:
        attributes = os.lstat(str(path)).st_file_attributes
    except (OSError, AttributeError):
        return False
    return bool(attributes & flag)


def is_link(path: Path) -> bool:
    return os.path.islink(str(path)) or _is_reparse_point(path)


def link_target(path: Path) -> Optional[Path]:
    try:
        raw = os.readlink(str(path))
    except OSError:
        return None
    if raw.startswith("\\\\?\\"):
        raw = raw[4:]
    target = Path(raw)
    if not target.is_absolute():
        target = path.parent / target
    return target


def same_target(path: Path, expected: Path) -> bool:
    current = link_target(path)
    if current is None:
        return False
    normalize = lambda value: os.path.normcase(os.path.normpath(str(value)))  # noqa: E731
    return normalize(current) == normalize(expected)


def create_link(link: Path, target: Path) -> None:
    if os.name == "nt":
        result = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(link), str(target)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        if result.returncode != 0:
            detail = _decode(result.stdout or b"").strip()
            raise LinkError("创建 Junction 失败：{} {}".format(link, detail))
    else:
        os.symlink(str(target), str(link), target_is_directory=True)


def remove_link(link: Path) -> None:
    """只删除链接本身；绝不递归进入目标目录。"""
    try:
        os.rmdir(str(link))
    except OSError:
        os.unlink(str(link))


# ---------- 挂载逻辑 ----------


def collect_sources(source: Path) -> List[Path]:
    if not source.is_dir():
        raise LinkError("找不到技能源目录：{}".format(source))
    entries: List[Path] = []
    for entry in sorted(source.iterdir(), key=lambda path: path.name.lower()):
        if entry.is_dir():
            entries.append(entry)
        elif is_link(entry):
            print("[WARN] 源链接已失效，跳过：{}".format(entry.name))
    return entries


def mount(entries: List[Path], target_dir: Path, force: bool, dry_run: bool) -> int:
    print("源目录：{}".format(entries[0].parent))
    print("挂载点：{}".format(target_dir))
    print("")

    problems = 0
    for entry in entries:
        name = entry.name
        link = target_dir / name

        if is_link(link):
            if same_target(link, entry):
                if link.exists():
                    print("[OK]   {} 已经挂载".format(name))
                    continue
                state = "repair"
            else:
                state = "repair" if not link.exists() else "conflict"
        elif link.exists():
            print(
                "[WARN] {} 已存在且不是链接（真实目录），为免误删已跳过；"
                "确认无用后请手动处理。".format(name)
            )
            problems += 1
            continue
        else:
            state = "new"

        if state == "conflict":
            if not force:
                print(
                    "[WARN] {} 已指向其它位置（{}），未覆盖；确认后加 --force 重新挂载。".format(
                        name, link_target(link)
                    )
                )
                problems += 1
                continue
            state = "repair"

        if dry_run:
            label = "会重新挂载" if state == "repair" else "会新建挂载"
            print("[DRY]  {} {}".format(name, label))
            continue

        if state == "repair":
            remove_link(link)
        target_dir.mkdir(parents=True, exist_ok=True)
        create_link(link, entry)
        print("[{}] {} -> {}".format("FIX" if state == "repair" else "NEW", name, entry))

        if not (entry / "SKILL.md").is_file():
            print("       [WARN] 缺少 SKILL.md，可能不会被识别为技能。")

    return problems


def prune(target_dir: Path, keep: Set[str], dry_run: bool) -> int:
    if not target_dir.is_dir():
        print("[OK]   挂载点不存在，无需清理。")
        return 0

    removed = 0
    for entry in sorted(target_dir.iterdir(), key=lambda path: path.name.lower()):
        if entry.name in keep or not is_link(entry):
            continue
        if entry.exists():
            continue
        if dry_run:
            print("[DRY]  会删除失效链接：{} -> {}".format(entry.name, link_target(entry)))
            removed += 1
            continue
        target = link_target(entry)
        remove_link(entry)
        print("[PRUNE] {} -> {}（目标已不存在）".format(entry.name, target))
        removed += 1

    if removed == 0:
        print("[OK]   没有失效链接需要清理。")
    return removed


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--prune", action="store_true")
    parser.add_argument("-h", "--help", action="store_true")
    args = parser.parse_args(argv)

    if args.help:
        print_usage()
        return 0

    try:
        entries = collect_sources(DEFAULT_SOURCE)
        if not entries:
            raise LinkError("{} 下没有可挂载的技能目录。".format(DEFAULT_SOURCE))
        if not args.dry_run:
            DEFAULT_TARGET.mkdir(parents=True, exist_ok=True)
        problems = mount(entries, DEFAULT_TARGET, args.force, args.dry_run)
        if args.prune:
            print("")
            prune(DEFAULT_TARGET, {entry.name for entry in entries}, args.dry_run)
        print("")
        if args.dry_run:
            print("[DRY-RUN] 未修改磁盘；去掉 --dry-run 才会实际挂载。")
        print("[DONE] 源文件未被改动；挂载后重启/刷新会话即可在 /skills 面板看到。")
        return 1 if problems else 0
    except LinkError as error:
        print("[ERROR] {}".format(error), file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\n已取消。", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
