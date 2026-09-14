#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_greenbook.py - 面试绿皮书累积器（project-showcase-enhancer 模式 C）

把一问一答的面试对话稿沉淀进长期记忆：
  1. 解析输入 md 里的 Q/A 条目（支持抖音/自己项目面试题/手动 三种来源格式）
  2. 在 memory/绿皮书.md 追加为「面试对话 N」，并更新顶部目录
  3. 维护 memory/index.json（机器可读索引，按技术点检索）
  4. 重建 memory/基因文档.md 的「高频考点」聚合（跨面试共性答案要点）

纯标准库，无第三方依赖。

用法：
  python build_greenbook.py --input dialogue.md --source douyin|<url> --author 张三 --topic 后端八股
  python build_greenbook.py --input 面试题.md --source self-project|youoa --author 我自己 --topic 项目面试题
  python build_greenbook.py --input 任意文本.md --source manual
"""
import argparse
import json
import os
import re
import sys
from datetime import date

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MEMORY = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "memory"))

# 识别「问题」行的多种写法
QUESTION_RE = re.compile(
    r"^(?:#{1,4}\s*)?"                      # 可选 markdown 标题
    r"(?:"                                  # 以下任一开头
    r"Q\s*\d+\s*[:：]"                       # Q1：
    r"|问\s*[:：]"                           # 问：
    r"|问题\s*\d*\s*[:：]"                   # 问题：
    r"|题\s*\d+\s*[:：]"                     # 题1：
    r"|\d+\.\s+"                            # 1. 介绍你的项目
    r")",
    re.I,
)
ANSWER_RE = re.compile(r"^\*\*\s*A\s*\*\*\s*[:：]?\s*(.*)", re.I)
TECH_RE = re.compile(r"技术点\s*\*{0,2}\s*[:：]\s*(.*)", re.I)
STAR_RE = re.compile(r"STAR\s*\*{0,2}\s*[:：]\s*(.*)", re.I)


def parse_qa(text):
    """返回 [{'q':..., 'a':..., 'tech':[...], 'star':...}, ...]"""
    lines = text.splitlines()
    blocks = []
    cur = None
    buf = []

    def flush():
        if cur is not None:
            block_text = "\n".join(buf).strip()
            a = ""
            m = ANSWER_RE.search(block_text)
            if m:
                a = m.group(1).strip()
            # 若没有 **A**：标记，把整段非标题内容当答案
            if not a:
                a = re.sub(r"^\*\*(?:技术点|STAR)\*\*\s*[:：].*$", "", block_text,
                           flags=re.I | re.M).strip()
            tech = []
            mt = TECH_RE.search(block_text)
            if mt:
                raw = re.findall(r"[`「『]?([\u4e00-\u9fa5A-Za-z0-9_+\-/ ]+)[`』」]?",
                                 mt.group(1))
                for t in raw:
                    t = t.strip()
                    if not t:
                        continue
                    if "," in t:  # 无反引号时按逗号拆分
                        tech.extend(x.strip() for x in t.split(",") if x.strip())
                    else:
                        tech.append(t)
                tech = tech[:8]
            star = ""
            ms = STAR_RE.search(block_text)
            if ms:
                star = ms.group(1).strip()
            blocks.append({"q": cur, "a": a, "tech": tech, "star": star})

    for ln in lines:
        if QUESTION_RE.match(ln.strip()):
            flush()
            # 取冒号/点号后的内容作为问题
            q = re.sub(r"^(?:#{1,4}\s*)?(?:Q\s*\d+\s*[:：]|问\s*[:：]|问题\s*\d*\s*[:：]|题\s*\d+\s*[:：]|\d+\.\s+)",
                       "", ln.strip())
            cur = q.strip(" ：:") or ln.strip()
            buf = []
        else:
            if cur is not None:
                buf.append(ln)
    flush()
    return [b for b in blocks if b["q"]]


def read_existing(path):
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def next_dialogue_index(greenbook_text):
    idxs = [int(m) for m in re.findall(r"##\s*面试对话\s*(\d+)", greenbook_text)]
    return (max(idxs) + 1) if idxs else 1


def append_greenbook(memory_dir, entries, meta):
    gb_path = os.path.join(memory_dir, "绿皮书.md")
    existing = read_existing(gb_path)
    idx = next_dialogue_index(existing)

    anchor = f"面试对话{idx}"
    section = [f"\n---\n", f"\n## {anchor}",
               f"**来源**：{meta['source']}  ",
               f"**作者/候选人**：{meta['author']}  ",
               f"**日期**：{meta['date']}  ",
               f"**主题**：{meta['topic']}\n"]
    for i, e in enumerate(entries, 1):
        section.append(f"\n### Q{i}：{e['q']}")
        section.append(f"**A**：{e['a']}")
        if e["tech"]:
            section.append("**技术点**：" + " ".join(f"`{t}`" for t in e["tech"]))
        if e["star"]:
            section.append(f"**STAR**：{e['star']}")
    section.append("")

    if not existing:
        # 首次创建：写标题 + 目录占位 + 分隔
        new_content = ("# 面试绿皮书 📗\n"
                       "> 持续累积的一问一答题库。每次分析自动追加，只增不覆盖。\n\n"
                       "## 目录\n")
        # 目录稍后统一重建
        body = new_content + "\n" + "\n".join(section)
    else:
        # 插到「## 目录」之后、第一个「---」之前；简单起见追加到文末
        body = existing.rstrip() + "\n" + "\n".join(section)

    # 重建目录
    body = rebuild_catalog(body, idx, meta)
    with open(gb_path, "w", encoding="utf-8") as fh:
        fh.write(body)
    return gb_path, idx


def rebuild_catalog(body, idx, meta):
    """把本次新增的目录项写进顶部「## 目录」。"""
    new_bullet = (f"- [面试对话{idx} · {meta['topic']} · {meta['date']} · "
                  f"{meta['source']}](#面试对话{idx})")
    if "## 目录" in body:
        # 在 ## 目录 行后插入
        parts = body.split("## 目录", 1)
        head = parts[0] + "## 目录\n"
        rest = parts[1]
        # 避免重复
        if new_bullet.split("]")[0] not in rest:
            rest = "\n" + new_bullet + rest
        return head + rest
    return body


def update_index(memory_dir, idx, entries, meta):
    idx_path = os.path.join(memory_dir, "index.json")
    data = {"interviews": []}
    if os.path.exists(idx_path):
        try:
            with open(idx_path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception:
            data = {"interviews": []}
    rec = {
        "id": idx,
        "source": meta["source"],
        "author": meta["author"],
        "topic": meta["topic"],
        "date": meta["date"],
        "questions": [{"q": e["q"], "tech": e["tech"]} for e in entries],
    }
    data["interviews"].append(rec)
    with open(idx_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    return idx_path


def rebuild_gene(memory_dir):
    """按技术点聚合高频考点，重建 基因文档.md。"""
    idx_path = os.path.join(memory_dir, "index.json")
    if not os.path.exists(idx_path):
        return None
    with open(idx_path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    tech_map = {}  # tech -> [{"q":..., "source":...}, ...]
    for it in data["interviews"]:
        for q in it["questions"]:
            for t in q.get("tech", []):
                tech_map.setdefault(t, []).append(
                    {"q": q["q"], "source": it["source"], "topic": it["topic"]})

    lines = ["# 面试基因文档 🧬",
             "> 按技术点聚合的长期知识库。每次 build_greenbook 自动重建。\n",
             "## 高频考点（按出现次数排序）\n"]
    ranked = sorted(tech_map.items(), key=lambda x: -len(x[1]))
    if not ranked:
        lines.append("- 暂无带技术点标签的问答，先给对话打上「技术点」标签。\n")
    for tech, items in ranked:
        lines.append(f"\n### `{tech}`（被问 {len(items)} 次）")
        seen = set()
        for it in items:
            key = it["q"]
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"- {it['q']}  _{it['source']} · {it['topic']}_")
    out = "\n".join(lines) + "\n"
    gene_path = os.path.join(memory_dir, "基因文档.md")
    with open(gene_path, "w", encoding="utf-8") as fh:
        fh.write(out)
    return gene_path


def main():
    ap = argparse.ArgumentParser(description="面试绿皮书累积器")
    ap.add_argument("--input", required=True, help="对话稿/面试题 markdown")
    ap.add_argument("--source", required=True,
                    help="来源：douyin|<url> / self-project|<项目名> / manual")
    ap.add_argument("--author", default="未知", help="作者/候选人")
    ap.add_argument("--topic", default="未命名", help="主题")
    ap.add_argument("--date", default=date.today().isoformat(), help="日期 YYYY-MM-DD")
    ap.add_argument("--memory", default=DEFAULT_MEMORY, help="memory 目录路径")
    args = ap.parse_args()

    memory_dir = os.path.abspath(args.memory)
    os.makedirs(memory_dir, exist_ok=True)

    with open(args.input, "r", encoding="utf-8") as fh:
        text = fh.read()
    entries = parse_qa(text)
    if not entries:
        print("[警告] 未从输入中解析到任何 Q/A 条目。请确认格式含 Q1：/问：/1. 等标记。",
              file=sys.stderr)
        sys.exit(1)

    meta = {"source": args.source, "author": args.author,
            "topic": args.topic, "date": args.date}

    gb_path, idx = append_greenbook(memory_dir, entries, meta)
    idx_path = update_index(memory_dir, idx, entries, meta)
    gene_path = rebuild_gene(memory_dir)

    print(f"[OK] 已追加为「面试对话{idx}」，共 {len(entries)} 条问答。")
    print(f"     绿皮书  : {gb_path}")
    print(f"     索引    : {idx_path}")
    if gene_path:
        print(f"     基因文档: {gene_path}")


if __name__ == "__main__":
    main()
