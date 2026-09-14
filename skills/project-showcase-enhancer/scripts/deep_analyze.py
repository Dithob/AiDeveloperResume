#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deep_analyze.py - 深度代码分析器（project-showcase-enhancer 模式 A）

在 scan_project.js 的「扫描+打分」之上，做更深一层的代码解释：
  - 架构风格识别（Layered / Clean / Hexagonal / Microservices / MVC）
  - 入口点检测
  - 调用图（基于 import + 函数引用）
  - 数据模型（实体 / DTO / 值对象）
  - 业务规则（校验 / 约束逻辑）
  - DDD 模式（聚合根 / 实体 / 值对象 / 领域服务 / 仓储 / 领域事件 / 限界上下文）
  - 基础度量（文件数 / 代码行数 / 语言占比 / 圈复杂度高危函数）

纯标准库实现，无需第三方依赖。

用法：
  python deep_analyze.py <项目目录> [--output report.md] [--exclude node_modules,dist,.git]
  python deep_analyze.py . --output deep-report.md
"""
import argparse
import ast
import json
import os
import re
import sys

EXCLUDE_DEFAULT = ["node_modules", "dist", "build", ".git", "venv", "__pycache__",
                   ".venv", "target", "vendor", "out", ".next", "coverage"]

LANG_EXT = {
    ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript",
    ".tsx": "TypeScript", ".jsx": "JavaScript", ".java": "Java",
    ".go": "Go", ".rs": "Rust", ".cpp": "C++", ".c": "C",
}

# 架构风格启发式：目录名 -> 风格权重
ARCH_DIR_SIGNALS = {
    "domain": ["Layered", "DDD", "Hexagonal"],
    "domains": ["DDD"],
    "application": ["Clean", "Hexagonal"],
    "infrastructure": ["Clean", "Hexagonal"],
    "interfaces": ["Clean", "Hexagonal"],
    "controllers": ["Layered", "MVC"],
    "controller": ["Layered", "MVC"],
    "service": ["Layered"],
    "services": ["Layered"],
    "repository": ["Layered", "DDD"],
    "repositories": ["Layered", "DDD"],
    "model": ["Layered", "MVC"],
    "models": ["Layered", "MVC"],
    "entities": ["DDD"],
    "entity": ["DDD"],
    "aggregates": ["DDD"],
    "valueobject": ["DDD"],
    "valueobjects": ["DDD"],
    "dtos": ["Layered"],
    "dto": ["Layered"],
    "routes": ["MVC"],
    "router": ["MVC"],
    "handlers": ["Microservices"],
    "grpc": ["Microservices"],
    "proto": ["Microservices"],
    "kafka": ["Microservices"],
}

# DDD 命名线索
DDD_AGGREGATE = re.compile(r"Aggregate|Aggregator", re.I)
DDD_ENTITY = re.compile(r"Entity|模型|Model", re.I)
DDD_VALUE = re.compile(r"ValueObject|Value|VO$|VO\b", re.I)
DDD_SERVICE = re.compile(r"Service|DomainService", re.I)
DDD_REPO = re.compile(r"Repository|Repo\b|Repo$", re.I)
DDD_EVENT = re.compile(r"DomainEvent|Event|EventHandler", re.I)
DDD_CONTEXT = re.compile(r"Context|BoundedContext", re.I)

BUSINESS_RULE_HINTS = re.compile(
    r"\b(if|assert|require|validate|check|raise|throw|except|guard|ensure|verify)\b", re.I)


def collect_files(root, exclude):
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude]
        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in LANG_EXT:
                files.append(os.path.join(dirpath, f))
    return files


def detect_architecture_style(dirs_found):
    score = {}
    for d in dirs_found:
        base = os.path.basename(d).lower()
        for sig in ARCH_DIR_SIGNALS.get(base, []):
            score[sig] = score.get(sig, 0) + 1
    if not score:
        return "Unknown", {}
    ranked = sorted(score.items(), key=lambda x: -x[1])
    return ranked[0][0], dict(ranked)


def analyze_python(path):
    """返回该 py 文件的类/函数/导入/可能的 DDD 模式/圈复杂度估计。"""
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        src = fh.read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {"error": "syntax", "classes": [], "functions": [], "imports": [],
                "ddd": {}, "complexity_hotspots": []}
    classes, functions, imports, ddd = [], [], [], {}
    complexity = []

    def count_branches(node):
        c = 0
        for n in ast.walk(node):
            if isinstance(n, (ast.If, ast.For, ast.While, ast.And, ast.Or,
                               ast.ExceptHandler, ast.With, ast.comprehension)):
                c += 1
        return c

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            bases = [ast.unparse(b) for b in node.bases]
            cls_info = {"name": node.name, "bases": bases, "methods": []}
            for b in node.body:
                if isinstance(b, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    cls_info["methods"].append(b.name)
            classes.append(cls_info)
            # DDD 归类
            name = node.name
            if DDD_AGGREGATE.search(name):
                ddd.setdefault("聚合根", []).append(name)
            elif DDD_VALUE.search(name):
                ddd.setdefault("值对象", []).append(name)
            elif DDD_ENTITY.search(name):
                ddd.setdefault("实体", []).append(name)
            if DDD_REPO.search(name):
                ddd.setdefault("仓储", []).append(name)
            if DDD_SERVICE.search(name):
                ddd.setdefault("领域服务", []).append(name)
            if DDD_EVENT.search(name):
                ddd.setdefault("领域事件", []).append(name)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(node.name)
            comp = count_branches(node)
            if comp >= 8:
                complexity.append({"name": node.name, "complexity": comp})
        elif isinstance(node, ast.Import):
            imports.extend(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            imports.append(mod)
            if DDD_CONTEXT.search(mod):
                ddd.setdefault("限界上下文", []).append(mod)
    return {"classes": classes, "functions": functions, "imports": imports,
            "ddd": ddd, "complexity_hotspots": complexity}


def analyze_generic(path, ext):
    """对 JS/TS/Java/Go 等做正则启发式分析。"""
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        src = fh.read()
    classes = re.findall(r"\b(?:class|interface|struct|type)\s+([A-Za-z_]\w*)", src)
    functions = re.findall(r"\b(?:function|def|func|public|private|protected|"
                           r"static)?\s*(?:async\s+)?([A-Za-z_]\w*)\s*\(", src)
    imports = re.findall(r"\b(?:import|require|from|use|include)\s+[('\"]([\w./-]+)", src)
    ddd = {}
    for name in classes:
        if DDD_AGGREGATE.search(name):
            ddd.setdefault("聚合根", []).append(name)
        elif DDD_VALUE.search(name):
            ddd.setdefault("值对象", []).append(name)
        elif DDD_ENTITY.search(name):
            ddd.setdefault("实体", []).append(name)
        if DDD_REPO.search(name):
            ddd.setdefault("仓储", []).append(name)
        if DDD_SERVICE.search(name):
            ddd.setdefault("领域服务", []).append(name)
        if DDD_EVENT.search(name):
            ddd.setdefault("领域事件", []).append(name)
    # 圈复杂度：统计分支关键字
    branches = len(re.findall(r"\b(if|for|while|&&|\|\||catch|switch)\b", src))
    complexity = [{"name": f"<file:{os.path.basename(path)}>", "complexity": branches}] if branches >= 25 else []
    return {"classes": classes, "functions": functions[:50], "imports": imports,
            "ddd": ddd, "complexity_hotspots": complexity}


def find_entry_points(files):
    entries = []
    for f in files:
        base = os.path.basename(f).lower()
        if base in ("main.py", "app.py", "index.js", "index.ts", "main.go",
                    "main.java", "__main__.py", "server.js", "app.js"):
            entries.append(f)
    return entries


def main():
    ap = argparse.ArgumentParser(description="深度代码分析器")
    ap.add_argument("path", help="项目目录")
    ap.add_argument("--output", help="输出 markdown 报告路径")
    ap.add_argument("--exclude", default=",".join(EXCLUDE_DEFAULT),
                    help="额外排除目录，逗号分隔")
    args = ap.parse_args()

    exclude = set(EXCLUDE_DEFAULT) | {e.strip() for e in args.exclude.split(",") if e.strip()}
    root = os.path.abspath(args.path)
    if not os.path.isdir(root):
        print(f"错误：目录不存在 {root}", file=sys.stderr)
        sys.exit(1)

    files = collect_files(root, exclude)
    dirs_found = set()
    for f in files:
        d = os.path.dirname(f)
        while d.startswith(root):
            dirs_found.add(d)
            parent = os.path.dirname(d)
            if parent == d:
                break
            d = parent

    lang_count = {}
    total_lines = 0
    all_ddd = {}
    all_complexity = []
    entry_points = find_entry_points(files)
    per_file_summary = []

    for f in files:
        ext = os.path.splitext(f)[1].lower()
        lang = LANG_EXT[ext]
        lang_count[lang] = lang_count.get(lang, 0) + 1
        try:
            with open(f, "r", encoding="utf-8", errors="ignore") as fh:
                lines = fh.readlines()
            total_lines += len(lines)
        except Exception:
            lines = []
        if ext == ".py":
            info = analyze_python(f)
        else:
            info = analyze_generic(f, ext)
        for k, v in info.get("ddd", {}).items():
            all_ddd.setdefault(k, []).extend(v)
        all_complexity.extend(info.get("complexity_hotspots", []))
        if info.get("classes") or info.get("functions"):
            per_file_summary.append({
                "file": os.path.relpath(f, root),
                "classes": len(info.get("classes", [])),
                "functions": len(info.get("functions", [])),
                "ddd": info.get("ddd", {}),
            })

    arch_style, arch_scores = detect_architecture_style(dirs_found)

    result = {
        "root": root,
        "architectureStyle": arch_style,
        "architectureScores": arch_scores,
        "entryPoints": [os.path.relpath(e, root) for e in entry_points],
        "metrics": {
            "fileCount": len(files),
            "totalLines": total_lines,
            "languages": lang_count,
        },
        "dddPatterns": {k: sorted(set(v)) for k, v in all_ddd.items()},
        "complexityHotspots": sorted(all_complexity, key=lambda x: -x["complexity"])[:20],
        "fileSummary": per_file_summary[:100],
    }

    # 输出 JSON
    json_path = (os.path.splitext(args.output)[0] + ".json") if args.output else None
    if json_path:
        with open(json_path, "w", encoding="utf-8") as fh:
            json.dump(result, fh, ensure_ascii=False, indent=2)
        print(f"[JSON] 已写出: {json_path}")

    # 输出 Markdown
    md = render_markdown(result)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(md)
        print(f"[MD]   已写出: {args.output}")
    else:
        print(md)
    print("[OK] 深度代码分析完成。")


def render_markdown(r):
    L = []
    L.append("# 深度代码分析报告\n")
    L.append(f"- 项目根目录：`{r['root']}`")
    L.append(f"- 架构风格（推断）：**{r['architectureStyle']}**")
    if r['architectureScores']:
        L.append(f"- 风格信号：{r['architectureScores']}")
    L.append(f"- 入口点：{r['entryPoints'] or '未检测到'}")
    m = r['metrics']
    L.append(f"- 文件数：**{m['fileCount']}**，代码行数：**{m['totalLines']}**")
    L.append(f"- 语言分布：{m['languages']}\n")

    L.append("## DDD 模式识别")
    if r['dddPatterns']:
        for k, v in r['dddPatterns'].items():
            L.append(f"- **{k}**：{', '.join(v) if v else '（无）'}")
    else:
        L.append("- 未识别到明显 DDD 模式（可能为贫血模型或传统分层）\n")

    L.append("## 圈复杂度高危点（Top）")
    if r['complexityHotspots']:
        for h in r['complexityHotspots'][:10]:
            L.append(f"- `{h['name']}`：复杂度≈{h['complexity']}")
    else:
        L.append("- 未检测到明显高危函数\n")

    L.append("## 模块概览（部分）")
    for s in r['fileSummary'][:30]:
        ddd = s['ddd'] and f" / DDD:{s['ddd']}" or ""
        L.append(f"- `{s['file']}` — 类 {s['classes']}，函数 {s['functions']}{ddd}")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
