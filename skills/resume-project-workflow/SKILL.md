---
name: resume-project-workflow
description: 当用户处理 D:/TestProjects/AiDeveloperResume 的 LaTeX 多岗位简历（评分、润色、岗位定制、导出、抽库整理、重构或本地编译预览），或提及 .temptest、.plan、.preview、tex/data/projects、main_algorithm/backend/frontend/testdevelop、项目库抽库、薄装配层、build.bat 时，应使用本 skill。它固化了用户的协作硬约束（不覆盖根文件、改动只落 .temptest 并按岗分类、方案先放 .plan、用 git 而非 .bak 回退、编译产物只进 .preview），并整合五维评分模型与本简历的 4 点优化方向。通用简历撰写技巧见 skills/resume-coach，与本 skill 互补不重复。
agent_created: true
---

# Resume Project Workflow（本项目专用）

## Overview

本 skill 沉淀自对本仓库 LaTeX 多岗位简历的多次协作，使「评分 → 方案 → 优化 → 校验」流程可复现，并固化用户的协作约定与本地预览硬需求，避免重复踩坑（曾误覆盖根文件、误重构根文件被回退、编译产物污染根目录被严厉批评）。

## When to Use

- 对 `main_algorithm/backend/frontend/testdevelop.tex` 任一变体评分、润色、岗位定制或导出 PDF。
- 抽库整理项目经历，或将简历按岗位重构为薄装配层。
- 本地编译 / 预览 / 产物管理（涉及 `.preview/`、`build.bat`、VS Code 实时预览）。
- 用户提及 `.temptest`、`.plan`、`.preview`、`tex/data/projects`、薄装配层等本仓库专属概念时。

## Hard Collaboration Constraints（编辑/编译前必先核对）

下列规定均源自已发生的回退/翻车教训，每次动手前核对：

1. **绝不原地覆盖根目录 `main_*.tex`。** 用户自管根文件，曾被原地覆盖后回退。
2. **改前先写方案 + 评分到 `.plan/`**，等待用户确认后再执行。既有产物：`plan.md`（方案）、`score.md`（评分报告）、`projects_matrix.md`（项目×岗位矩阵）。
3. **改动/优化版本只输出到 `.temptest/` 并按岗位分类**：`optimized/`（通用优化版）、`algorithm/` `backend/` `frontend/` `testdevelop/`（各岗薄装配层版）。子文件夹编译需把 `tex/` 引用重指向 `../../tex/`。
4. **「抽库归档」与「重构根文件」是两件事，分别确认。** 抽 17 个项目 bullet 进 `tex/data/projects/` 已获批；把根文件改为 `\projectheading`+`\input` 薄装配层未获批、已被回退。除非用户明确说「并入根目录 / 改回去也行」，否则根文件保持原样。
5. **根文件回退用 git，不用 `.bak`。** 用户真实原始版在 `git HEAD`（如标题 `Agent 质量效能`）；`main_*.tex.bak` 可能已是优化版副本，不可靠。回退用 `git checkout HEAD -- <file>`。
6. **编译产物只进 `.preview/`，绝不污染根目录。** 任何编译必须带 `-output-directory=.preview/<模板名>/`，严禁裸跑 `xelatex main_*.tex`；VS Code Build 按钮不可信，用 `build.bat` 或终端。详见「Local Preview & Compile」。

## Project Structure（速查）

```
D:/TestProjects/AiDeveloperResume/
├── main_algorithm.tex    # AI 应用/Agent 岗（求职主线）
├── main_backend.tex      # 后端岗
├── main_frontend.tex     # 前端岗
├── main_testdevelop.tex  # 测试开发岗
├── tex/
│   ├── shared/  preamble.tex（\ResumeTargetRole 等宏）、components.tex（\projectheading）
│   ├── data/
│   │   ├── profile.tex / education.tex   # 模板占位（姓名/邮箱需补真实信息）
│   │   └── projects/  proj_*.tex ×17     # tex 备份：每项目只含 \begin{itemize} 内容体
├── reference/       # 参考素材库（见 reference/README.md）
│   ├── projects/    *.md ×17（按岗分子目录）  # md 文本镜像：README.md 含岗位映射表
│   ├── source/      Project_Experience_list.md / Internship_Experience.md  # 原始素材真相源
│   ├── interview/   qwen_guid_review.md    # 面试复习
│   └── samples/     ai_developer_resume.md / Software_developer_resume.tex  # 参考样例
├── .plan/      # plan.md / score.md / projects_matrix.md
├── .temptest/  # 改动版本（按岗位子文件夹），不入根
└── .preview/   # 编译产物（按模板子文件夹），已 gitignore
```

- 4 套岗位变体：标题与实习 bullet 按岗量身定制（尤其腾讯地图 / 啄木鸟实习），实习**保留在根文件内联**，不强制 DRY。
- 17 个项目已在 `tex/data/projects/` 抽库；根文件现为 `git HEAD` 原始内联版（薄装配层重构未获批）。库文件已可直接 `\input` 复用。
- `profile.tex` / `education.tex` 为占位模板，投递前须填真实姓名/联系方式。

## Optimization Workflow（5 步）

1. **识别意图**：评分 / 润色 / 岗位定制 / 导出 / 抽库整理。信息不足时最小追问。
2. **基线评分**：先按五维模型打分建立基线，列问题清单。
3. **写方案到 `.plan/` + 评分报告**，给 Before→After 与 5 步计划，**等用户确认**。
4. **执行到 `.temptest/`**：不碰根文件；按下方 Compile & Verify 编译校验。
5. **质量回检**：二次评分量化提升（如 78→91），交付并提示下一步。

## Scoring Model（五维）

| 维度 | 权重 | 关注点 |
|---|---|---|
| 内容质量 | 30 | 量化成果、技术深度、岗位相关度、离岗内容精简 |
| 结构与排版 | 25 | 模板干净度、有无 summary、篇幅聚焦、重叠消除 |
| 语言与语法 | 20 | 中英文混排规范（CN-EN spacing）、精炼度、强动词 / bilingual clarity |
| ATS 优化 | 15 | 关键词密度/对齐 JD、标题不误导岗位 |
| 影响力与印象 | 10 | 一眼记忆点、差异化标签 |

- 等级 A+→F；输出须含：总分/等级、五维明细、Top 3 优势、优先级改进项（🔴🟡🟢 + Before→After）、5 步行动计划。
- 实测：优化前 78/B → 优化后 91/A（见 `.plan/score.md`）。
- **本项目场景一律用本五维模型**；通用/其他候选人场景才用 `skills/resume-coach` 的通用评分表，勿混用。

## Four-Point Optimization Direction（Agent 岗锚点，用户给出 / User-provided anchors）

① **篇幅 / Scope & Brevity**：砍「模型微调」偏算法细节（Transformer/自注意力原理删，LoRA/SFT/PPO 一句带过），空间让给 Agent 工程主线；项目保留腾讯地图 Agent 工程 + 医药 RAG 问答两个最贴岗的，其余压缩/移出/作备选（cut algorithm-heavy details; keep only the two most role-relevant projects）。

② **重点 / Positioning**：标题 `AI 应用开发（Agent 质量效能）` 易误读为测试岗 → 改 `Agent 工程`；腾讯实习叙述从「测试提效」转「Agent 工程 / LLM 应用开发」，质量闭环作**产出结果**而非岗位定位（recast the quality loop as an *outcome*, not the job title）。

③ **个人特色 / Differentiation**：顶部加 1–2 行「个人简介」点出 **AI Native 工程习惯**（CodeBuddy/Claude Code 当第一工具、自研多 Agent 编排与评测——2026 届稀缺）+ SCI 在投 + AI 竞赛奖的「研究+落地」标签。中英对照模板见下方「Project-Specific Phrasing」。

④ **技术更新 / Tech Freshness**：已前沿（MCP、Subagent 编排、探索门禁/人工接管护栏、RAGAS、vLLM），无过时技术；Dify/LangChain 已趋标配，**别让框架名抢戏**，强化真正稀缺的可靠性护栏与评测方法论（意图锁定/探索门禁/单步验证/多维自审/人工接管 + 多 Agent 交叉检查/RAGAS/Golden Dataset）。框架名降权、方法论升权（downgrade framework names, upgrade methodology）。

## Project Library Methodology（抽库 + 选岗）

- **库与排版解耦**：每个项目一个 `tex/data/projects/proj_*.tex`，只放 `\begin{itemize}...\end{itemize}` 内容体（不含 `\section`/标题行）。标题行 `\projectheading` 留根变体（不同岗位改角色措辞）。
- **切换岗位 = 改几行 `\input`**，不再翻注释块；同一项目只维护一份，多岗共用。
- **选岗原则**：每岗「2 实习 + 3 项目」封顶，超出靠 `projects_matrix.md` 勾选而非堆进一份源码。
- **备选/被注释项目**：根文件里以「注释掉的 `\input` 桩」保留入口，取消注释即启用。
- 详见 `.plan/projects_matrix.md`（17 项目清单、岗位匹配打分表、勾选法）。

## Reverse-Sync Workflow（反向同步工作流节点，2026-08-23 沉淀）

数据流已明确为「**主稿优先，备份跟随**」，与早期构想的「reference → projects → main」单向流相反：

```
main_*.tex（主稿，唯一编辑入口 / 真相源）
    │  某项目定稿或大幅改写后
    ├─→ tex/data/projects/*.tex   （tex 备份，可 \input 复用）
    └─→ reference/projects/*.md   （md 文本镜像，浏览/检索/复用）
```

- **触发时机**：主稿 `main_*.tex` 中某项目经历定稿 / 大幅改写后，分别同步两处备份，保持三处一致。
- **同步内容**：项目 bullet、量化指标、岗位适配标注（首选/次选）、技术栈。指标改动须与主稿完全一致，不臆造。
- **同步原则**：主稿优先，备份跟随；`reference/projects/*.md` 只是可读镜像，不作为独立编辑入口。
- **边界**：根文件 `main_*.tex` 是用户自管真相源，Agent 不原地覆盖；同步时只改 `tex/data/projects/` 与 `reference/projects/` 两处备份。
- **目录映射**：`reference/projects/` 按岗位分子目录（`ai-application` / `algorithm` / `backend` / `frontend` / `testdevelop`），其 `README.md` 含「项目 → 适配岗位」多对多映射表与「岗位 → 项目」索引。

## Compile & Verify Commands

```bash
# 根变体编译（产物进 .preview/<模板名>，严禁裸跑污染根目录；跑两遍做交叉引用）
xelatex -interaction=nonstopmode -synctex=1 -output-directory=.preview/main_algorithm main_algorithm.tex
xelatex -interaction=nonstopmode -synctex=1 -output-directory=.preview/main_algorithm main_algorithm.tex

# 在 .temptest 子文件夹编译（引用需重指向 ../../tex/）
xelatex -output-directory=.temptest/algorithm -interaction=nonstopmode \
  .temptest/algorithm/main_algorithm.tex

# 路径重指向（用 Python 避免转义坑）
python - <<'PY'
for f in [".temptest/algorithm/main_algorithm.tex",
          ".temptest/backend/main_backend.tex",
          ".temptest/frontend/main_frontend.tex",
          ".temptest/testdevelop/main_testdevelop.tex"]:
    s = open(f, encoding="utf-8").read()
    s = s.replace(r"\input{tex/", r"\input{../../tex/") \
         .replace(r"\includegraphics{tex/", r"\includegraphics{../../tex/")
    open(f, "w", encoding="utf-8").write(s)
PY
```

- **文本等价校验**（重构后证明只搬家没改内容）：分别编译原版与新版 → `pdftotext -layout` 提取 → `diff` 比对（归一化空白）。4 变体曾验证逐字节一致。
- **LaTeX 生成陷阱**：用 heredoc/Python 生成 `.tex` 时，`\vspace` 等可能变成 `0x0B` 控制符致编译失败；生成后用脚本把 `0x0B` 替换为 `backslash-v`。写文件优先用 Write 工具而非 echo/heredoc。
- 仅有来自模板本身的 `\textit` 字体替换警告（非改动），不影响输出。

## Local Preview & Compile（用户硬需求，2026-08-22 沉淀）

凡涉及本地编译 / 预览，必须遵循（用户反复强调，曾因根目录被污染极度不满）：

### 硬约束

- **产物绝不污染根目录**：编译必须带 `-output-directory=.preview/<模板名>/`，严禁裸跑 `xelatex main_*.tex`。
- **产物按模板分类**：`.preview/main_algorithm/`、`main_backend/`、`main_frontend/`、`main_testdevelop/`。
- **VS Code Build 按钮不可信**：`main_*.tex` 首行 `% !TeX program = xelatex` 魔术注释会劫持 recipe，按钮编译会落根目录。优先 `build.bat` 或终端。
- **不做自动清理**：本机无 Perl，`latexmk` 不可用，`autoClean` 须设 `never`。
- **双击 PDF 跳回源码**：用内置 pdf.js 查看器（`Ctrl+Alt+V`），编译须带 `-synctex=1`。

### 最可靠编译方式（用户最终认可）

终端（VS Code 集成终端 / PowerShell / CMD）跑上方 Compile & Verify 里的根变体命令（带 `-output-directory=.preview/<模板名>/`，跑两遍），换模板时把文件名与目录名一起改。

### build.bat（仓库根目录，已提供）

- 双击 / 无参 → 弹菜单选单个模板（默认 1 = `main_algorithm`）。
- `build.bat main_algorithm.tex` → 编译指定模板。
- `build.bat --all` → 一次性编译全部 4 个。
- 产物统一进 `.preview/<模板名>/`；脚本带「找不到 xelatex 补 MiKTeX 路径」兜底。

### VS Code 实时预览（Overleaf 体验）

1. `build.bat` 编译当前在改的模板（稳定，不经过插件 recipe）。
2. VS Code 打开 `main_*.tex`，`Ctrl+Alt+V` 打开 PDF（内置 pdf.js 标签页）。
3. PDF 标签页拖右侧 / `Split Right` → 左源码右 PDF。
4. 改 `.tex` 重编，右侧 PDF 监测文件变化自动刷新。
5. 双击 PDF 跳回 `.tex` 对应行（反向 `Ctrl+Alt+J`）。

`.vscode/settings.json` 要点：`outDir: .preview/%DOC%`、recipe `xelatex-preview`（`-output-directory=.preview/%DOC%` 跑两遍）、`forceRecipeUsage: true`（压魔术注释）、`autoClean.run: never`、`view.pdf.viewer: tab`。⚠️ 但用户实测按钮仍落根目录 → Agent 应**优先推荐终端 / build.bat**，别拍胸脯说「按钮肯定进 preview」。

### 踩坑清单（必须避免）

- `% !TeX program` 魔术注释优先级 > `recipe.default` → 产物落根目录；用 `forceRecipeUsage` 或干脆不用按钮。
- 只双击打开单个 `.tex`（非 `File → Open Folder`）→ `.vscode/settings.json` 不生效 → 按钮退回默认 recipe。
- 本机无 Perl → `latexmk` 命令不可用、`autoClean`（调 `latexmk -c`）必报错。装 Perl：`winget install StrawberryPerl`。
- 裸跑 `xelatex main_*.tex` 必污染根目录。
- `.latexmkrc` 是配置文件非副产物，别删（依赖 Perl 才有用）。
- **行为教训（最重要）**：之前只验证「终端命令能进 preview」就断言「VS Code 配置好了自动进 preview」，没验证 GUI 按钮实际行为，被打脸。→ 涉及 VS Code 插件行为，**不能假设 recipe 一定被采用**；给保证前先验证实际 GUI 路径，或明确说「无法在这边点按钮验证，结论基于插件文档行为」。

### 备选：Docker 跑原版 Overleaf（需先装 Docker，当前未装）

```bash
docker run -d -p 8080:80 -v /d/overleaf_data:/var/lib/overleaf --name overleaf sharelatex/sharelatex
```

浏览器开 `http://localhost:8080` → 注册管理员 → 新建项目导入仓库 → Compiler 设 XeLaTeX。镜像自带 TeX Live + CLSI + MongoDB，1:1 还原 Overleaf（社区版无付费同步）。

## Project-Specific Phrasing（本项目专属英文弹药，可直接抄）

> 通用强动词列表、量化句式、STAR/CAR 改写模式见 `skills/resume-coach` 的 `references/rewrite-patterns.md`；此处只保留绑定本候选人的专属表述。

- **个人简介 / Summary（中英对照，Agent 岗）**：
  - 中文：「AI 应用开发方向，擅长 Agent 编排与 LLM 应用落地；以 CodeBuddy / Claude Code 作为第一开发工具，自建多 Agent 编排与评测体系；SCI 在投 + 多项 AI 竞赛奖，具备研究 + 落地的跨界能力。」
  - English: "AI application developer focused on Agent orchestration and LLM-powered products. AI-native by habit — CodeBuddy / Claude Code as the primary dev tool, with a self-built multi-agent orchestration and evaluation stack. Currently has a SCI paper under review and multiple AI competition awards, bridging research and production."
- **技术栈英文写法 / Tech-stack phrasing**：LLM application development; Agent orchestration; MCP tool integration; Subagent scheduling; reliability guardrails (intent-locking / exploration gating / human-in-the-loop); RAG evaluation (RAGAS / Golden Dataset); model serving (vLLM); backend services (FastAPI); frontend (Vue / React).
- **岗位标题英文 / Role-title phrasing**：`AI 应用开发（Agent 工程）` → "AI Application Developer (Agent Engineering)"; `后端开发` → "Backend Developer"; `前端开发` → "Frontend Developer"; `测试开发` → "Test Development Engineer".

## Relationship with skills/resume-coach（分工边界）

本 skill 是「本项目专属记忆」，`skills/resume-coach` 是「通用简历方法论」，互补不重复：

| 能力 | 归属 | 说明 |
|---|---|---|
| 通用撰写技巧（强动词/量化/STAR-CAR/改写/技能条目） | resume-coach | `references/rewrite-patterns.md` |
| JD 匹配 / ATS / 关键词覆盖 / 缺口分析 | resume-coach | `references/jd-matching.md` |
| 通用简历结构 / 板块权重 / 常见问题 / 中文排版 | resume-coach | `references/programmer-resume-guide*.md` |
| 通用 LaTeX 布局模板 | resume-coach | `references/latex-resume-layout.md` + `assets/latex/` |
| 本项目硬约束 / 结构 / 抽库 / 编译预览 | 本 skill | 唯一归属，resume-coach 不含 |
| 五维评分模型（本项目定制） | 本 skill | 本项目场景用五维，优先于 resume-coach 通用评分表 |
| 4 点优化方向 / 专属英文弹药 | 本 skill | 绑定本候选人，不可复用 |

- 撰写技巧类请求：方法论交 `resume-coach`，本 skill 只负责「落到本项目文件结构的正确位置」。
- 评分口径：本项目场景用本 skill 五维模型；通用/其他候选人场景用 resume-coach 评审模式，勿混用。

## Scope & Location

- 本 skill 位于 `skills/resume-project-workflow/`，非 CodeBuddy 默认自动发现路径（默认扫描 `.codebuddy/skills/`）。若需自动加载，可将副本/软链放入 `.codebuddy/skills/`。
- 与 `skills/resume-coach`（通用）及会话内简历优化专家互补；撰写方法论以 resume-coach 为准，本项目约束以本 skill 为准。

## Quick Reference（速记）

> 评分进 `.plan/` → 方案等确认 → 改动只落 `.temptest/`（按岗分类）→ 编译只进 `.preview/`（按模板分类）→ xelatex 校验 + 文本等价比对 → **根文件只动于用户明确批准**。通用撰写技巧 → `skills/resume-coach`。
