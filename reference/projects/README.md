# 项目库（Project Bank）

本目录是 `tex/data/projects/*.tex` 的 **Markdown 文本镜像**，用于浏览、检索与跨岗位复用。每个项目一个独立 md，按「首选岗位」归类到子目录：

```
reference/projects/
├── README.md            # 本文件：多对多岗位映射 + 岗位索引 + 投递提示
├── ai-application/      # 7 个：AI 应用开发 / 多模态 / RAG / Agent
├── algorithm/           # 2 个：CV 多模态 / 机器学习
├── backend/             # 3 个：Java 微服务 / 高并发 / 小程序
├── frontend/            # 3 个：Vue3 / AI 产品前端 / Django 全栈
└── testdevelop/         # 2 个：测开平台 / AI 智能体测开
```

## 数据流向（单一真相源在主稿）

```
main_*.tex（主稿，唯一编辑入口）
    │  定稿后同步
    ├─→ tex/data/projects/*.tex   （tex 备份，可 \input 复用）
    └─→ reference/projects/*.md   （md 文本镜像，本目录）
```

> 原则：**主稿优先，备份跟随**。改项目内容直接在主稿里改，改完后同步两处备份；本目录只是可读镜像，不作为独立编辑入口。

## 表 A：项目 → 适配岗位（多对多）

> 一个项目可适配多个岗位；「首选」为最契合方向，「次选」为可投递方向。

| 项目 | 首选岗位 | 次选岗位 |
| --- | --- | --- |
| [LLM Agent 质量效能工程](ai-application/agent_qa.md) | 测开、AI 应用开发 / AI Agent | AI 工程、后端（AI Agent 经验） |
| [基于 RAG 的医药数据分析问答助手](ai-application/medical_rag.md) | AI 应用开发、算法（NLP） | 后端（RAG / Text-to-SQL）、数据分析 |
| [多模态家电识别与知识库入库系统](ai-application/homeappliance.md) | AI 应用开发、多模态 | 后端（服务封装 / vLLM）、算法（多模态） |
| [汽车配件表格问答系统](ai-application/autoparts_sql.md) | 算法（LLM 微调 / RL）、AI 应用开发 | NLP 算法、大模型应用工程师 |
| [智能填表系统](ai-application/form_fill.md) | AI 应用开发 / RAG、算法（检索） | 后端（RAG / 向量检索） |
| [空气质量分析报告生成平台](ai-application/air_quality.md) | AI 应用开发、算法（NLP / 数据） | 数据平台、数据分析 |
| [多模态智能导盲车](ai-application/guide_car.md) | AI 应用开发 / 多模态 Agent、算法（多模态） | 机器人 / 嵌入式 AI（ROS） |
| [视频内容分析与语义理解](algorithm/video_understanding.md) | 算法（CV / 多模态） | AI 应用开发（模型侧） |
| [催收策略效果评估](algorithm/collection_ml.md) | 算法（ML / 风控） | 数据分析、数据平台 |
| [小麦购票](backend/wheat_ticket.md) | 后端、全栈 | 后端 + AI 应用研发 |
| [天天购物平台](backend/daily_shop.md) | 后端、全栈 | 后端 + AI 应用研发 |
| [实时订单系统](backend/realtime_order.md) | 后端、全栈（小程序） | 后端 + AI 应用研发 |
| [云端智能图像协同系统](frontend/cloud_image.md) | 前端、全栈 | AI 产品前端 |
| [智能应用生成平台](frontend/ai_app_gen.md) | 前端、AI 产品前端 / 全栈 | AI 应用开发（交互侧） |
| [校园二手交易平台](frontend/campus_secondhand.md) | 前端 / 全栈（Django） | Web 应用开发 |
| [智能持续测试平台](testdevelop/continuous_test.md) | 测开 | 后端（自动化）、全栈（工程化） |
| [手机地图 UI 自动化平台](testdevelop/map_ui_auto.md) | 测开、AI 应用开发 / Agent | AI 工程 |

## 表 B：岗位 → 可用项目清单

| 岗位 | 首选项目 | 次选项目 |
| --- | --- | --- |
| **AI 应用开发** | agent_qa、medical_rag、homeappliance、form_fill、air_quality、guide_car | autoparts_sql、map_ui_auto、video_understanding、ai_app_gen |
| **算法** | video_understanding、collection_ml、autoparts_sql | medical_rag、form_fill、air_quality、guide_car、homeappliance |
| **后端** | wheat_ticket、daily_shop、realtime_order | homeappliance、medical_rag、form_fill、continuous_test |
| **前端** | cloud_image、ai_app_gen、campus_secondhand | — |
| **全栈** | wheat_ticket、daily_shop、cloud_image、ai_app_gen | realtime_order、campus_secondhand、continuous_test |
| **测开** | continuous_test、map_ui_auto、agent_qa | — |

## 同质项目「二选一」提示

投递时避免内容重复，以下项目建议二选一：

| 组 | 项目 | 说明 |
| --- | --- | --- |
| 后端高并发 | `wheat_ticket` vs `daily_shop` | 均含 Redis 库存扣减 + 消息队列解耦，技术同质；`wheat_ticket` 指标更全，`daily_shop` 微服务治理更完整 |
| 测开智能体 | `agent_qa` vs `map_ui_auto` | 同一套 CodeBuddy 体系，内容高度同源；投测开岗优先 `map_ui_auto`（更深入），投 AI 应用岗优先 `agent_qa` |
| 后端入门 | `realtime_order` | 技术深度较浅，仅作补充「实时通信（WebSocket）」能力点或初级岗备选 |

## 注意事项

- 每个 md 顶部的「岗位适配」与「时间 / 角色 / 技术栈」来自 `tex/data/projects/*.tex` 的注释块及 `main_*.tex` 的标题行；标注「待确认」处需本人核对。
- 本目录与 `reference/source/Project_Experience_list.md`（按人分组的原始素材）职责不同：后者是**未提炼的真相源**，本目录是**提炼后的岗位化镜像**。
- 若项目内容在 `main_*.tex` 中发生改动，请同步更新本目录对应 md 与 `tex/data/projects/*.tex`，保持三处一致。
