# LLM Agent 质量效能工程（腾讯地图）

> 岗位适配：**首选** 测试开发（测开）、AI 应用开发 / AI Agent 开发；**次选** AI 工程 / LLM 应用工程、后端（具备 AI Agent 工程经验）

> 理由：核心是「LLM Agent 编排 + MCP 工具链 + RAG 知识工程 + 多模态感知自愈」，同时覆盖自动化测试效能场景，是「测开 + AI」复合方向的最强项目，也适配 AI 应用 / Agent 研发岗。投测开岗时突出「自动化测试体系」；投 AI 应用岗时突出「Agent 编排、MCP、RAG、自愈闭环」，弱化纯测试话术。

- **时间**：2026.07--2026.10
- **角色**：核心参与（Agent 编排落地）
- **技术栈**：CodeBuddy（Skill / Subagent / MCP / Rules / Memory）、Python、UIAutomator、RapidOCR、OmniParser(YOLO)、OpenCV、jieba、BM25、scrcpy

## 项目简介

基于 CodeBuddy（Skill + Subagent + MCP + Rules + Memory）构建 LLM Agent 质量效能体系，打通“自然语言需求 → 可执行代码生成 → 真机执行 → 失败自愈 → 知识沉淀”闭环，替代人工编写脚本模式；覆盖 17 个业务域、600+ 生成代码单元。

## 主要工作

- **多 Agent 编排与可靠性设计**：按职责五层编排 13 个 Skill 与 3 个自研 MCP 服务；以 Given/When/Then 意图锁定防止模型为“跑通”而降低验收标准，通过探索门禁 + 单步验证 + 九维度自审控制生成质量，设置探索预算与人工接管机制实现人机协同止损，单任务生成约 10--15 分钟（人工需 1--2 小时）。
- **RAG 与知识工程**：设计纯文件知识图谱（4 类节点 + 6 类边，按域加载降噪）与同源代码库静态推理（23 个仓库 UI 索引快照），让 Agent 生成前先检索理解研发代码；以 AST 三道闸扫描 1500+ 函数，结合 jieba + BM25 + 120+ 受控能力词表实现公共能力语义检索与自动沉淀，解决 LLM 规模化生成时“重复造轮子”问题。
- **多模态感知与自愈闭环**：融合 UIAutomator XML / RapidOCR / OmniParser(YOLO) / OpenCV 模板四层感知，链式降级 + 命中率自适应排序解决无 resource-id 控件定位问题；失败后基于证据包（截图/trace/标注图）自动再生成补丁，形成 Self-heal 闭环；scrcpy 持久流将截图耗时由约 1s 降至 30--100ms。
