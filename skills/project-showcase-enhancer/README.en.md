<p align="center">
  <img src="./images/logo.svg" width="120" alt="Project Showcase Enhancer" />
</p>

<h1 align="center">Project Showcase Enhancer · Interview War Room</h1>

<p align="center">
  <b>Evolve your demo-grade project into a commercial-grade product — and prep the interview while you are at it. One Agent Skill that runs the full loop: understand your own code → learn from real interviews → accumulate a persistent Q&amp;A bank.</b>
</p>

<p align="center">
  🌐 <a href="./README.md">Bilingual</a> &nbsp;·&nbsp; 🇨🇳 <a href="./README.zh-CN.md">中文</a>
</p>

<p align="center">
  <img alt="Agent Skill" src="https://img.shields.io/badge/Agent--Skill-00b4d8" />
  <img alt="Modes" src="https://img.shields.io/badge/modes-4-8b5cf6" />
  <img alt="Architecture" src="https://img.shields.io/badge/architecture-hybrid-10b981" />
  <img alt="Rating" src="https://img.shields.io/badge/SkillHub-4.5%2F5-ffb703" />
  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen" />
  <img alt="Models" src="https://img.shields.io/badge/models-Opus%204.6%20%7C%20DeepSeek%20v4%20Pro%20%7C%20GPT--5.6-ff6b35" />
</p>

---

## What is this?

**Project Showcase Enhancer · Interview War Room** is an **Agent Skill** for **programmers who are actively preparing for interviews**. It is not a "scan the code and emit a template" tool. It is a **human-in-the-loop interview-prep workflow**: first it reads your code and your original intent, then it works with you to evolve the demo into a commercial-grade product plan, and finally it produces ready-to-use documents — a **project showcase document**, a **JD-driven mock interview**, an **interview prep guide**, and a continuously growing **interview green book (绿皮书)**.

### The real pain point: what blocks you is not "can you code"

You are a programmer heading into an interview soon. The hard part is turning code into a ticket through the door:

- **Resume project bullets fall flat:** the code runs, but the "project experience" line only says "a blog built with React + Node" — no technical depth, no business value.
- **The portfolio-site project page is weak:** you built the portfolio site, but the project detail page is hollow, like a copy-paste of the README.
- **You have the JD but no idea how the interviewer will probe:** the JD for your dream role sits there, yet you lack a **JD-driven mock interview** to rehearse beforehand.
- **The project is not impressive enough, so it needs honest packaging:** your real project may not be "grand", but what you want is to **amplify the real highlights professionally — not fabricate**.
- **You want to learn from others' real interviews:** tons of UP-owners share real interview audio on Douyin, but no one systematically breaks down what was asked and how it was answered impressively.

Building on v1, it merges four sources into four modes:

- From **code-project-analyzer** — the original script and ideas for code scanning and project documentation.
- From **Code Analyzer** — deep code interpretation (architecture / call graph / data flow / DDD patterns).
- From **douyin-analyzer** — Douyin video parsing → extract voice → Whisper transcription → structured content.
- From **Self-Improving + 总结** — long-term memory accumulation + layered Q&A distillation.

This skill ties those threads into one chain: **understand your own code → learn from real interviews → evolve / package the project → rehearse with a JD-driven mock interview → accumulate a persistent Q&A bank**.

## Four modes at a glance

```
┌─────────────────────────────────────────────────────────────┐
│  Mode A  Deep code analysis   → Understand your own code     │
│  Mode B  Douyin interview      → Learn from real interviews   │
│  Mode C  Interview green book  → Accumulate Q&A (long memory) │
│  Mode D  Showcase + questions  → Original power, feeds C      │
└─────────────────────────────────────────────────────────────┘
      Outputs of A / B / D (Q&A) ──┐
                                  ▼
                    memory/ Interview Green Book (grows)
```

| Mode | In one line | Input | Output |
|---|---|---|---|
| **A Deep code analysis** | Explain how the code actually works (see a deeper layer) | project dir | `{project}-deep-analysis.md` |
| **B Douyin interview** | Turn an interview video into structured Q&A (learn from others) | Douyin link | `{author}-{title}-interview-dialogue.md` |
| **C Interview green book** | Accumulate Q&A as long-term memory | dialogue / questions / manual text | `memory/绿皮书.md` + `基因文档.md` |
| **D Showcase + questions + JD mock interview** | Write a sharp resume / package the project / JD role-play | project dir + (optional) JD/resume | `{project}-showcase.md` + `{project}-interview-prep.md` + `{project}-{role}-mock-interview.md` |

### Interview-prep chain: the six things that block you, and which mode answers them

| What blocks you while prepping | Mode | Key output |
|---|---|---|
| ① Understand your own project, see a deeper layer | **A Deep code analysis** | `{project}-deep-analysis.md` |
| ② Write the project as a sharp resume / portfolio page | **D Showcase** | `{project}-showcase.md` |
| ③ Package the highlights honestly (facts, no fabrication) | **D Evolve / package** | commercial evolution + gap roadmap |
| ④ Rehearse with a JD-driven mock interview | **D JD mock interview** (+ A) | `{project}-{role}-mock-interview.md` |
| ⑤ Learn from others' real interview videos | **B Douyin interview** | `{author}-{title}-interview-dialogue.md` |
| ⑥ Accumulate your own question bank for long-term review | **C Interview green book** | `memory/绿皮书.md` + `基因文档.md` |

## Highlights

> **The script provides a deterministic map; the model does deep reasoning on that map — together they are fast, accurate, and token-efficient.** — the core design

- **Real code comprehension (Mode A):** a script does a deterministic scan, then the model reads key source files to explain architecture, call chains, data flow, and whether DDD is truly applied — not guesswork from file names.
- **Learn from real interviews (Mode B):** give it a Douyin interview video; it extracts the voice track → transcribes → splits into Q&A by "interviewer asks / candidate answers", tagging tech points and STAR.
- **Interview green book (Mode C):** every analysis is distilled into long-term memory, accumulating across sessions and sources (Douyin / your project / manual), clustered by tech point into a "gene document" — your private high-frequency question bank.
- **Demo-to-commercial evolution (Mode D):** given your product vision, it lists gaps across functionality, engineering, and operations, then gives a phased roadmap (MVP → polish → commercial).
- **Hybrid architecture:** scripts do the fast, stable scan and transcription; the model does the deep, accurate reasoning.

## Get started

### Prerequisites

```bash
# 1. A client that supports "Agent Skills" (this skill ships as a user-level skill)
# 2. Recommended to run under a "high-reasoning model" (see Configuration)
#    Recommended: Claude Opus 4.6 / DeepSeek v4 Pro / GPT-5.6

# 3. (Optional) install dependencies per the mode you need:
pip install pdfplumber python-docx pypdf                      # resume parsing (Mode D)
pip install openai-whisper requests scipy imageio-ffmpeg      # Douyin interview (Mode B)
node runtime                                                   # code scanning (Mode A/D)
```

### Install the skill

```bash
# Option 1: clone into the user-level skills directory
git clone https://github.com/whishi47/project-showcase-enhancer-skill.git \
  "$HOME/.workbuddy/skills/project-showcase-enhancer"

# Option 2: extract the zip into $HOME/.workbuddy/skills/project-showcase-enhancer/
#   Make sure SKILL.md sits directly inside that directory

# Option 3: install from SkillHub
#   Search for project-showcase-enhancer-skill on SkillHub and install it
```

> On Windows, `$HOME` is usually `C:\Users\your-username`. The skills directory may also be `.codebuddy\skills` depending on your client. No build step is required; trigger the skill with plain language in a conversation.

### One-line triggers

| Trigger | Say this | Enters |
|---|---|---|
| 💬 Natural language | "Deep-analyze my project" | Mode A |
| 💬 Natural language | "Analyze this Douyin interview video: <link>" | Mode B |
| 💬 Natural language | "Save this interview dialogue into the green book" | Mode C |
| 💬 Natural language | "Evolve this project to commercial, and give me a showcase doc + interview questions" | Mode D |
| 📎 Resume file | Upload PDF / DOCX / TXT | Parsed to text for Mode D |

On first trigger, the skill asks at once (answer together): **which mode**, **project path / Douyin link / existing dialogue**, **(Mode D) use case & target role**.

## Walkthrough: run each of the four modes

> Saying "it generates documents" is too abstract. Below, each mode is **actually run**, so you can see what "command → output" looks like. Outputs are excerpts; real results are longer and fuller.

### Mode A · Deep code analysis

You: *"Deep-analyze `./my-app`."*

The skill runs two scripts first (deterministic scan), then the model interprets deeply on top of the "map":

```bash
node scripts/scan_project.js ./my-app
python scripts/deep_analyze.py ./my-app --output my-app-deep-analysis.md
```

`deep_analyze.py` gives structured judgments; the model writes evidence-backed interpretation with file/function names. Sample excerpt:

```markdown
## Architecture style
Detected **Layered** architecture: controller → service → repository,
boundaries clear; but `service/OrderService.java` also handles "send email"
and "compute inventory" — a god-class tendency.

## DDD pattern review
- Aggregate root: Order (with OrderItem value object) ✅ correctly applied
- Repository: OrderRepository interface + MyBatis impl ✅
- ⚠️ Anemic-model warning: `User` entity has only getters/setters;
  business rules (e.g. "disabled user cannot order") live in Service, not the entity.

## Key call chain
OrderController.createOrder() → OrderService.create()
  → InventoryService.lock() → OrderRepository.save()
```

### Mode B · Douyin interview analysis

You: *"Analyze this Douyin interview video: https://v.douyin.com/xxxx/"*

```bash
python scripts/douyin_interview.py --url "https://v.douyin.com/xxxx/" --output interview-raw.md
```

Pipeline: bugpk metadata → download → extract **voice** track → Whisper transcription → polish & structure. Sample excerpt (`{author}-{title}-interview-dialogue.md`):

```markdown
### Q1: How do you solve Redis cache penetration?
**A**: Cache null values + Bloom filter as two gates; hot keys use logical
expiry to avoid breakdown……
**Tech points**: `Redis` `cache penetration` `Bloom filter`
**STAR**: Candidate cited a "flash-sale inventory" scenario, QPS 2k → 50k.

### Q2: Redis or ZooKeeper for distributed locks?
**A**: CAP trade-off — Redis is fast but needs lock-expiry handling;
ZK is strongly consistent but lower throughput……
**Tech points**: `distributed lock` `ZooKeeper` `Redisson`
```

> If the current model is **not multimodal**, visual analysis is skipped automatically and only the audio flow runs — with a clear note. It will not pretend to have analyzed the video frames.

### Mode C · Interview green book

You: *"Save this interview dialogue into the green book."*

```bash
python scripts/build_greenbook.py \
  --input interview-raw.md \
  --source "douyin|https://v.douyin.com/xxxx/" \
  --author "Tech UP-owner Lao Li" \
  --topic "Backend fundamentals" \
  --date "2026-07-25"
```

The script appends the Q&A into `memory/绿皮书.md` (auto-numbered "Interview Dialogue N"), updates the table of contents, and maintains `memory/index.json` and `memory/基因文档.md`. Sample excerpt:

```markdown
# Interview Green Book 📗
## Table of contents
- [Interview Dialogue 1 · Backend fundamentals · 2026-07-25 · douyin](#interview-dialogue-1)

## Interview Dialogue 1
**Source**: douyin · https://v.douyin.com/xxxx/ | **Author**: Tech UP-owner Lao Li | **Date**: 2026-07-25

### Q1: How do you solve Redis cache penetration?
**A**: Cache null values + Bloom filter……
**Tech points**: `Redis` `cache penetration` `Bloom filter`
```

`基因文档.md` clusters by tech point, accumulating "high-frequency question → recommended answer skeleton" over time:

```markdown
## Redis
- Cache penetration (asked 3×): cache null + Bloom filter [from Dialogue 1/3/5]
- Distributed lock (asked 2×): Redisson watchdog auto-renew [from Dialogue 1/4]
```

### Mode D · Showcase + interview questions + JD mock interview

You: *"Evolve `./my-app` to commercial, give me a showcase doc, 15 interview questions from my JD, and run a JD mock interview — save them all into the green book."*

After the evolution dialogue, the skill produces three documents: the showcase doc, the interview prep guide, and the **JD-driven mock interview**. The prep questions and mock-interview Q&A prompt you to call Mode C (source `self-project`) to accumulate them too.

`{project}-interview-prep.md` sample (excerpt):

```markdown
### Must-ask 1: How do you guarantee consistency in order creation?
- Tested: transaction boundary, eventual consistency, idempotency
- Strategy: local transaction (@Transactional) first, then message-table for cross-service eventual consistency
- STAR: duplicate orders from resubmission → solved with an idempotency key
```

`{project}-{role}-mock-interview.md` sample (excerpt, role-play style):

```markdown
> Interviewer视角 (based on your JD "high-concurrency trading system" + your real code)
**Q**: You used a local transaction for order creation. If deducting inventory and
  creating the order are not in the same database, how do you keep consistency?
**Recommended answer**: ① admit a local transaction can't span databases; ② use a
  "local message table / Saga" for eventual consistency; ③ back it with the real
  `InventoryService.lock()` logic in your project; ④ mention an idempotency key.
**Follow-up (interviewer)**: What if the message is lost?
**Recommended answer**: message table + scheduled reconciliation + manual fallback;
  in our project, after `OrderRepository.save()` we emit an event via transactional outbox……
```

## How it works

```
┌──────────────────────────────────────────────────────────┐
│            project-showcase-enhancer-skill                 │
│   Input: project dir / Douyin link / dialogue + opt JD+resume│
└───────────────────────────┬──────────────────────────────┘
                            ▼
   ┌──────────────────────────────────────────────┐
   │ A Deep code analysis                           │
   │   scan_project.js + deep_analyze.py (scripts)  │
   │   + model semantic interpretation              │
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ B Douyin interview analysis                    │
   │   douyin_interview.py (parse→voice→Whisper→struct)│
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ C Interview green book (long-term memory)      │
   │   build_greenbook.py → memory/ (append-only)   │
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ D Showcase + questions (original power kept)   │
   │   → {project}-showcase.md + interview-prep.md  │
   └──────────────────────────────────────────────┘
```

**Three-layer hybrid architecture:** ① scripts do deterministic scan / transcription (fast, stable, no semantic cost); ② the model does the deep reasoning only an LLM can do, on top of script output; ③ the green book turns outputs into cross-session long-term memory.

## Mode details

### Mode A: Deep code analysis (merges Code Analyzer)

- **A.1 Scan:** `scan_project.js` (stack/deps/tree) + `deep_analyze.py` (architecture/call graph/data flow/DDD/complexity), → JSON + Markdown.
- **A.2 Read:** the model **must cite file names, function names, code snippets**, explaining architecture, execution flow, data flow, business rules, and reviewing DDD authenticity.
- **A.3 Output:** `{project}-deep-analysis.md`, also feeds Mode D's "technical depth" section.
- Constraint: Mode A must run both scripts first; do not skip them and guess with the LLM.

### Mode B: Douyin interview analysis (merges douyin-analyzer, conditional vision)

- **B.1** receive link → **B.2** run `douyin_interview.py` (parse→download→voice→Whisper→optional frames).
- **B.3** polish → **B.4** structure (core): the model tags "interviewer / candidate", splitting each into Q/A + tech points + STAR.
- **B.5** visual analysis (multimodal only): frame descriptions + production-style guess, as a "video form" note, not affecting the Q&A.
- **B.6** into green book: the skill prompts you to accumulate the Q&A into `memory/绿皮书.md`.
- Missing deps → the script **prompts the install command at entry and stops**, never failing silently.

### Mode C: Interview green book (merges Self-Improving + 总结)

- **C.1** three sources: Douyin video, your project questions, manual text.
- **C.2** run `build_greenbook.py` → parse Q&A, append as "Interview Dialogue N", update TOC + `index.json`, maintain `基因文档.md`.
- **C.3** green book structure: TOC on top + each Q&A tagged with `tech points` / `STAR`.
- **C.4** gene document: long-term knowledge base clustered by tech point, reviewable alone.
- Memory rules: append-only, never overwrite; every Q&A tagged with its source (douyin / self-project / manual), traceable.

### Mode D: Showcase + interview questions + JD mock interview (original power kept, enhanced)

- **D.1** project positioning → **D.2** commercial evolution dialogue (vision→gaps P0/P1/P2→roadmap, honest packaging, label "planned").
- **D.3** deliverables: showcase doc (sharp resume / portfolio page) + 15 questions (must-ask / targeted / follow-up) + **JD-driven mock interview** (role-play: interviewer questions + recommended answers + follow-up chain).
- **D.4** honest packaging: use Mode A's code evidence to upgrade "built a feature" into "solved a business problem, made engineering trade-offs" — never fabricate.
- **D.5** into green book: the skill prompts you to accumulate the prep questions and mock-interview Q&A via Mode C (source `self-project`).

## Common pitfalls

> This section is dedicated to the traps. Avoid them and you save a lot of debugging time.

1. **Model is not high-reasoning:** with a low-reasoning model, code comprehension is shallow, evolution is templated, and Q&A splitting is messy. Check the skill's prompt at entry; switch to Opus 4.6 / DeepSeek v4 Pro / GPT-5.6 if needed.
2. **Skipping scripts and guessing with the LLM:** Mode A must run `scan_project.js` + `deep_analyze.py` first; Mode B must run `douyin_interview.py` first. Without scripts, conclusions lack evidence.
3. **Douyin link expired / bugpk parse failed:** share codes or short links may expire. The pipeline reports a clear error at entry; retry with a link that opens normally.
4. **Whisper not installed:** Mode B depends on `openai-whisper`. If missing, the script prompts `pip install openai-whisper requests scipy imageio-ffmpeg` and stops — do not force-run it.
5. **Memory dir not committed to git:** the green book and gene document under `memory/` are long-term assets. Before changing machines / reinstalling, `git add memory/ && git commit && git push`, or the question bank is lost.
6. **Forcing visual analysis on a non-multimodal model:** in Mode B, if the model does not support images, visual analysis auto-degrades to audio-only — do not mistake it for "frame analysis done".
7. **Resume parse reports "missing dependency / read failed":** see "Bundled scripts" below. Usually `pdfplumber` is not installed, or the PDF is encrypted / a scan — install the dependency or use OCR per the prompt.

## Configuration

This skill requires a **high-reasoning model**. **Recommended:**

- Claude Opus 4.6
- DeepSeek v4 Pro
- GPT-5.6 (or equivalent)

A low-reasoning model still runs, but quality drops noticeably. The skill prompts you to confirm the current model at entry and suggests switching if it does not meet the bar.

> 💡 Tip: set your preferred high-reasoning model as the client default, or switch manually before triggering the skill, for the best results.

**Multimodal requirement (Mode B visual analysis only):** when Mode B triggers, the skill first detects whether the current model supports image input; if not, it auto-degrades to the audio-only flow.

## Bundled scripts

### `scripts/scan_project.js`

Scans a project with a hard-coded dictionary and emits structured JSON. It does not call a model, so it is fast and deterministic.

```bash
node scripts/scan_project.js <project-directory> [--max-depth N]
```

> **Error messages improved (v2):** if the path does not exist / is not a directory, it intercepts at entry with a clear checklist instead of silently emitting empty output; if a subdirectory cannot be read mid-scan, it is skipped and written to `warnings`, and all warnings are summarized to stderr at the end without breaking the stdout JSON.

### `scripts/deep_analyze.py`

AST / heuristic deep analysis (architecture style, call graph, data flow, DDD patterns, high-complexity hotspots), → JSON + Markdown. Pure standard library, no third-party deps.

```bash
python scripts/deep_analyze.py <project-directory> --output report.md
```

### `scripts/douyin_interview.py`

Douyin interview pipeline: parse + download + extract voice + Whisper transcription + optional frames.

```bash
python scripts/douyin_interview.py --url "<Douyin link>" --output interview-raw.md
```

Dependencies: `openai-whisper requests scipy imageio-ffmpeg`. If missing, it prompts the install command at entry and stops.

### `scripts/build_greenbook.py`

Q&A → accumulate green book + gene document + index. Pure standard library.

```bash
python scripts/build_greenbook.py --input dialogue.md \
  --source "douyin|<url>" --author "<author>" --topic "<topic>" --date "YYYY-MM-DD"
```

### `scripts/parse_file.py`

Parses a resume PDF / DOCX / TXT into plain text (for Mode D).

```bash
python scripts/parse_file.py ./resume.pdf
```

> **Error messages improved (v2):** any failure returns human-readable text prefixed with `[category]` — cause + troubleshooting steps — **no more unreadable tracebacks**. Common cases:
> - `[依赖缺失] / [dependency missing]`: `pdfplumber`/`pypdf`/`python-docx` not installed → prompts `pip install ...`
> - `[PDF 读取失败] / [PDF read failed]`: encrypted / corrupt / scanned PDF → prompts to decrypt, use OCR, or try pypdf
> - `[文件不存在] / [file not found]` · `[路径非文件] / [not a file]` · `[格式不支持] / [unsupported format]`: path or extension issue → prompts to verify the path and supported formats

## Directory layout

```
project-showcase-enhancer/
├── SKILL.md                          # Skill definition (workflow)
├── README.md                         # Bilingual version (main doc)
├── README.en.md                      # This document (English version)
├── README.zh-CN.md                   # Chinese version
├── 简介.md                            # SkillHub review intro copy
├── images/
│   └── logo.svg
├── scripts/
│   ├── scan_project.js               # Project scanner: dictionary match → JSON
│   ├── deep_analyze.py               # Deep code analysis: AST/heuristic → JSON+MD
│   ├── douyin_interview.py           # Douyin pipeline: parse→voice→Whisper→struct
│   ├── build_greenbook.py            # Green book accumulator: Q&A → long-term memory
│   └── parse_file.py                 # Resume parser: PDF/DOCX/TXT → text
├── assets/
│   ├── showcase-template.md          # Project showcase document template
│   ├── interview-prep-template.md    # Interview prep guide template
│   ├── deep-analysis-template.md     # Deep code analysis template
│   ├── interview-dialogue-template.md# Q&A dialogue template
│   └── greenbook-template.md         # Interview green book template
└── memory/                           # Long-term memory (committed to git)
    ├── 绿皮书.md                       # Growing Q&A question bank
    ├── 基因文档.md                     # High-frequency points clustered by tech
    └── index.json                     # Machine-readable index
```

## What users say (SkillHub rating)

Published on SkillHub with an overall score of **4.5 / 5 (the maximum is 4.5)**. The original dimension comments are below; v2 addresses each point:

> **C · Convention 4.2 / 5**
> "The documentation is well-structured, guiding from shallow to deep, with ready-to-use templates and scripts that quickly scan the project. But it lacks step-by-step practical examples — you never see what the final output actually looks like, and no one tells you where things easily go wrong."

> **R · Reliability 4.4 / 5**
> "Overall quite reliable; scanning and analysis rarely crash, and the two scripts skip minor issues and keep going instead of erroring out. It covers the full chain from project analysis to interview prep, with rich templates. However, if the PDF library is not installed, or a directory read fails, the messages are not clear enough and require some troubleshooting ability."

**How v2 responds:**

- "No practical examples" → new **[Walkthrough](#walkthrough-run-each-of-the-four-modes)** section: each of the four modes shows "what you say → command to run → real sample output".
- "No one tells you where it goes wrong" → new **[Common pitfalls](#common-pitfalls)** section: seven high-frequency traps and how to avoid them.
- "PDF lib / directory read messages unclear" → rewrote `parse_file.py` and `scan_project.js` error handling: every failure returns human-readable text with cause + steps; missing/non-directory paths are intercepted at entry, and mid-scan read failures are written to `warnings` and summarized.

## Publish

```bash
# Option 1: SkillHub web
#   Go to https://skillhub.cn , upload the packaged project-showcase-enhancer.zip
#   Slug: project-showcase-enhancer, Display name: 个人项目展示增强器 · 面试作战室

# Option 2: SkillHub CLI
#   After login, run: skillhub publish ./project-showcase-enhancer-skill

# Repackage (requires skill-creator's package_skill.py)
python package_skill.py ./project-showcase-enhancer-skill ./dist
```

> Bump the `version` field in SKILL.md before publishing.

## License

MIT © 2026
