<p align="center">
  <img src="./images/logo.svg" width="120" alt="Project Showcase Enhancer" />
</p>

<h1 align="center">个人项目展示增强器 · 面试作战室 — Project Showcase Enhancer</h1>

<p align="center">
  <b>把能跑的 Demo 推演成商用级产品，顺手把面试也备了。一套智能体技能（Agent Skill），打通「读懂自己代码 → 偷师真实面试 → 沉淀一问一答题库」全链路。</b>
</p>

<p align="center">
  📄 单语版本（Single-language）： <a href="./README.en.md">English</a> · <a href="./README.zh-CN.md">中文</a>
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

<h2 id="chinese">🇨🇳 中文</h2>

## 楔子

> 夫良玉韫椟，待良工而后彰其华；宝剑藏匣，遇识者而始显其锋。今之开发者，多能运斤成风，俄顷立一项目；然藏器于身而莫之能言，怀璧在握而难自陈其价。是以码虽精而人未之知，Demo 虽巧而市未之售。善作者不必善述，此古今之通患也。

本智能体技能，正为此患而生。

## 这是什么？

**个人项目展示增强器 · 面试作战室（Project Showcase Enhancer）** 是一个面向**正在备战面试的程序员**的智能体技能（Agent Skill）。它不止于「扫一遍代码吐模板」，而是一套**人机协作的面试备战工作流**：先读懂你的代码与原始意图，再与你共创，把能跑的 Demo 推演成商用级产品方案，最后产出可直接使用的文档——**项目展示文档**、**JD 驱动模拟面试**、**面试备考手册**，以及持续累积的**面试绿皮书**。

### 真实痛点：你卡住的不是"会不会写代码"

你是一个马上要去面试的程序员。真正难的，是把代码变成入场券：

- **简历项目栏写不出彩**：代码能跑，项目经历却只会写「基于 React + Node 做的博客」；
- **个人网站的项目展示模块写不好**：作品集站点有了，项目详情页却空泛得像 README 照搬；
- **拿到 JD 不知面试官怎么追问**：心仪岗位的 JD 摆在那，却缺一套 **JD 驱动的模拟面试**提前演练；
- **项目不够亮眼，需要合理包装**：真实项目可能没那么"高大上"，你要的是**基于事实把亮点放大、讲专业**，而不是编造；
- **想偷师别人的真实面试表现**：抖音上大量 UP 主分享真实面试口播，但没人帮你系统拆过——到底问了什么、怎么答才惊艳。

它在 v1 的基础上融合了四份能力，演化出四大模式：

- 源自 **code-project-analyzer** —— 代码扫描与项目文档生成的原始脚本与思路；
- 源自 **Code Analyzer** —— 深度代码解释（架构 / 调用图 / 数据流 / DDD 模式）；
- 源自 **douyin-analyzer** —— 抖音视频解析 → 提取人声 → Whisper 转写 → 内容结构化；
- 源自 **Self-Improving + 总结** —— 长期记忆累积 + 一问一答分层沉淀。

这个技能把上述几件事串成一条链：**读懂自己代码 → 偷师真实面试 → 推演 / 包装项目 → JD 模拟面试对练 → 沉淀一问一答题库**。

## 四大模式一览

```
┌─────────────────────────────────────────────────────────────┐
│  模式 A  深度代码分析      → 读懂自己的代码（架构 / DDD / 数据流）│
│  模式 B  抖音面试分析      → 偷师真实面试（视频 → 对话结构化）  │
│  模式 C  面试绿皮书生成    → 沉淀一问一答（长期记忆累积）       │
│  模式 D  展示文档 + 面试题  → 原能力保留，并喂给绿皮书          │
└─────────────────────────────────────────────────────────────┘
      A / B / D 的产出（问答）──┐
                               ▼
                        memory/ 面试绿皮书（持续变厚）
```

| 模式 | 一句话 | 输入 | 产出 |
|---|---|---|---|
| **A 深度代码分析** | 解释代码是怎么跑的（看到更深一层） | 项目目录 | `{项目}-深度代码分析.md` |
| **B 抖音面试分析** | 把面试视频变结构化问答（偷师别人） | 抖音链接 | `{作者}-{标题}-面试对话.md` |
| **C 面试绿皮书** | 把问答长期累积成题库 | 对话稿 / 面试题 / 手动文本 | `memory/绿皮书.md` + `基因文档.md` |
| **D 展示文档 + 面试题 + JD 模拟面试** | 写亮眼履历 / 包装项目 / JD 对练 | 项目目录 +（可选）JD/简历 | `{项目}-展示文档.md` + `{项目}-面试备考手册.md` + `{项目}-{岗位}-模拟面试.md` |

### 面试备战链路：你卡住的六件事，四个模式怎么接

| 你备战面试时卡住的事 | 对应模式 | 关键产出 |
|---|---|---|
| ① 读懂自己的项目，看到更深一层 | **A 深度代码分析** | `{项目}-深度代码分析.md` |
| ② 把项目写成亮眼履历 / 个人网站展示 | **D 展示文档** | `{项目}-展示文档.md` |
| ③ 合理包装项目亮点（基于事实不编造） | **D 推演 / 包装** | 商用推演 + 差距路线图 |
| ④ 拿到 JD 做模拟面试对练 | **D JD 模拟面试**（+ A） | `{项目}-{岗位}-模拟面试.md` |
| ⑤ 偷师别人的真实面试视频 | **B 抖音面试分析** | `{作者}-{标题}-面试对话.md` |
| ⑥ 沉淀成自己的题库长期复习 | **C 面试绿皮书** | `memory/绿皮书.md` + `基因文档.md` |

## 亮点

> **脚本提供确定性地图，大模型在地图上做深度推理——两者结合，既快又准，也省 token。** —— 本技能的核心设计

- **真实读懂代码（模式 A）**：先用脚本做确定性扫描，再由大模型阅读关键源文件，解释架构、调用链、数据流与 DDD 落地的真伪，而不是靠文件名猜。
- **偷师真实面试（模式 B）**：给你一个抖音面试视频，自动提取人声 → 转写 → 按「面试官问 / 候选人答」切分成一问一答，连技术点和 STAR 都标好。
- **面试绿皮书（模式 C）**：每次分析的问答自动沉淀为长期记忆，跨会话、跨来源（抖音 / 自己项目 / 手动）持续累积，并按技术点聚类成「基因文档」——你的私人高频考点库。
- **Demo 到商用的推演（模式 D）**：结合你的产品愿景，列出功能 / 工程化 / 运维三方面的差距，给出分阶段演进路线图（MVP → 完善 → 商用）。
- **混合架构**：脚本做快而稳的扫描与转写，大模型做深而准的推理，兼顾速度与质量。

## 快速上手

### 前提

```bash
# 1. 已安装支持「智能体技能（Agent Skill）」的客户端（本技能以用户级技能形式存放）
# 2. 建议在「高推理模型」下使用（见「配置」）
#    推荐：Claude Opus 4.6 / DeepSeek v4 Pro / GPT-5.6

# 3.（可选）按所需模式安装依赖：
pip install pdfplumber python-docx pypdf        # 解析简历（模式 D）
pip install openai-whisper requests scipy imageio-ffmpeg  # 抖音面试（模式 B）
node 环境                                      # 代码扫描（模式 A/D）
```

### 安装技能

```bash
# 方式一：从 GitHub 克隆到用户级技能目录
git clone https://github.com/whishi47/project-showcase-enhancer-skill.git \
  "$HOME/.workbuddy/skills/project-showcase-enhancer"

# 方式二：从压缩包解压到 $HOME/.workbuddy/skills/project-showcase-enhancer/
#   确保目录下直接包含 SKILL.md

# 方式三：SkillHub 市场安装
#   在 SkillHub 搜索 project-showcase-enhancer-skill 并安装
```

> `$HOME` 在 Windows 上通常是 `C:\Users\你的用户名`。技能目录也可能是 `.codebuddy\skills`，以你使用的客户端为准。安装后无需编译，在客户端对话中直接用自然语言触发即可。

### 一句话触发

| 触发方式 | 你说的话 | 进入 |
|---|---|---|
| 💬 自然语言 | "深度分析一下我的项目" | 模式 A |
| 💬 自然语言 | "分析这个抖音面试视频：<链接>" | 模式 B |
| 💬 自然语言 | "把这份面试对话存进绿皮书" | 模式 C |
| 💬 自然语言 | "帮我把这个项目推演到商用，并出展示文档和面试题" | 模式 D |
| 📎 简历文件 | 上传 PDF / DOCX / TXT | 解析为纯文本，供模式 D 使用 |

首次触发时，技能会一次性问清（不用逐条回答）：**要做哪个模式**、**项目路径 / 抖音链接 / 已有对话稿**、**（模式 D）使用场景与岗位方向**。

## 实战演练：四个模式各跑一遍

> 光说「能生成文档」太空泛。下面把每个模式**真正跑起来**，让你看到「命令 → 输出」长什么样。示例输出为节选，真实结果会更长更完整。

### 模式 A · 深度代码分析

你说：*"深度分析一下 `./my-app` 这个项目。"*

技能先跑两个脚本（确定性扫描），再让大模型在「地图」上做深度解读：

```bash
node scripts/scan_project.js ./my-app
python scripts/deep_analyze.py ./my-app --output my-app-深度代码分析.md
```

`deep_analyze.py` 给出结构化判断，大模型据此写出带文件名/函数名证据的解读。示例输出片段：

```markdown
## 架构风格
检测到 **Layered（分层）** 架构：controller → service → repository 三层，
边界清晰；但 `service/OrderService.java` 同时承担了「发邮件」与「算库存」，
存在上帝类倾向。

## DDD 模式复盘
- 聚合根：Order（含 OrderItem 值对象）✅ 落地正确
- 仓储：OrderRepository 接口 + MyBatis 实现 ✅
- ⚠️ 贫血模型预警：`User` 实体仅有 getter/setter，
  业务规则（如「禁用用户不可下单」）散落在 Service 而非实体中。

## 关键调用链
OrderController.createOrder() → OrderService.create()
  → InventoryService.lock() → OrderRepository.save()
```

### 模式 B · 抖音面试分析

你说：*"分析这个抖音面试视频：https://v.douyin.com/xxxx/"*

```bash
python scripts/douyin_interview.py --url "https://v.douyin.com/xxxx/" --output interview-raw.md
```

管道依次：bugpk 解析元数据 → 下载视频 → 提取**人声**音轨 → Whisper 转写 → 大模型润色并结构化。示例输出片段（`{作者}-{标题}-面试对话.md`）：

```markdown
### Q1：说说 Redis 缓存穿透怎么解决？
**A**：缓存空值 + 布隆过滤器两道闸门；热点 key 用逻辑过期避免击穿……
**技术点**：`Redis` `缓存穿透` `布隆过滤器`
**STAR**：候选人举了「秒杀库存」场景，QPS 从 2k 扛到 5w。

### Q2：分布式锁用 Redis 还是 ZooKeeper？
**A**：CAP 取舍——Redis 性能好但需处理锁过期，ZK 强一致但吞吐低……
**技术点**：`分布式锁` `ZooKeeper` `Redisson`
```

> 若当前模型**不支持多模态**，视觉分析自动跳过，只走音频流程并明确告知你——不会假装做了画面分析。

### 模式 C · 面试绿皮书

你说：*"把上面这份面试对话存进绿皮书。"*

```bash
python scripts/build_greenbook.py \
  --input interview-raw.md \
  --source "douyin|https://v.douyin.com/xxxx/" \
  --author "技术UP主-老李" \
  --topic "后端八股" \
  --date "2026-07-25"
```

脚本把问答追加进 `memory/绿皮书.md`（自动编号「面试对话 N」），更新目录，并维护 `memory/index.json` 与 `memory/基因文档.md`。示例输出片段：

```markdown
# 面试绿皮书 📗
## 目录
- [面试对话一 · 后端八股 · 2026-07-25 · douyin](#面试对话一)

## 面试对话一
**来源**：douyin · https://v.douyin.com/xxxx/ | **作者**：技术UP主-老李 | **日期**：2026-07-25

### Q1：说说 Redis 缓存穿透怎么解决？
**A**：缓存空值 + 布隆过滤器……
**技术点**：`Redis` `缓存穿透` `布隆过滤器`
```

`基因文档.md` 则按技术点聚类，长期累积「高频考点 → 推荐答法骨架」：

```markdown
## Redis
- 缓存穿透（被问 3 次）：缓存空值 + 布隆过滤器 [来自 面试对话一/三/五]
- 分布式锁（被问 2 次）：Redisson 看门狗自动续期 [来自 面试对话一/四]
```

### 模式 D · 展示文档 + 面试题 + JD 模拟面试

你说：*"把 `./my-app` 推演到商用，出一份展示文档，结合我的 JD 出 15 道面试题，再做一轮 JD 模拟面试，都存进绿皮书。"*

技能走完推演对话后，产出三份文档：展示文档、面试备考手册，以及 **JD 驱动模拟面试**。其中面试题与模拟面试问答提示你调用模式 C（来源 `self-project`）一并沉淀。

`{项目}-面试备考手册.md` 示例（节选）：

```markdown
### 必问 1：订单创建这块你是怎么保证一致性的？
- 考察点：事务边界、最终一致、幂等
- 策略：先讲本地事务（@Transactional），再讲跨服务用消息表保证最终一致
- STAR：曾因重复提交产生两笔订单 → 加幂等键解决
```

`{项目}-{岗位}-模拟面试.md` 示例（节选，角色扮演式）：

```markdown
> 面试官视角（基于你的 JD「高并发交易系统」+ 项目真实代码）
**Q**：订单创建你用了本地事务，如果扣库存和创建订单不在同一个库，怎么保证一致？
**推荐答法**：① 先承认跨库不能用本地事务；② 用"本地消息表 / Saga"保证最终一致；
  ③ 用项目里 `InventoryService.lock()` 的真实逻辑佐证；④ 提幂等键防重复。
**追问（面试官）**：那消息丢了怎么办？
**推荐答法**：消息表 + 定时回查 + 人工兜底；我们项目里 `OrderRepository.save()` 后发事件走事务消息……
```

## 工作原理

```
┌──────────────────────────────────────────────────────────┐
│            project-showcase-enhancer-skill                 │
│   输入：项目目录 / 抖音链接 / 对话稿 +（可选）JD + 简历    │
└───────────────────────────┬──────────────────────────────┘
                            ▼
   ┌──────────────────────────────────────────────┐
   │ A 深度代码分析                                  │
   │   scan_project.js + deep_analyze.py（脚本）     │
   │   + 大模型语义解读（架构/DDD/数据流）           │
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ B 抖音面试分析                                  │
   │   douyin_interview.py（解析→人声→Whisper→结构化）│
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ C 面试绿皮书（长期记忆）                        │
   │   build_greenbook.py → memory/（只追加不覆盖）  │
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ D 展示文档 + 面试题（原能力保留）              │
   │   → {项目}-展示文档.md + 面试备考手册.md        │
   └──────────────────────────────────────────────┘
```

**三层混合架构**：① 脚本做确定性扫描 / 转写（快、稳、零语义消耗）；② 大模型在脚本产物之上做只有 LLM 能做的深度推理；③ 绿皮书把产出沉淀为跨会话长期记忆。

## 模式详解

### 模式 A：深度代码分析（融合 Code Analyzer）

- **A.1 快速扫描**：`scan_project.js`（技术栈/依赖/目录树）+ `deep_analyze.py`（架构风格/调用图/数据流/DDD 模式/圈复杂度高危点），输出 JSON + Markdown。
- **A.2 深度阅读**：基于扫描结果，大模型**必须引用具体文件名、函数名、代码片段**，解释架构、执行流程、数据流、业务规则，并复盘 DDD 模式真伪。
- **A.3 输出**：`{项目}-深度代码分析.md`，同时作为模式 D 的「技术深度」素材。
- 约束：模式 A 必须先跑两个脚本，不得跳过脚本直接靠 LLM 猜。

### 模式 B：抖音面试分析（融合 douyin-analyzer，条件视觉）

- **B.1 接收链接** → **B.2 跑管道** `douyin_interview.py`（解析→下载→提取人声→Whisper 转写→可选截帧）。
- **B.3 润色** → **B.4 面试对话结构化**（核心）：LLM 自动区分「面试官 / 候选人」，每条拆为 Q/A + 技术点 + STAR。
- **B.5 视觉分析**（仅多模态模型）：逐帧画面描述 + 制作方式判断，作为「视频形式」附注，不影响问答主体。
- **B.6 进绿皮书**：提示你是否把本次问答沉淀进 `memory/绿皮书.md`。
- 依赖缺失时脚本会**在入口明确提示安装命令并中止**，不会默默失败。

### 模式 C：面试绿皮书生成（融合 Self-Improving + 总结）

- **C.1 三路来源**：抖音视频、自己项目面试题、手动任意文本。
- **C.2 运行累积器** `build_greenbook.py`，解析 Q/A、追加为「面试对话 N」、更新目录与 `index.json`、维护 `基因文档.md`。
- **C.3 绿皮书结构**：顶部目录 + 每条问答带 `技术点`/`STAR` 标签。
- **C.4 基因文档**：按技术点聚类的长期知识库，可单独复习。
- 记忆原则：只追加不覆盖；每条问答标注来源（抖音/自己项目/手动），可追溯。

### 模式 D：展示文档 + 面试题 + JD 模拟面试（原能力保留并增强）

- **D.1 项目定位** → **D.2 商用推演对话**（愿景→差距 P0/P1/P2→路线图，基于事实包装、标注"规划中"）。
- **D.3 生成交付物**：展示文档（亮眼履历 / 个人网站展示）+ 15 道面试题（必问 / 针对 / 追问）+ **JD 驱动模拟面试**（角色扮演对练：面试官出题 + 推荐答法 + 追问链）。
- **D.4 合理包装**：用模式 A 的代码证据把"做了功能"升级为"解决业务问题、工程权衡"，绝不编造。
- **D.5 并入绿皮书**：提示把面试题与模拟面试问答按 Q/A 调用模式 C 沉淀（来源 `self-project`）。

## 容易做错的地方

> 这一节专门讲「坑」。照着避，能省下大把排查时间。

1. **模型不是高推理**：用低推理模型，代码理解会浅、推演会模板化、问答拆分会乱。触发后先看技能提示，必要时切到 Opus 4.6 / DeepSeek v4 Pro / GPT-5.6。
2. **没先跑脚本就靠 LLM 猜**：模式 A 必须先跑 `scan_project.js` + `deep_analyze.py`，模式 B 必须先跑 `douyin_interview.py`。跳过脚本，结论没有证据支撑。
3. **抖音链接失效 / bugpk 解析失败**：分享口令或短链可能过期。管道会在入口报明确错误；换一个能正常打开的链接重试。
4. **Whisper 没装**：模式 B 依赖 `openai-whisper`。没装时脚本会提示 `pip install openai-whisper requests scipy imageio-ffmpeg` 并中止，不要硬跑。
5. **记忆目录没随 git 提交**：`memory/` 下的绿皮书与基因文档是长期资产。换机 / 重装前务必 `git add memory/ && git commit && git push`，否则题库丢失。
6. **非多模态模型硬要视觉分析**：模式 B 当前模型不支持图像时，视觉分析自动降级为纯音频——不要误以为「做了画面分析」。
7. **简历解析报「依赖缺失 / 读取失败」**：见下节「内置脚本」。多为 `pdfplumber` 未装或 PDF 被加密/是扫描件，按提示安装依赖或换 OCR 即可。

## 配置

本技能要求**高推理能力**的大模型。**推荐模型**：

- Claude Opus 4.6
- DeepSeek v4 Pro
- GPT-5.6（或同等级别）

低推理模型仍能用，但质量明显下降。技能在入口会提示你确认当前模型，若不满足建议切换后再用。

> 💡 建议：把常用的高推理模型设为客户端默认，或在触发技能前手动切换，以获得最佳推演与文档质量。

**多模态要求（仅模式 B 的视觉分析）**：触发模式 B 时技能会先检测当前模型是否支持图像输入；不支持则自动降级纯音频流程。

## 内置脚本

### `scripts/scan_project.js`

硬编码字典扫描项目，输出结构化 JSON。不调用大模型，速度快、确定性强。

```bash
node scripts/scan_project.js <项目目录> [--max-depth N]
```

> **错误提示已增强（v2）**：路径不存在 / 不是目录时，会在入口明确拦截并给出排查清单，而非静默输出空结果；扫描途中某目录读不到，会跳过并写入 `warnings`，最后把警告汇总打到 stderr，不影响 stdout 的 JSON 解析。

### `scripts/deep_analyze.py`

AST / 启发式深度分析（架构风格、调用图、数据流、DDD 模式、圈复杂度高危点），输出 JSON + Markdown。纯标准库，无第三方依赖。

```bash
python scripts/deep_analyze.py <项目目录> --output report.md
```

### `scripts/douyin_interview.py`

抖音面试管道：解析 + 下载 + 提取人声 + Whisper 转写 + 可选截帧。

```bash
python scripts/douyin_interview.py --url "<抖音链接>" --output interview-raw.md
```

依赖：`openai-whisper requests scipy imageio-ffmpeg`。缺失时入口即提示安装命令并中止。

### `scripts/build_greenbook.py`

一问一答 → 累积绿皮书 + 基因文档 + 索引。纯标准库。

```bash
python scripts/build_greenbook.py --input dialogue.md \
  --source "douyin|<url>" --author "<作者>" --topic "<主题>" --date "YYYY-MM-DD"
```

### `scripts/parse_file.py`

把简历 PDF / DOCX / TXT 解析为纯文本（模式 D 用）。

```bash
python scripts/parse_file.py ./resume.pdf
```

> **错误提示已增强（v2）**：任何失败都返回带 `[分类]` 前缀的「人话」——含原因 + 排查步骤，**不再抛出一堆看不懂的 traceback**。常见情形：
> - `[依赖缺失]`：未装 `pdfplumber`/`pypdf`/`python-docx` → 提示 `pip install ...`
> - `[PDF 读取失败]`：文件加密 / 损坏 / 是扫描件 → 提示解密、换 OCR 或换 pypdf
> - `[文件不存在]` / `[路径非文件]` / `[格式不支持]`：路径或扩展名问题 → 提示核对路径与支持格式

## 目录结构

```
project-showcase-enhancer/
├── SKILL.md                          # 技能主文件（工作流定义）
├── README.md                         # 双语版（主文档）
├── README.en.md                      # 英文版
├── README.zh-CN.md                   # 中文版
├── 简介.md                            # SkillHub 审核简介文案
├── images/
│   └── logo.svg
├── scripts/
│   ├── scan_project.js               # 项目扫描器：字典匹配 → JSON
│   ├── deep_analyze.py               # 深度代码分析：AST/启发式 → JSON+MD
│   ├── douyin_interview.py           # 抖音面试管道：解析→人声→Whisper→结构化
│   ├── build_greenbook.py            # 绿皮书累积：一问一答 → 长期记忆
│   └── parse_file.py                 # 简历解析器：PDF/DOCX/TXT → 文本
├── assets/
│   ├── showcase-template.md          # 项目展示文档模板
│   ├── interview-prep-template.md    # 面试备考手册模板
│   ├── deep-analysis-template.md     # 深度代码分析模板
│   ├── interview-dialogue-template.md# 一问一答对话稿模板
│   └── greenbook-template.md         # 面试绿皮书模板
└── memory/                           # 长期记忆（随 git 提交持久化）
    ├── 绿皮书.md                       # 持续累积的一问一答题库
    ├── 基因文档.md                     # 按技术点聚类的高频考点
    └── index.json                     # 机器可读索引
```

## 用户怎么说（SkillHub 评分）

本技能发布于 SkillHub，综合评分 **4.5 / 5（满分 4.5）**。两个维度的原始评语如下，v2 已逐条回应：

> **C · 规范性（Convention）4.2 / 5**
> 「文档层次分明，从浅到深逐步引导，配套模板拿来即用，脚本帮你快速扫描项目。但缺少一步步的实际操作示例，不知道最终输出的效果到底怎样，也没人告诉你哪里容易做错。」

> **R · 可靠性（Reliability）4.4 / 5**
> 「整体运行比较可靠，扫描和分析过程很少崩溃，两个脚本在遇到小问题时会跳过继续执行而不是直接报错。功能覆盖从项目分析到面试准备全链路，模板内容也很丰富。不过如果 PDF 库没装好，或者目录读取出错，提示信息不够清晰，需要用户有一定排查能力。」

**v2 的回应：**

- 针对「缺少实际操作示例」→ 新增上文「[实战演练](#实战演练四个模式各跑一遍)」：四个模式逐一给出「你说的话 → 运行命令 → 真实样例输出」。
- 针对「没人告诉你哪里容易做错」→ 新增「[容易做错的地方](#容易做错的地方)」：七条高频坑位与避雷方法。
- 针对「PDF 库 / 目录读取提示不清晰」→ 重写 `parse_file.py` 与 `scan_project.js` 的错误提示：所有失败返回带原因 + 排查步骤的人话；目录不存在 / 非目录在入口即明确拦截，扫描中途的读取失败也会写入 `warnings` 并汇总提示。

## 发布

```bash
# 方式一：SkillHub 网页发布
#   进入 https://skillhub.cn ，上传打包好的 project-showcase-enhancer.zip
#   Slug: project-showcase-enhancer，显示名称：个人项目展示增强器 · 面试作战室

# 方式二：SkillHub CLI 发布
#   登录后执行 skillhub publish ./project-showcase-enhancer-skill

# 重新打包（需 skill-creator 的 package_skill.py）
python package_skill.py ./project-showcase-enhancer-skill ./dist
```

> 发布前记得同步更新 SKILL.md 中的 `version` 字段。

## 协议

MIT © 2026

---

<h2 id="english">🇬🇧 English</h2>

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
├── README.en.md                      # English version
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
