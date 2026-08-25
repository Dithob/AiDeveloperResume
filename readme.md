# AiDeveloperResume

一套面向中文软件求职场景的 LaTeX 简历模板与简历优化资料库。仓库包含算法/AI 应用、Java 后端、前端开发、测试开发等岗位方向模板，并配套两个 AI Agent skill：`resume-coach`（通用简历撰写/评估/JD 匹配/LaTeX 排版方法论）与 `resume-project-workflow`（本项目专属的评分模型、优化方向与协作约束）。

![CV preview](./docs/CV-preview.jpg)

## 快速开始

本项目使用 XeLaTeX 编译中文简历，字体文件已内置在 `fonts/` 目录。

### 第 0 步：初始化本地数据文件（首次克隆必做）

`tex/data/profile.tex` 和 `tex/data/education.tex` 包含姓名、电话等真实个人信息，已被 `.gitignore` 忽略，仓库只提供 `*.example` 脱敏模板。首次克隆后必须先复制，否则编译时 `\input{tex/data/profile}` 会直接报错：

macOS / Linux（zsh、bash）：

```bash
cp tex/data/profile.tex.example tex/data/profile.tex
cp tex/data/education.tex.example tex/data/education.tex
```

Windows（PowerShell）：

```powershell
Copy-Item tex/data/profile.tex.example tex/data/profile.tex
Copy-Item tex/data/education.tex.example tex/data/education.tex
```

### 第 1 步：编译

**必须在仓库根目录执行**——模板通过相对路径 `fonts/` 加载内置字体。统一使用仓库脚本，避免把 `.pdf`、`.aux`、`.log` 和 `.synctex.gz` 污染到根目录；产物会按模板写入 `.preview/<模板名>/` 或 `.output/<模板名>/`，日志和 SyncTeX 文件会保留。

脚本需要 Python 3 和 XeLaTeX：

```bash
# macOS / Linux：停止输入后快速预览（单遍，适合日常编辑）
./build.sh preview main_algorithm.tex

# 发布编译（双遍，适合投递前确认）
./build.sh release main_algorithm.tex

# 批量发布编译四个模板
python3 scripts/build.py release --all
```

Windows 使用同一套 Python 编译逻辑：

```powershell
build.bat preview main_algorithm.tex
build.bat release main_algorithm.tex
build.bat release --all
```

旧命令 `build.bat main_algorithm.tex` 仍兼容，默认执行 `release`。四个主稿可替换为：

| 文件 | 适用方向 |
| --- | --- |
| `main_algorithm.tex` | 算法工程师、AI 应用开发、大模型/RAG/Agent 相关岗位 |
| `main_backend.tex` | Java 后端开发、后端 + AI 应用研发 |
| `main_frontend.tex` | 前端开发、AI 产品前端、Web 应用开发 |
| `main_testdevelop.tex` | 测试开发、AI 应用测试与交付 |

`preview` 只启动一遍 XeLaTeX，服务于热更新；`release` 启动两遍 XeLaTeX，服务于最终发布。脚本限制目标文件白名单，固定仓库根目录执行，并使用 `-synctex=1`、`-file-line-error` 与 `-no-shell-escape`。

## 本地编译方案

本地环境安装以下方案二选一，安装完成后回到「快速开始」执行编译。

### macOS

**方案一：MacTeX（推荐，一步到位）**

包含全部常用宏包（约 5 GB），安装后无需再补装任何依赖：

```bash
brew install --cask mactex
```

也可以到 [tug.org/mactex](https://www.tug.org/mactex/) 下载 pkg 安装包。安装完成后重启终端，执行 `xelatex --version` 验证。

**方案二：BasicTeX（轻量，约 100 MB，按需补装宏包）**

```bash
brew install --cask basictex

# BasicTeX 默认不带以下宏包，需手动补装
sudo tlmgr install fontawesome5 xecjk titlesec enumitem pgf fancybox environ trimspaces
```

编译时如果提示缺某个宏包（如 `fontawesome5.sty not found`），按报错提示执行 `sudo tlmgr install <宏包名>` 即可。

### Windows

**方案一：MiKTeX（推荐，缺失宏包自动安装）**

```powershell
winget install MiKTeX.MiKTeX
```

也可以到 [miktex.org](https://miktex.org/download) 下载安装器。安装后打开 `MiKTeX Console` → `Settings`，把 `Missing package installation` 设为 `Always`，首次编译时会自动安装 `fontawesome5` 等缺失宏包。

**方案二：TeX Live（全量安装）**

到 [tug.org/texlive](https://www.tug.org/texlive/) 下载安装器，包含全部宏包，安装耗时较长但后续无需补装。

Windows 还需要 Python 3；安装后可用 `py -3 --version` 检查。日常预览和发布请使用 `build.bat`，不需要额外安装 Perl。

### 编辑器集成（可选）

#### VS Code + LaTeX Workshop 实时预览（推荐）

本项目已在 `.vscode/settings.json` 中预置“左侧源码、右侧 PDF”的编辑体验：编辑停止约 800ms 后自动触发单遍 XeLaTeX，PDF 标签页自动刷新，预览产物进入 `.preview/<模板名>/`。

使用方法：

1. 用 `File → Open Folder` 打开整个仓库，不要只打开单个 `.tex` 文件。
2. 安装 **LaTeX Workshop**，打开任意 `main_*.tex`。
3. 按 `Ctrl+Alt+V` 打开 PDF，将 PDF 标签页拖到右侧或执行 `Split Right`。
4. 修改源码后等待自动编译；也可以运行 `build.bat preview main_algorithm.tex` 或 `./build.sh preview main_algorithm.tex`。

LaTeX 源码启用了编辑器显示层的视觉软换行：`wordWrap: bounded`、缩进换行和 100/120 列标尺。软换行不会写入真实换行符，不改变源码行号、Git diff、PDF 排版或 SyncTeX 映射；同时已关闭保存/粘贴格式化。停止输入后的热更新目标是 3 秒以内，首次 TeX 冷启动和字体缓存耗时需单独记录。

> `.vscode/settings.json` 使用 `latex-workshop.latex.build.forceRecipeUsage: true`，并保留 `-synctex=1`、`-file-line-error` 和 `-no-shell-escape`。如果插件行为异常，优先运行仓库脚本；脚本和插件都不会把产物写入根目录。

#### PDF 与源码双向定位

- 源码到 PDF：在源码中执行 LaTeX Workshop 的 `SyncTeX from cursor`，或使用对应的正向搜索命令。
- PDF 到源码：在内置 PDF 预览中双击目标位置，或执行 `Ctrl+Alt+J`，跳回真实 `.tex` 行。
- 视觉软换行产生的显示折行不是实际源码行，因此反向定位以文件真实行号为准。
- `.preview/<模板名>/` 中保留 `.synctex.gz` 和 `.log`；编译失败时先查看日志，再定位源文件。

#### 只在终端里手动编译

```bash
./build.sh preview main_algorithm.tex   # 单遍快速预览
./build.sh release main_algorithm.tex   # 双遍发布编译
./build.sh release --all                # 四模板批量编译
```

Windows 将 `./build.sh` 替换为 `build.bat`。脚本不接受任意路径，只允许四个白名单主稿，并固定从仓库根目录运行。

### 发布到 Overleaf（显式副本）

本地四个 `main_*.tex` 是唯一编辑入口；Overleaf 只接收明确生成的发布副本，不与本地同时维护第二份主稿。`scripts/overleaf_publish.py` 默认只做准备或 ZIP，不会自动提交、推送，也不会把 GitHub `origin` 当作 Overleaf 远程。

#### 有 Overleaf Git Integration 时

隔离镜像目录为 `.overleaf-sync/repo/`，其远程别名固定为 `overleaf`：

```bash
# 首次使用：把 Integrations → Git 中的地址放入隔离镜像
python3 scripts/overleaf_publish.py --init "<OVERLEAF_GIT_URL>"

# 先查看白名单文件和镜像差异，不推送
python3 scripts/overleaf_publish.py --include-private

# 确认后才提交并推送；个人信息必须显式允许
python3 scripts/overleaf_publish.py --include-private --push \
  --message "publish resume templates"
```

脚本会检查远程是否领先本地、只允许 `main`/`master`、拒绝强制推送，并在镜像存在未知文件变更时停止。远程领先时应先人工在 Overleaf 检查，再在镜像中处理冲突；不要从 Overleaf 反向覆盖本地主稿。访问令牌不应写入脚本、仓库或日志。

#### 没有 Git Integration 时：生成 ZIP

免费账号或没有 Git Integration 时，直接生成白名单 ZIP，不需要初始化镜像：

```bash
python3 scripts/overleaf_publish.py --include-private \
  --zip .overleaf-sync/resume-upload.zip
```

将 ZIP 手动上传到 Overleaf 后，在 `Menu → Compiler` 选择 `XeLaTeX`。`--include-private` 会把本地 `profile.tex`、`education.tex` 和实际使用的个人照片放进被忽略的隔离目录或临时 ZIP；默认不读取这些文件。上传前请检查 ZIP 清单，上传后也应确认项目权限、共享链接和评论内容没有暴露不必要的个人信息。

## 环境要求

- Python 3（用于 `scripts/build.py` 和 `scripts/overleaf_publish.py`）
- TeX 发行版（任选其一）：
  - macOS：MacTeX（推荐）或 BasicTeX + `tlmgr` 补装宏包
  - Windows：MiKTeX（推荐）或 TeX Live
- XeLaTeX 引擎
- 常用宏包：`fontspec`、`xeCJK`、`fontawesome5`、`titlesec`、`enumitem`、`tikz`、`hyperref`、`fancybox`、`geometry`
- `latexmk` 仅作为历史兼容工具，不是本项目预览或发布流程的必需依赖；统一入口不会依赖 Perl。

如果 `fontawesome5` 缺失，请用你的 TeX 发行版包管理器安装：macOS 执行 `sudo tlmgr install fontawesome5`，Windows 在 MiKTeX Console 中安装或开启自动安装。

## 项目结构

```text
.
├── main_algorithm.tex              # 算法 / AI 应用方向简历模板
├── main_backend.tex                # Java 后端方向简历模板
├── main_frontend.tex               # 前端方向简历模板
├── main_testdevelop.tex            # 测试开发方向简历模板
├── .vscode/settings.json           # 视觉软换行、LaTeX Workshop 自动预览与 SyncTeX
├── build.bat / build.sh            # Windows 与 macOS/Linux 入口
├── scripts/build.py                # 统一 preview/release/--all 编译逻辑
├── scripts/overleaf_publish.py     # 隔离 Overleaf 发布或白名单 ZIP
├── .preview/                       # 快速预览输出（git 忽略）
├── .output/                        # 发布输出（git 忽略）
├── .overleaf-sync/                 # 隔离镜像与 ZIP（git 忽略）
├── .latexmkrc                      # 历史兼容配置，不是默认入口
├── docs/
│   └── CV-preview.jpg              # 简历预览图
├── fonts/                          # 内置 Noto Serif SC 字体
├── images/                         # 页眉、照片、校徽等图片素材
├── tex/
│   ├── shared/
│   │   ├── preamble.tex            # 宏包、字体、颜色、页面和通用命令
│   │   └── components.tex          # 联系栏、个人信息和教育背景渲染组件
│   └── data/
│       ├── profile.tex.example    # 姓名、邮箱、电话、学校、照片等（脱敏模板，复制为 profile.tex 使用）
│       └── education.tex.example  # 通用教育背景（脱敏模板，复制为 education.tex 使用）
├── reference/                      # 简历素材、项目经历、复盘与参考模板
└── skills/                         # AI Agent skill（详见「Skills」章节）
    ├── resume-coach/               # 通用简历撰写/评估/JD 匹配/LaTeX 排版
    └── resume-project-workflow/    # 本项目专属：评分模型、优化方向、协作约束与编译预览
```

## 如何改成自己的简历

1. 选择最接近目标岗位的 `main_*.tex`。
2. 修改 `tex/data/profile.tex` 中的姓名、邮箱、电话、GitHub、学校和照片路径。
3. 修改 `tex/data/education.tex` 中的教育背景。
4. 在对应 `main_*.tex` 中修改 `\ResumeTargetRole`、专业技能、实习经历、项目经历和成果奖项。
5. 将自己的照片放在本地 `images/`，并在 `tex/data/profile.tex` 中修改 `\ResumePhoto` 路径；`profile.tex` 和个人照片不会提交到 Git。
6. 编译并检查 PDF：中文换行、日期格式、技术名词大小写、链接是否可点击。

写入正式简历前，请确认所有项目指标、获奖、论文、上线情况和链接都能经得起面试追问。本仓库中的素材强调“真实事实 + 清晰表达”，不建议虚构经历或不可验证的量化结果。

## 参考素材

`reference/` 中的文件用于整理简历内容，不一定都适合直接放进最终简历，已按职责归档为子目录：

- `source/`：原始素材真相源（按人分组）
  - `Project_Experience_list.md`：项目经历素材清单
  - `Internship_Experience.md`：实习经历素材清单
- `interview/`：面试复习
  - `qwen_guid_review.md`：大模型简历素材、技术口径和面试复盘
- `samples/`：参考样例
  - `ai_developer_resume.md`：AI/后端方向简历样例（外部参考，非本人）
  - `Software_developer_resume.tex`：英文软件工程简历参考模板
- `projects/`：结构化项目库（按岗位分类，见 `projects/README.md`）

建议把 `reference/` 当作候选素材库：先筛选与目标 JD 相关的事实，再压缩进对应岗位模板。

## Skills（AI Agent 技能）

`skills/` 目录下提供两个配套简历工作流的 AI Agent skill：

### resume-coach（通用简历方法论）

`skills/resume-coach/` 是通用的简历撰写、评估、JD 匹配与 LaTeX 排版 skill，可复用于任意候选人/岗位：

- `SKILL.md`：skill 入口说明和工作流
- `references/`：程序员简历指南、JD 匹配、改写模式、LaTeX 排版规则
- `assets/latex/compact-ai-resume-template.tex`：可复用的紧凑型中文 AI/软件岗简历模板
- `agents/openai.yaml`：可选 agent 配置示例

#### 安装（详见 [skills/resume-coach/README.md](skills/resume-coach/README.md)）

`resume-coach` 已封装为标准 npm 包，可通过 npx 安装；也可手动挂载到本项目的 CodeBuddy：

```powershell
# 方式一：安装脚本（挂到项目级 .codebuddy/skills/）
node skills/resume-coach/bin/install.js --target codebuddy:project

# 方式二：软链（改源自动生效，开发推荐）
New-Item -ItemType Directory -Force .codebuddy/skills | Out-Null
New-Item -ItemType Junction -Path .codebuddy/skills/resume-coach -Target (Resolve-Path skills/resume-coach)
```

### resume-project-workflow（本项目专属工作流）

`skills/resume-project-workflow/` 沉淀自对本仓库的多次协作，固化本项目专属的约束与优化方向：

- 协作硬约束：不覆盖根文件、改动只落 `.temptest/`、方案先放 `.plan/`、git 回退、编译产物只进 `.preview/`
- 五维评分模型 + 4 点优化方向（Agent 岗锚点）
- 项目抽库方法论与本地编译预览工作流

挂载到本项目 CodeBuddy（软链，改源自动生效）：

```powershell
New-Item -ItemType Directory -Force .codebuddy/skills | Out-Null
New-Item -ItemType Junction -Path .codebuddy/skills/resume-project-workflow -Target (Resolve-Path skills/resume-project-workflow)
```

> 挂载后重启/刷新会话，`/skills` 面板即可看到，任务匹配 `description` 时自动触发。`.codebuddy/` 已被 `.gitignore` 忽略，克隆后需重新挂载（或将该目录例外进版本管理）。

示例需求：

```text
请使用 resume-coach 评估 main_backend.tex 是否匹配 Java 后端实习岗位。
请根据这份 JD 调整 main_algorithm.tex，保留真实事实，不新增未经确认的指标。
请把 source/Project_Experience_list.md 中的项目压缩成一页中文简历项目经历。
请对 main_algorithm.tex 做五维评分，并按 4 点优化方向给出 Before→After 方案。
```

## 编译排错

- 请使用仓库的 `build.sh`/`build.bat` 或 `scripts/build.py`，不要直接裸跑 `xelatex main_*.tex`；中文模板不能使用默认 `pdflatex`。
- 报错 `tex/data/profile.tex not found`：首次克隆未执行「第 0 步」，先复制 `*.example` 文件。
- 报错找不到 `fonts/NotoSerifSC.otf` 或 `images/foot.png`：脚本会在编译前提示缺失文件，请确认当前命令从仓库根目录执行。
- 提示 `fontawesome5.sty not found` 等宏包缺失：macOS 执行 `sudo tlmgr install <宏包名>`；Windows 在 MiKTeX Console 中安装，或开启缺包自动安装。
- 如果提示找不到照片，检查 `tex/data/profile.tex` 中的 `\ResumePhoto` 路径；个人照片属于本地私有文件，不要提交到 Git。
- 如果停止输入后热更新超过 3 秒，分别记录首次编译和后续热更新耗时，先确认是否为 TeX 冷启动或字体缓存，不要删除 SyncTeX、日志或错误检查参数来换取速度。
- 如果 PDF 生成但排版溢出，优先压缩项目经历、技能条目和荣誉奖项，而不是继续缩小字号。

清理编译产物（均已被 `.gitignore` 忽略）：

```bash
rm -rf .preview .output       # 删除预览和发布输出
```

## 开源发布说明

- 本仓库已忽略 LaTeX 编译产物、本地 MiKTeX 缓存和私有备份目录。
- 对外发布前，请检查模板中的姓名、电话、邮箱、照片、学校、公司和项目指标是否适合公开。
- 本仓库当前尚未包含 `LICENSE` 文件；正式开源前请由维护者选择许可证并加入仓库。

## 致谢

版式最初参考了 SEU 中文 CV 模板和 NPU 中文 CV 模板，并在中文程序员简历场景下进行了岗位化改造。
