# resume-coach

面向中文 / 英文软件求职场景的 AI Agent 简历技能（skill）：简历撰写、评估打分、JD 匹配与定制、bullet 改写、以及 LaTeX/XeLaTeX 排版。

- 入口：`SKILL.md`
- 参考资料：`references/`（程序员简历指南、JD 匹配、改写模式、LaTeX 排版规则）
- 排版模板：`assets/latex/compact-ai-resume-template.tex`
- 可选 agent 配置：`agents/openai.yaml`

兼容 CodeBuddy、Claude Code 及 `npx skills`（Vercel）等以 `SKILL.md` 为识别标准的工具。

## 安装

### 方式一：npx（发布到 npm 后）

```bash
# 装到 CodeBuddy 用户级目录（默认，跨项目可用）
npx resume-coach-skill

# 装到当前项目级
npx resume-coach-skill --target codebuddy:project

# 装到 Claude Code
npx resume-coach-skill --target claude
```

### 方式二：本地脚本（无需发布，直接跑）

```bash
node bin/install.js --target codebuddy           # 用户级 CodeBuddy（~/.codebuddy/skills/）
node bin/install.js --target codebuddy:project   # 项目级 CodeBuddy（.codebuddy/skills/）
node bin/install.js --target claude              # Claude Code（~/.claude/skills/）
node bin/install.js --target agents --symlink    # 通用目录（~/.agents/skills/）+ 软链（开发模式）
node bin/install.js --dir /path/to/skills        # 任意目录
```

### 方式三：npm scripts

```bash
npm run install:codebuddy
npm run install:codebuddy:project
npm run install:claude
npm run install:agents
```

### 方式四：手动挂载

把整个目录复制或软链到目标工具的 skills 目录：

- CodeBuddy 项目级：`.codebuddy/skills/resume-coach/`
- CodeBuddy 用户级：`~/.codebuddy/skills/resume-coach/`
- Claude Code：`~/.claude/skills/resume-coach/`

安装后重启 / 刷新会话，工具会按 `SKILL.md` 的 `description` 在相关任务中自动触发。

## CLI 参数

| 参数 | 说明 |
|---|---|
| `--target <name>` | `codebuddy`（默认）/ `codebuddy:project` / `claude` / `agents` |
| `--dir <path>` | 安装到指定目录 |
| `--symlink` | 软链而非复制（开发模式，改源自动生效） |
| `--force` | 覆盖已有安装 |
| `--help` | 显示帮助 |

## 发布

```bash
npm login
npm publish
```

本地调试可先 `npm link`，再到任意目录执行 `npx resume-coach-skill` 验证。

> 也可直接作为独立 git 仓库发布，配合 `npx skills add <user>/<repo>` 安装（Vercel skills 工具，无需 `package.json`）。
