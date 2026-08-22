# 手机地图 UI 自动化平台（AI Agent）

> 岗位适配：**首选** 测试开发（测开，移动端 / 智能体方向）、AI 应用开发 / Agent 开发；**次选** AI 工程

> 理由：LLM Agent 编排 + 多 MCP 服务 + 感知定位引擎 + 知识工程 + 稳定性工程，是「AI 智能体测开」最深入的项目，技术密度与规模感强；与 LLM Agent 质量效能工程高度同源（同一套 CodeBuddy 体系），投递时建议二选一，避免内容重复；投 AI 应用岗时突出 Agent/MCP/知识工程。

- **时间**：2026.07--2026.10
- **角色**：核心参与（框架建设）
- **技术栈**：CodeBuddy（Skill / Subagent / MCP / Rules / Memory）、Python、uiautomator2、scrcpy、OpenCV、RapidOCR、OmniParser(YOLO)、jieba / BM25

## 项目简介

面向手机地图 Android 端复杂 UI 场景的智能体自动化测试体系，基于 CodeBuddy（Skill + Subagent + MCP + Rules + Memory）编排 13 个 Skill 与 3 个自研 MCP 服务，打通“需求理解 → 用例生成 → 审查调试 → 精准回归 → 平台回填”全生命周期，替代传统人工编写 Appium 脚本的模式；框架覆盖 17 个业务域、600+ 用例。

## 主要工作

- **智能体编排与生成工作流**：按需求理解、用例生成、质量保障、回归筛选、平台对接五层职责编排 Skill——联动 TAPD/Figma MCP 从需求自动生成 C1/C2/C3 分级文本用例、存量 xlsx 用例转 BDD；核心中枢三阶段生成可执行 case.py（锁定 Given/When/Then 防意图漂移 → 全链路探索门禁 + 逐步探针单步验证 + 九维度自审 → lint 与知识沉淀回填智研平台）；辅以 8 维度稳定性静态体检与代码 diff 驱动的 P0/P1/P2 精准回归圈选；设置探索预算与单次时长上限，超限自动调起人工录制 Skill 接管，形成“AI 提效 + 人工止损”的人机协同机制，单用例生成约 10--15 分钟（手写需 1--2 小时）。
- **多 MCP 服务与感知定位引擎**：自研设备控制 MCP（17 个工具按准备/感知/决策/执行分组，支撑单步探针执行与截图/OCR/YOLO 并行感知）、线上批次失败诊断 MCP（按批次一键拉齐日志/截图/源码供 AI 根因分析），并接入腾讯地图官方 MCP 将地点名动态解析为坐标以构造 schema 跳转与测试数据；构建 XML/RapidOCR/OmniParser(YOLO)/模板匹配四层分级感知与 L1 → L3 链式降级定位 + 命中率自适应排序，解决自绘控件无 resource-id、动态页面与多分辨率适配的定位不稳定问题；scrcpy 持久流将截图耗时从约 1s 降至 30--100ms，支持多设备 session 隔离并行调试。
- **知识工程与语义检索**：设计纯文件知识图谱（Page/Component/Pitfall/Operation 四类节点 + 6 类边，17 模块按域加载降噪，文件即真相源、git 可 review），并基于 23 个研发仓库的 UI 索引快照做同源静态推理，让 Agent 写用例前先“读懂”研发代码，产出页面跳转链与控件定位预测，低置信度条目诚实标注待实机校准；以 AST 三道闸（hash 主版本占比/依赖可解析性/模式纯度）扫描 1500+ 私有 helper，结合 jieba 分词 + BM25 + 120+ 受控能力词表实现公共方法两层沉淀与语义检索，弹窗/踩坑/锚点经验随执行自动回流复用。
- **稳定性工程**：Lint 静态门禁禁止裸坐标、裸 sleep 等不稳定写法，每步强制后置断言，证据链全量落盘（before/after/verify 截图 + XML + trace + 标注图）支持失败回放与再生成修复；以 health.json 记录 10/30/100 次回测通过率，驱动用例生命周期（untested → active → stable/flaky）与 HTML 稳定性报告，单 case 耗时控制在 180s 内。
