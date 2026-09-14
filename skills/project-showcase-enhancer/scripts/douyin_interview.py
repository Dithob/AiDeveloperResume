#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
douyin_interview.py - 抖音面试视频分析管道（project-showcase-enhancer 模式 B）

融合 douyin-analyzer 的音频能力，做成「面试专用」管道：
  1. 调用 bugpk API 解析抖音视频元数据
  2. 下载视频
  3. 提取「人声」音轨（面试场景要人声，不是 BGM）
  4. Whisper 本地转写（MP3 -> 16k WAV -> 文本 + 分段）
  5. （可选 --frames）逐帧截取，供多模态模型做视觉描述

依赖：
  pip install openai-whisper requests scipy imageio-ffmpeg

注意：
  - bugpk API 为第三方服务，可能限流/失效，脚本会在解析失败时给出明确错误
  - 若只需音频流程（当前模型非多模态），不要传 --frames 即可
  - 转写语言默认中文（model="base"），可用 --model 调整（medium/large 更准更慢）

用法：
  python douyin_interview.py --url "https://v.douyin.com/xxx/" --output interview-raw.md
  python douyin_interview.py --url "..." --frames --fps 0.5 --max-frames 12
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

API_URL = "https://api.bugpk.com/api/douyin"

try:
    import requests
except ImportError:
    print("[依赖缺失] 请先安装: pip install requests", file=sys.stderr)
    sys.exit(2)


# ---------------------------------------------------------------------------
# 1. 解析元数据
# ---------------------------------------------------------------------------
def analyze_douyin(url):
    print(f"[1/5] 解析抖音元数据: {url}")
    try:
        r = requests.get(API_URL, params={"url": url}, timeout=20)
        data = r.json()
    except Exception as e:
        print(f"[错误] 调用 bugpk API 失败: {e}", file=sys.stderr)
        sys.exit(1)
    if data.get("code") != 200:
        print(f"[错误] API 返回非 200: {data}", file=sys.stderr)
        sys.exit(1)
    return data.get("data", data)


def pick_best_video_url(d):
    for key in ("url", "video_url"):
        if d.get(key):
            return d[key]
    backups = d.get("video_backup") or []
    if backups:
        return backups[0]
    # 兼容嵌套
    if isinstance(d.get("video"), dict):
        return d["video"].get("url") or (d["video"].get("backup") or [None])[0]
    return None


# ---------------------------------------------------------------------------
# 2. 下载视频
# ---------------------------------------------------------------------------
def download_file(url, output_path):
    print(f"[2/5] 下载视频...")
    try:
        r = requests.get(url, timeout=60, stream=True)
        r.raise_for_status()
        with open(output_path, "wb") as fh:
            for chunk in r.iter_content(1024 * 256):
                fh.write(chunk)
        print(f"      已保存: {output_path}")
        return output_path
    except Exception as e:
        print(f"[错误] 下载失败: {e}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# 3. 提取人声音轨
# ---------------------------------------------------------------------------
def get_ffmpeg_path():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        # 退回到系统 PATH 中的 ffmpeg
        return "ffmpeg"


def extract_voice(video_path, out_mp3):
    print(f"[3/5] 提取人声音轨 (ffmpeg)...")
    ffmpeg = get_ffmpeg_path()
    # 用 highpass 滤掉低频 BGM 干扰；保留人声频段
    cmd = [
        ffmpeg, "-y", "-i", video_path,
        "-vn", "-ac", "1", "-ar", "16000",
        "-af", "highpass=f=200,lowpass=f=3000",
        out_mp3,
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        print(f"      人声已提取: {out_mp3}")
        return out_mp3
    except subprocess.CalledProcessError as e:
        print(f"[警告] ffmpeg 提取失败({e})，尝试直接转写视频原音", file=sys.stderr)
        return video_path


# ---------------------------------------------------------------------------
# 4. Whisper 转写
# ---------------------------------------------------------------------------
def transcribe(mp3_path, model_name="base", language="zh"):
    print(f"[4/5] Whisper 转写 (model={model_name}, lang={language})...")
    try:
        import whisper
    except ImportError:
        print("[依赖缺失] 请先安装: pip install openai-whisper", file=sys.stderr)
        sys.exit(2)
    model = whisper.load_model(model_name)
    result = model.transcribe(mp3_path, language=language, verbose=False)
    text = result.get("text", "").strip()
    segments = [{"start": s["start"], "end": s["end"], "text": s["text"].strip()}
                for s in result.get("segments", [])]
    print(f"      转写字数: {len(text)}")
    return {"text": text, "segments": segments}


# ---------------------------------------------------------------------------
# 5. 逐帧截取（供多模态模型视觉描述）
# ---------------------------------------------------------------------------
def extract_frames(video_path, output_dir, fps=0.5, max_frames=12):
    print(f"[5/5] 逐帧截取 (fps={fps}, max={max_frames})...")
    try:
        import imageio_ffmpeg
    except ImportError:
        print("[依赖缺失] 请先安装: pip install imageio-ffmpeg", file=sys.stderr)
        sys.exit(2)
    ffmpeg = get_ffmpeg_path()
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        ffmpeg, "-y", "-i", video_path,
        "-vf", f"fps={fps}", "-frames:v", str(max_frames),
        os.path.join(output_dir, "frame_%03d.png"),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    frames = sorted(os.path.join(output_dir, f)
                    for f in os.listdir(output_dir) if f.endswith(".png"))
    print(f"      截出 {len(frames)} 帧 -> {output_dir}")
    return frames


# ---------------------------------------------------------------------------
# 报告生成
# ---------------------------------------------------------------------------
def generate_report(meta, transcription, frames=None):
    title = meta.get("title", "未知标题")
    author = (meta.get("author") or {}).get("name", "未知作者") if isinstance(meta.get("author"), dict) else meta.get("author", "未知作者")
    lines = []
    lines.append("# 抖音面试视频 · 原始分析稿\n")
    lines.append(f"- **标题**：{title}")
    lines.append(f"- **作者**：{author}")
    lines.append(f"- **时长**：{meta.get('duration', '未知')} 秒")
    lines.append("")
    lines.append("## 原始转写文本\n")
    lines.append(transcription["text"] or "（转写为空，请检查音频质量）")
    lines.append("")
    if frames:
        lines.append("## 视频帧（供多模态模型视觉描述）\n")
        for fr in frames:
            lines.append(f"- 帧截图：`{fr}`")
        lines.append("\n> 把以上帧图发送给多模态模型，用自然语言描述画面"
                     "（色调/人物/场景/字幕/AI破绽），判断制作方式。")
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="抖音面试视频分析管道")
    ap.add_argument("--url", required=True, help="抖音视频链接")
    ap.add_argument("--output", help="输出 markdown 路径")
    ap.add_argument("--model", default="base", help="Whisper 模型")
    ap.add_argument("--language", default="zh", help="转写语言")
    ap.add_argument("--frames", action="store_true", help="额外逐帧截取（需多模态模型）")
    ap.add_argument("--fps", type=float, default=0.5)
    ap.add_argument("--max-frames", type=int, default=12)
    ap.add_argument("--workdir", default=".", help="工作目录（下载/中间文件）")
    args = ap.parse_args()

    os.makedirs(args.workdir, exist_ok=True)
    meta = analyze_douyin(args.url)
    video_url = pick_best_video_url(meta)
    if not video_url:
        print("[错误] 未从 API 返回中提取到视频直链", file=sys.stderr)
        sys.exit(1)

    video_path = os.path.join(args.workdir, "interview_video.mp4")
    download_file(video_url, video_path)

    voice_mp3 = os.path.join(args.workdir, "voice.mp3")
    extract_voice(video_path, voice_mp3)

    transcription = transcribe(voice_mp3, args.model, args.language)

    frames = None
    if args.frames:
        frames = extract_frames(video_path,
                                os.path.join(args.workdir, "frames"),
                                args.fps, args.max_frames)

    md = generate_report(meta, transcription, frames)
    out = args.output or os.path.join(args.workdir, "interview-raw.md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"\n[OK] 原始分析稿已写出: {out}")
    print("下一步：把该稿交给 LLM 做「面试对话结构化」（模式 B.4），"
          "或调用 build_greenbook.py 沉淀进绿皮书（模式 C）。")


if __name__ == "__main__":
    main()
