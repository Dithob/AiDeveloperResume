#!/usr/bin/env python3
"""
解析文件内容（PDF / DOCX / TXT / MD → 纯文本）
用法: python3 parse_file.py "/path/to/file.pdf"

设计原则：任何失败都返回「人话」提示（含原因 + 排查步骤），绝不抛出一堆看不懂的 traceback。
所有提示以 [分类] 开头，便于调用方（或人类）一眼判断出了什么问题。
"""
import sys
import os


def _missing_lib_hint(pkg, path):
    return (
        f"[依赖缺失] 未检测到解析该类型文件所需的库。\n"
        f"  请安装依赖后重试：\n"
        f"    pip install {pkg}\n"
        f"  说明：\n"
        f"    · PDF 推荐 pdfplumber（解析更稳）；若不想装 pdfplumber，也可装 pypdf 作为备选。\n"
        f"    · DOCX 需要 python-docx。\n"
        f"  文件路径：{path}"
    )


def parse_pdf(path):
    # 第一优先：pdfplumber
    try:
        import pdfplumber
    except ImportError:
        # 退而求其次：pypdf
        try:
            from pypdf import PdfReader
        except ImportError:
            return _missing_lib_hint("pdfplumber pypdf", path)
        try:
            reader = PdfReader(path)
            return "\n".join((p.extract_text() or "") for p in reader.pages)
        except Exception as e:
            return _pdf_fail(e, path)
    try:
        with pdfplumber.open(path) as pdf:
            return "\n".join((p.extract_text() or "") for p in pdf.pages)
    except Exception as e:
        return _pdf_fail(e, path)


def _pdf_fail(e, path):
    return (
        f"[PDF 读取失败] 文件可能无法打开、被加密或损坏。\n"
        f"  错误详情：{e}\n"
        f"  排查步骤：\n"
        f"    1. 用浏览器 / 预览工具确认这份 PDF 能正常打开；\n"
        f"    2. 若是扫描件（图片型 PDF），纯文本解析取不到内容，需先做 OCR；\n"
        f"    3. 若是加密 PDF，请先解除密码再解析；\n"
        f"    4. 仍失败可换 pypdf 试一次（pip install pypdf）。\n"
        f"  文件路径：{path}"
    )


def parse_docx(path):
    try:
        from docx import Document
    except ImportError:
        return _missing_lib_hint("python-docx", path)
    try:
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs)
    except Exception as e:
        return (
            f"[DOCX 读取失败] 文件可能损坏或不是有效的 Word 文档。\n"
            f"  错误详情：{e}\n"
            f"  排查步骤：用 Word / WPS 确认能正常打开，或另存为 .docx 后再试。\n"
            f"  文件路径：{path}"
        )


def parse_file(path):
    if not path:
        return "[参数错误] 未提供文件路径。\n  用法：python3 parse_file.py <文件路径>"
    if not os.path.exists(path):
        return (
            f"[文件不存在] 找不到该路径：{path}\n"
            f"  请检查：绝对/相对路径是否正确、是否多了空格或引号、当前工作目录是否是你想的那个。"
        )
    if not os.path.isfile(path):
        return f"[路径非文件] 该路径不是文件（可能是目录）：{path}"

    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return parse_pdf(path)
    if ext in (".docx", ".doc"):
        return parse_docx(path)
    if ext in (".txt", ".md", ".markdown"):
        try:
            with open(path, encoding="utf-8", errors="ignore") as f:
                return f.read()
        except Exception as e:
            return f"[文本读取失败] 无法读取该文本文件：{e}\n  文件路径：{path}"
    # 兜底：尝试按 UTF-8 文本读取
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return (
            f"[格式不支持] 扩展名 {ext or '（无）'} 不被支持，且按纯文本读取也失败。\n"
            f"  支持：.pdf / .docx / .doc / .txt / .md / .markdown\n"
            f"  错误详情：{e}\n"
            f"  文件路径：{path}"
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 parse_file.py <文件路径>")
        print("支持: PDF / DOCX / TXT / MD → 纯文本")
        sys.exit(1)
    # 始终输出到 stdout；失败时返回的是以 [分类] 开头的人话提示，调用方可据此判断。
    print(parse_file(sys.argv[1]))
