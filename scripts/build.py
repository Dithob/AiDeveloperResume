#!/usr/bin/env python3
"""Cross-platform XeLaTeX build driver for AiDeveloperResume."""

from __future__ import annotations

import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TARGETS = (
    "main_algorithm.tex",
    "main_backend.tex",
    "main_frontend.tex",
    "main_testdevelop.tex",
)
MODES = ("preview", "release")


class BuildError(Exception):
    """A user-correctable build setup or argument error."""


def print_usage() -> None:
    print(
        "用法:\n"
        "  python scripts/build.py [TARGET]              发布编译（兼容旧命令）\n"
        "  python scripts/build.py preview [TARGET]      单遍快速预览\n"
        "  python scripts/build.py release [TARGET]      双遍发布编译\n"
        "  python scripts/build.py [preview|release] --all\n"
        "\n"
        f"TARGET 可选：{', '.join(ALLOWED_TARGETS)}\n"
        "默认无参数时进入交互式选择；非交互环境默认选择 main_algorithm.tex。"
    )


def parse_invocation(argv: Sequence[str]) -> Tuple[str, bool, Optional[str]]:
    if any(arg in ("-h", "--help") for arg in argv):
        print_usage()
        raise SystemExit(0)

    mode = "release"
    mode_seen = False
    all_targets = False
    positional: List[str] = []

    for arg in argv:
        if arg in MODES:
            if mode_seen and mode != arg:
                raise BuildError("preview 和 release 不能同时指定。")
            mode = arg
            mode_seen = True
        elif arg == "--preview":
            if mode_seen and mode != "preview":
                raise BuildError("preview 和 release 不能同时指定。")
            mode = "preview"
            mode_seen = True
        elif arg == "--release":
            if mode_seen and mode != "release":
                raise BuildError("preview 和 release 不能同时指定。")
            mode = "release"
            mode_seen = True
        elif arg == "--all":
            all_targets = True
        elif arg.startswith("-"):
            raise BuildError(f"不支持的参数：{arg}")
        else:
            positional.append(arg)

    if len(positional) > 1:
        raise BuildError("一次只能指定一个模板文件。")
    if all_targets and positional:
        raise BuildError("--all 不能与具体模板文件同时使用。")

    return mode, all_targets, positional[0] if positional else None


def choose_target() -> str:
    if not sys.stdin.isatty():
        return ALLOWED_TARGETS[0]

    print("\n选择要编译的简历模板：")
    for index, target in enumerate(ALLOWED_TARGETS, start=1):
        print(f"  {index}) {target}")
    choice = input("输入 1-4（默认 1）：").strip() or "1"
    try:
        selected = ALLOWED_TARGETS[int(choice) - 1]
    except (ValueError, IndexError):
        raise BuildError("选择无效，请输入 1-4。")
    return selected


def validate_target(value: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute() or candidate.name != value or value not in ALLOWED_TARGETS:
        raise BuildError(
            f"模板不在允许列表中：{value}\n允许值：{', '.join(ALLOWED_TARGETS)}"
        )
    target = ROOT / value
    if not target.is_file():
        raise BuildError(f"找不到模板文件：{target}")
    return target


def check_prerequisites() -> str:
    xelatex = shutil.which("xelatex")
    if not xelatex:
        raise BuildError(
            "找不到 xelatex。macOS 请安装 MacTeX/BasicTeX，Windows 请安装 MiKTeX 或 TeX Live，"
            "然后重新打开终端。"
        )

    required = (
        ROOT / "tex" / "data" / "profile.tex",
        ROOT / "tex" / "data" / "education.tex",
        ROOT / "fonts" / "NotoSerifSC.otf",
        ROOT / "fonts" / "NotoSerifSC-Bold.otf",
        ROOT / "images" / "foot.png",
    )
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        missing_text = "\n".join(f"  - {item}" for item in missing)
        raise BuildError(
            "缺少本地编译所需文件：\n"
            f"{missing_text}\n"
            "首次使用请先复制 tex/data/*.tex.example，并按需填写本地个人信息。"
        )
    return xelatex


def command_for(xelatex: str, target: Path, output_dir: Path) -> List[str]:
    return [
        xelatex,
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        "-no-shell-escape",
        "-synctex=1",
        f"-output-directory={output_dir}",
        target.name,
    ]


def compile_one(xelatex: str, target: Path, mode: str) -> None:
    output_root = ROOT / (".preview" if mode == "preview" else ".output")
    output_dir = output_root / target.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    passes = 1 if mode == "preview" else 2
    print(f"\n=== {mode}：{target.name}（{passes} pass）===")
    started = time.perf_counter()

    for pass_number in range(1, passes + 1):
        print(f"--- XeLaTeX pass {pass_number}/{passes} ---")
        result = subprocess.run(
            command_for(xelatex, target, output_dir),
            cwd=str(ROOT),
            check=False,
        )
        if result.returncode != 0:
            log_path = output_dir / f"{target.stem}.log"
            print(f"[ERROR] 编译失败，退出码 {result.returncode}。")
            if log_path.is_file():
                print(f"日志：{log_path}")
            raise SystemExit(result.returncode or 1)

    pdf_path = output_dir / f"{target.stem}.pdf"
    synctex_path = output_dir / f"{target.stem}.synctex.gz"
    if not pdf_path.is_file():
        raise BuildError(f"XeLaTeX 返回成功，但没有生成 PDF：{pdf_path}")
    if not synctex_path.is_file():
        print("[WARN] 未找到 .synctex.gz，PDF 与源码的双向定位可能不可用。")

    elapsed = time.perf_counter() - started
    print(f"完成：{pdf_path}")
    print(f"耗时：{elapsed:.2f}s")


def main(argv: Sequence[str]) -> int:
    try:
        mode, all_targets, target_arg = parse_invocation(argv)
        xelatex = check_prerequisites()

        if all_targets:
            targets: Iterable[Path] = [validate_target(name) for name in ALLOWED_TARGETS]
        else:
            targets = [validate_target(target_arg or choose_target())]

        for target in targets:
            compile_one(xelatex, target, mode)
        return 0
    except BuildError as error:
        print(f"[ERROR] {error}", file=sys.stderr)
        print_usage()
        return 2
    except KeyboardInterrupt:
        print("\n已取消。", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
