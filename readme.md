# AiDeveloperResume

一套面向中文软件求职场景的 LaTeX 简历模板与简历优化资料库。仓库包含算法/AI 应用、Java 后端、前端开发、测试开发等岗位方向模板，也包含一个可用于简历撰写、评估、JD 匹配和 LaTeX 排版的 `resume-coach` skill 草稿。

![CV preview](./docs/CV-preview.jpg)

## 快速开始

本项目使用 XeLaTeX 编译中文简历，字体文件已内置在 `fonts/` 目录。

```powershell
# 编译算法 / AI 应用方向模板
xelatex main_algorithm.tex

# 如果安装了 latexmk，也可以直接使用仓库内的 .latexmkrc
latexmk main_algorithm.tex
```

在 Overleaf 中使用时，请打开左上角 `Menu`，把 `Compiler` 设置为 `XeLaTeX`。如果日志第一行出现 `This is pdfTeX` 或 `preloaded format=pdflatex`，说明仍在使用 pdfLaTeX，中文字体宏包会直接报错。

可替换 `main_algorithm.tex` 为其他岗位模板：

| 文件 | 适用方向 |
| --- | --- |
| `main_algorithm.tex` | 算法工程师、AI 应用开发、大模型/RAG/Agent 相关岗位 |
| `main_backend.tex` | Java 后端开发、后端 + AI 应用研发 |
| `main_frontend.tex` | 前端开发、AI 产品前端、Web 应用开发 |
| `main_testdevelop.tex` | 测试开发、AI 应用测试与交付 |

批量编译全部模板：

```powershell
Get-ChildItem main_*.tex | ForEach-Object { latexmk $_.Name }
```

## 环境要求

- TeX Live、MiKTeX 或 TinyTeX
- XeLaTeX
- 常用宏包：`fontspec`、`xeCJK`、`fontawesome5`、`titlesec`、`enumitem`、`tikz`、`hyperref`
- 可选工具：`latexmk`。在 Windows + MiKTeX 环境中，`latexmk` 可能还需要 Perl；如果未安装 Perl，请直接使用 `xelatex` 命令编译。
- 或者直接`Overleaf`解决

如果 `fontawesome5` 缺失，请用你的 TeX 发行版包管理器安装；MiKTeX 通常可以在首次编译时自动安装缺失宏包。

## 项目结构

```text
.
├── main_algorithm.tex              # 算法 / AI 应用方向简历模板
├── main_backend.tex                # Java 后端方向简历模板
├── main_frontend.tex               # 前端方向简历模板
├── main_testdevelop.tex            # 测试开发方向简历模板
├── .latexmkrc                      # latexmk 默认使用 XeLaTeX
├── docs/
│   └── CV-preview.jpg              # 简历预览图
├── fonts/                          # 内置 Noto Serif SC 字体
├── images/                         # 页眉、照片、校徽等图片素材
├── tex/
│   ├── shared/
│   │   ├── preamble.tex            # 宏包、字体、颜色、页面和通用命令
│   │   └── components.tex          # 联系栏、个人信息和教育背景渲染组件
│   └── data/
│       ├── profile.tex             # 姓名、邮箱、电话、学校、照片等通用信息
│       └── education.tex           # 通用教育背景
├── reference/                      # 简历素材、项目经历、复盘与参考模板
└── skill-staging/
    └── resume-coach/               # 简历撰写与优化评估 skill 草稿
```

## 如何改成自己的简历

1. 选择最接近目标岗位的 `main_*.tex`。
2. 修改 `tex/data/profile.tex` 中的姓名、邮箱、电话、GitHub、学校和照片路径。
3. 修改 `tex/data/education.tex` 中的教育背景。
4. 在对应 `main_*.tex` 中修改 `\ResumeTargetRole`、专业技能、实习经历、项目经历和成果奖项。
5. 替换 `images/xjpic.jpg` 为自己的照片，或在 `tex/data/profile.tex` 中改成新的照片路径。
6. 编译并检查 PDF：中文换行、日期格式、技术名词大小写、链接是否可点击。

写入正式简历前，请确认所有项目指标、获奖、论文、上线情况和链接都能经得起面试追问。本仓库中的素材强调“真实事实 + 清晰表达”，不建议虚构经历或不可验证的量化结果。

## 参考素材

`reference/` 中的文件用于整理简历内容，不一定都适合直接放进最终简历：

- `Project_Experience_list.md`：项目经历素材清单
- `Internship_Experience.md`：实习经历素材清单
- `ai_developer_resume.md`：AI/后端方向简历样例素材
- `Software_developer_resume.tex`：英文软件工程简历参考模板
- `qwen_guid_review.md`：大模型相关简历素材、技术口径和面试复盘

建议把 `reference/` 当作候选素材库：先筛选与目标 JD 相关的事实，再压缩进对应岗位模板。

## Resume Coach Skill

`skill-staging/resume-coach/` 是一个用于 AI Agent 的简历优化 skill 草稿，包含：

- `SKILL.md`：skill 入口说明和工作流
- `references/`：程序员简历指南、JD 匹配、改写模式、LaTeX 排版规则
- `assets/latex/compact-ai-resume-template.tex`：可复用的紧凑型中文 AI/软件岗简历模板
- `agents/openai.yaml`：可选 agent 配置示例

在支持 skills 的环境中，可以把 `skill-staging/resume-coach/` 安装或复制为 `resume-coach` skill 后使用。示例需求：

```text
请使用 resume-coach 评估 main_backend.tex 是否匹配 Java 后端实习岗位。
请根据这份 JD 调整 main_algorithm.tex，保留真实事实，不新增未经确认的指标。
请把 Project_Experience_list.md 中的项目压缩成一页中文简历项目经历。
```

## 编译排错

- 请使用 `xelatex`，不要用默认 `pdflatex` 编译中文模板。
- 如果提示找不到字体，确认 `fonts/NotoSerifSC.otf` 和 `fonts/NotoSerifSC-Bold.otf` 存在。
- 如果提示找不到图片，确认 `images/foot.png`、`images/xjpic.jpg` 等资源存在，或同步修改 `tex/data/profile.tex` 中的图片路径。
- 如果 PDF 生成但排版溢出，优先压缩项目经历、技能条目和荣誉奖项，而不是继续缩小字号。

清理编译产物：

```powershell
latexmk -C main_algorithm.tex
```

## 开源发布说明

- 本仓库已忽略 LaTeX 编译产物、本地 MiKTeX 缓存和私有备份目录。
- 对外发布前，请检查模板中的姓名、电话、邮箱、照片、学校、公司和项目指标是否适合公开。
- 本仓库当前尚未包含 `LICENSE` 文件；正式开源前请由维护者选择许可证并加入仓库。

## 致谢

版式最初参考了 SEU 中文 CV 模板和 NPU 中文 CV 模板，并在中文程序员简历场景下进行了岗位化改造。
