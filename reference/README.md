# 参考素材库（reference）

本目录存放简历撰写所需的各类参考素材，已按职责归档为子目录：

## 目录结构

```
reference/
├── projects/           # 结构化项目库（按岗位分类，一项目一 md）
│   ├── README.md       # 项目 → 岗位 多对多映射表 + 岗位索引 + 二选一提示
│   ├── ai-application/  algorithm/  backend/  frontend/  testdevelop/
├── source/             # 原始素材真相源（按人分组，未提炼）
│   ├── Project_Experience_list.md   # 项目经历素材（LI/He/Chen/Hu/Mou/Tan）
│   └── Internship_Experience.md     # 实习经历素材（按人分组）
├── interview/          # 面试复习
│   └── qwen_guid_review.md          # 素材筛选 + 技术口径校验 + 复盘卡片 + 速查
├── samples/            # 参考样例（非本人内容）
│   ├── ai_developer_resume.md       # 李鱼皮 AI/后端简历样例（外部参考）
│   └── Software_developer_resume.tex# 英文软件工程简历模板
└── testdevelop/        # 测试开发方向简历文案草稿（3 个版本）
```

## 各子目录职责

| 目录 | 职责 | 是否直接进简历 |
| --- | --- | --- |
| `projects/` | **提炼后的岗位化镜像**，写简历时直接挑选的「成品零件」，每项目含岗位适配标注 | 是（经 `\input` 或手动搬进 `main_*.tex`） |
| `source/` | **未提炼的真相源**，保留按人分组的原始事实（谁做了什么、多个候选版本、指标口径） | 否，是 `projects/` 与 `main_*.tex` 的事实依据 |
| `interview/` | **面试准备材料**，用于素材筛选、技术口径校验和面试前复习 | 否 |
| `samples/` | **他人简历样例/模板**，写作参考用，非本人内容 | 否，勿直接复用 |
| `testdevelop/` | 测开方向简历文案草稿（v1 业务测试导向 / v2 测试开发导向 / v3 AI 测试导向） | 按需 |

## 数据流

```
source/（原始真相源）
   │  人工/AI 提炼
   ▼
projects/（岗位化镜像）  +  main_*.tex（主稿，唯一编辑入口）
```

- 原始事实在 `source/`，提炼结果在 `projects/`，面试准备看 `interview/`，写作参考看 `samples/`。
- `projects/` 是 `source/` 的提炼产物；两者职责不同，`source/` 保留「谁做的」维度与多个候选版本，`projects/` 只保留岗位化定稿 bullet。
