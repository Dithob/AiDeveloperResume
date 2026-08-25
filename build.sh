#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if command -v python3 >/dev/null 2>&1; then
    exec python3 "$ROOT/scripts/build.py" "$@"
fi

if command -v python >/dev/null 2>&1; then
    exec python "$ROOT/scripts/build.py" "$@"
fi

printf '%s\n' '[ERROR] 找不到 Python 3，请先安装 Python 3。' >&2
exit 1
