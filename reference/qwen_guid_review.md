# 大模型简历素材与面试知识清单

> 来源说明：由早期大模型求职素材和算法岗简历草稿整理而来；本仓库保留的是清洗后的复盘清单。
>
> 使用方式：先看第 1-3 节决定哪些内容能写进简历；面试前复习第 5-7 节。凡是标注“需确认”的指标，只有在你能解释实验口径、数据来源和评估方法时才建议写入简历。

## 1. 可加入简历的内容

### 1.1 高优先级素材

| 素材 | 适合写入位置 | 当前状态 | 推荐简历表述 |
| --- | --- | --- | --- |
| 三层记忆管理：短期窗口、长期摘要、结构化状态 | 重庆啄木鸟 - 小啄 GPT | 已写入算法岗模板 | 针对多轮客服对话中上下文丢失和槽位遗漏问题，设计“短期记忆 + 长期摘要 + 结构化状态”的记忆管理机制，在每轮 Prompt 中动态注入关键业务状态。 |
| DST 对话状态追踪 | 重庆啄木鸟 - 小啄 GPT | 已写入 | 使用 JSON 维护家电类型、故障现象、预约时间等状态字段，提升长轮次对话的流程控制和指令遵循稳定性。 |
| 混合检索：Dense + BM25 + RRF + Rerank | 重庆啄木鸟 - 小啄 GPT 检索增强 | 已写入 | 构建商品手册、促销策略、维修手册知识库，采用向量召回、关键词召回、RRF 融合与 Rerank 精排，改善型号、故障码等专有词召回。 |
| Text-to-SQL 自修正 | 智能数据分析问答助手 | 已写入 | 引入 SQL 试执行与 Self-Correction 机制，捕获 MySQL Error Message 后回传给 LLM 重写 SQL，降低语法错误和 Schema 幻觉风险。 |
| 数据字典元数据增强 | 智能数据分析问答助手 | 已写入 | 将表名、字段名、字段含义和常见枚举值拼接为富文本后向量化，提高业务术语、字段语义和多表关联场景下的召回质量。 |
| RAGAS/Golden Dataset 评估闭环 | 智能数据分析问答助手 | 已写入 | 构建 Golden Dataset，使用 Context Recall、Faithfulness、Execution Accuracy 评估检索与 SQL 结果，并通过 Bad Case 回流优化 Prompt 和知识库。 |
| FastAPI 流式响应与同步/异步边界 | 专业技能或项目追问 | 可补充到面试话术，不建议塞入主简历 | 使用 `StreamingResponse` 封装大模型流式输出；对同步 SDK 或阻塞 IO 通过线程池隔离，避免阻塞事件循环。 |
| vLLM/PagedAttention 推理优化 | 智能家电识别与自动入库系统 | 已写入基础表述，可面试展开 | 接入 vLLM 管理 KV Cache 与动态批处理，提高模型服务吞吐；实际提升需按项目压测口径说明。 |
| Dify 多 Agent 编排 | 智能家电识别与自动入库系统 | 已写入 | 基于 Dify 编排“识别 - 联网补全 - 字段校验 - 向量去重 - 入库”流程，将图像/OCR 结果转为结构化产品数据。 |

### 1.2 谨慎加入的量化指标

| 指标 | 建议状态 | 使用条件 | 更稳妥的表达 |
| --- | --- | --- | --- |
| 长尾 Query 检索 Hit Rate 提升约 20% | 可用但需确认 | 你能说明测试集规模、命中定义、对比基线和统计时间 | 在包含型号、故障码的长尾 Query 上，相比单一路径检索，混合检索策略带来更高召回与更少幻觉回复。 |
| SQL 执行成功率 70% -> 90%+ | 可用但需确认 | 你能说明 SQL 成功率定义、测试问题数量、是否包含语义正确性 | 通过 SQL 试执行与自修正机制，显著降低语法错误和字段幻觉；在项目测试集中执行成功率提升至 90%+。 |
| 500 条 Golden Dataset | 可用但需确认 | 你确实参与构建或使用过该测试集，并能说明标注来源 | 构建面向真实业务问题的离线评估集，覆盖检索召回、事实一致性和 Text-to-SQL 执行结果。 |
| vLLM 吞吐提升多少 | 不建议写具体倍数，除非有压测 | 你有本项目基线和压测脚本 | 使用 vLLM 优化模型服务吞吐和 KV Cache 显存利用，具体收益根据序列长度、并发和 batch 策略评估。 |
| 工程师招聘成本下降 10% | 不建议写入当前医药问答项目 | 该指标和“医药供应链数据问答”业务背景不一致，面试官会追问 | 改成“支撑校企合作项目交付与竞赛展示，获得重庆市人工智能大赛市级银奖”。 |

### 1.3 可作为“备选加分项”的素材

- RAG 知识版本管理：`doc_id`、`version`、`effective_date`、`status`、`source` 等元数据，以及 `active/expired` 软删除策略。适合面试追问，不建议简历展开太多。
- 相似度阈值与拒答策略：适合“如何防幻觉”追问，可体现你不是只会堆 Prompt。
- 在线反馈闭环：点赞/踩、Bad Case 分析、Prompt 或知识库迭代。适合项目复盘。
- RAG-Fusion：适合“如何优化模糊 Query”追问。简历中除非实际落地，否则写“了解/研究过”即可。
- FastAPI 生命周期管理：`lifespan` 初始化 Milvus/vLLM 客户端、DB 连接池，适合工程能力追问。

## 2. 建议替换到简历的表述

### 2.1 小啄 GPT 智能回复模型

**原始方向**

- 微调开源 Qwen 大模型，提高多轮对话场景回复准确率、指令遵循率及回复多样性。
- 设计对话状态标注体系与动态指令注入机制。
- 构建知识库检索增强模块。

**优化后表述**

> 针对家电客服多轮对话中的上下文丢失、槽位遗漏和回复不可控问题，基于 Qwen 进行微调与指令优化；设计“短期记忆 + 长期摘要 + 结构化状态”的三层记忆机制，用 JSON 维护家电类型、故障现象、预约时间等关键状态，并在每轮 Prompt 中动态注入，提升长轮次对话的流程控制与指令遵循稳定性。

**面试展开重点**

- 为什么不能直接拼接全部历史：Token 成本高、上下文窗口受限、长文本中间信息利用不稳。
- 为什么需要 DST：客服任务里“关键信息是否收集齐”比“模型是否记得原话”更重要。
- 如何评估：人工标注多轮对话样本，检查状态字段完整率、指令遵循率、人工可采纳率。

### 2.2 小啄 GPT 检索增强

**优化后表述**

> 构建商品手册、促销策略与维修手册知识库，采用 Dense 向量召回 + BM25 关键词召回 + RRF 融合 + Rerank 精排的混合检索策略，解决型号、故障码等专有词匹配不准的问题；若项目指标可确认，可补充“长尾 Query 检索 Hit Rate 提升约 20%”。

**面试展开重点**

- Dense 召回适合语义泛化，如“空调不冷”匹配“制冷故障”。
- BM25 适合精确词，如型号、故障码、专有名词。
- RRF 用排名融合不同召回结果，避免直接归一化不同检索器分数。
- Rerank 进一步计算 Query 和候选文档相关性，筛出更适合注入 LLM 的 Top-K。

### 2.3 智能家电识别与自动入库系统

**优化后表述**

> 针对 OCR/图片识别结果不完整、人工补全成本高和重复入库问题，使用 Docker/Miniconda 统一部署 OCR/视觉大模型，接入 vLLM 优化推理吞吐；基于 Dify 编排“识别 - 联网补全 - 字段校验 - 向量去重 - 入库”多 Agent 流程，结合 Prompt 约束和相似度匹配完成产品信息抽取、补全、去重与自动化入库，并使用 FastAPI 封装服务接口。

**面试展开重点**

- OCR 错误如何处理：字段校验、正则/枚举校验、联网补全、多源交叉验证、低置信转人工。
- 去重如何做：品牌、型号、规格字段标准化后向量相似度 + 规则匹配。
- vLLM 如何调参：关注显存、序列长度、并发、`max_num_batched_tokens`、`gpu_memory_utilization`。

### 2.4 智能数据分析问答助手

**优化后表述**

> 面向药品采购、零售、库存等全链路数据，建设基于 LLM 的医药供应智能数据分析问答助手，将业务人员的自然语言问题转化为可执行 SQL 与分析结果；负责 LLM 应用架构、RAG 知识库与 Text-to-SQL 质量优化。

> 基于 Dify/LangChain 完成 LLM 工程化部署，使用 Milvus 构建外部知识库；对数据字典进行元数据增强，将表名、字段名、字段含义和常见枚举值拼接为富文本后向量化，并结合 HNSW 索引与标量过滤提高多表关联、专业术语和时间/分类条件的召回精度。

> 设计规则化问题分类、样例对、CoT 和约束 Prompt，引导模型生成 SQL；引入 SQL 试执行与 Self-Correction 机制，捕获 MySQL Error Message 后回传给 LLM 反思重写，最多重试 3 次，将 SQL 执行成功率由约 70% 提升至 90%+。该指标需确认真实测试口径。

**面试展开重点**

- 医药数据难点：多表关系复杂、字段命名偏业务、枚举值和时间条件多。
- 检索不准怎么解：数据字典富文本化、元数据过滤、业务术语同义词、Rerank。
- SQL 错误怎么解：先试执行，报错回传，再重写；语义错误则需要人工标注集或执行结果对比。
- 如何防幻觉：检索阈值、Schema 约束、只基于上下文回答、SQL 执行校验、Bad Case 回流。

## 3. 不建议写入简历但适合面试展开的内容

| 内容 | 不建议写入原因 | 面试使用方式 |
| --- | --- | --- |
| 4 周复习计划 | 这是准备计划，不是项目成果 | 自己复习用即可。 |
| 行为面试话术 | 简历不应写职业动机和公司适配套话 | 面试自我介绍时自然表达。 |
| Kubernetes、Celery、Nginx 负载均衡 | 原文件只是“如何保证可规模化”的泛化回答，未证明项目落地 | 如果被问系统扩展，可说“可以引入”，不要说“我已实现”。 |
| “工程师招聘成本下降 10%” | 与医药数据问答项目背景不贴合，容易被质疑 | 除非能解释业务链路，否则删除。 |
| “LoRA 与全量微调几乎无差异” | 容易被认为绝对化，且需实验支撑 | 改为“在数据分布集中、rank 合理时，LoRA 常能取得接近全量微调的效果”。 |
| “RAG 一定减少幻觉” | RAG 检索错或上下文注入错仍会幻觉 | 改为“RAG 提供 grounding 和可追溯性，但仍需评估、阈值和拒答策略”。 |
| “Qwen 与 LLaMA 高度兼容” | 容易被追问架构细节，表述过强 | 改为“Qwen 在 HuggingFace、PEFT、vLLM 等工程生态中支持成熟”。 |

## 4. 技术正确性校验与修正版口径

### 4.1 Transformer 与 Self-Attention

**正确口径**

- Transformer 是基于注意力机制的序列建模架构，不依赖 RNN/CNN。
- Scaled Dot-Product Attention 的常见公式是 `softmax(QK^T / sqrt(d_k))V`。
- 多头注意力通过多个 head 并行关注不同子空间的信息。

**面试时避免**

- 不要说“除以 `sqrt(d_k)` 是防止梯度消失”。更准确是避免点积随维度变大导致 softmax 进入饱和区，使梯度变小、训练不稳定。

**参考**

- Attention Is All You Need: https://arxiv.org/abs/1706.03762

### 4.2 Lost in the Middle 与三层记忆

**正确口径**

- 长上下文模型并不总能稳定利用所有位置的信息，相关信息在上下文中间时性能可能下降。
- 三层记忆不是标准固定范式，而是工程设计：短期窗口保连贯，长期摘要控 Token，结构化状态保业务槽位。

**简历口径**

- 可以写“设计三层记忆机制”，但不要写“无论多少轮都不会丢失状态”。更稳的是“降低长轮次对话中的关键信息丢失风险”。

**参考**

- Lost in the Middle: https://arxiv.org/abs/2307.03172

### 4.3 RAG

**正确口径**

- RAG 将参数化模型与外部非参数知识源结合，使模型在生成时利用检索到的上下文。
- RAG 能提升事实 grounding、可更新性和可追溯性，但效果取决于检索、切块、重排、上下文约束和评估。

**简历口径**

- 写“通过 RAG 引入外部知识，降低无依据回复风险”比“解决幻觉问题”更稳。

**参考**

- Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks: https://arxiv.org/abs/2005.11401
- Dify Knowledge: https://docs.dify.ai/en/guides/knowledge-base

### 4.4 Milvus、HNSW 与标量过滤

**正确口径**

- Milvus 支持多种向量索引，包括 FLAT、IVF_FLAT、HNSW 等。
- 标量过滤可以在 ANN 搜索前缩小搜索范围，也可以通过迭代过滤处理复杂表达式。
- HNSW 通常适合低延迟、高召回场景，但内存成本更高；是否最佳取决于数据量、维度、内存和延迟要求。

**简历口径**

- 可以写“结合 HNSW 索引与标量过滤提升检索精度”，但不要写“HNSW 一定最快/最好”。

**参考**

- Milvus Index Vector Fields: https://milvus.io/docs/index-vector-fields.md
- Milvus Filtered Search: https://milvus.io/docs/filtered-search.md

### 4.5 RAGAS 指标

**正确口径**

- Faithfulness 衡量回答中的事实声明是否能被检索上下文支持。
- Context Recall 衡量相关信息是否被成功检索出来，通常需要参考答案或参考上下文。
- Text-to-SQL 还应补 Execution Accuracy，即生成 SQL 的执行结果是否与标准 SQL 一致。

**简历口径**

- “使用 RAGAS 的 Context Recall/Faithfulness 与 Execution Accuracy 评估检索和 SQL 结果”是合理表述。

**参考**

- RAGAS Faithfulness: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/
- RAGAS Context Recall: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/

### 4.6 LoRA

**正确口径**

- LoRA 冻结预训练模型权重，在 Transformer 层注入可训练的低秩矩阵，从而减少下游任务的可训练参数。
- LoRA 论文在 GPT-3 175B 实验中报告：可训练参数减少约 10,000 倍，GPU 显存需求降低约 3 倍。
- 实际收益取决于模型、rank、target modules、序列长度、batch size 和训练框架。

**需要修正的原说法**

- 原说法“训练参数仅为整体参数的万分之一、显存占用减少 2/3”可改为“论文在特定 GPT-3 175B 设置中报告约 10,000 倍可训练参数减少和约 3 倍 GPU 显存需求降低，实际收益取决于配置”。

**参考**

- LoRA: https://arxiv.org/abs/2106.09685

### 4.7 QLoRA

**正确口径**

- QLoRA 通过 4-bit NormalFloat、双重量化和分页优化器降低微调显存。
- 论文展示了在单张 48GB GPU 上微调 65B 模型的能力。
- “24GB 卡上微调 32B 甚至更大”不能泛化，具体取决于模型结构、序列长度、batch、gradient checkpointing、量化实现和显存碎片。

**需要修正的原说法**

- 原说法“24G 的 4090/3090 上微调 32B 甚至更大”建议改为“QLoRA 显著降低显存门槛，但具体可训练规模需以模型和训练配置验证为准”。

**参考**

- QLoRA: https://arxiv.org/abs/2305.14314

### 4.8 vLLM 与 PagedAttention

**正确口径**

- PagedAttention 借鉴操作系统分页思想管理 KV Cache，减少碎片和冗余复制。
- vLLM 论文在评测负载中报告吞吐提升 2-4 倍，但该结果不应直接套到所有业务场景。

**简历口径**

- 写“接入 vLLM 优化推理吞吐与 KV Cache 显存利用”即可；具体倍数留给有压测数据时再说。

**参考**

- Efficient Memory Management for Large Language Model Serving with PagedAttention: https://arxiv.org/abs/2309.06180

### 4.9 FastAPI 流式响应与线程池

**正确口径**

- FastAPI 的 `StreamingResponse` 支持 async generator 或普通 generator/iterator，用于流式返回响应体。
- Starlette/FastAPI 会在多种场景使用线程池运行同步代码，以避免阻塞事件循环。
- 线程池不是无限资源，过度使用也会带来性能和内存成本。

**简历口径**

- “使用 FastAPI 封装服务接口”放简历即可；“流式响应、同步阻塞隔离、生命周期管理”更适合面试追问展开。

**参考**

- FastAPI StreamingResponse: https://fastapi.tiangolo.com/advanced/custom-response/
- Starlette Thread Pool: https://www.starlette.io/threadpool/

## 5. 面试知识清单

### 5.1 大模型基础

**必会问题**

- Transformer 为什么能并行？因为不依赖逐步递归，序列 token 之间通过注意力矩阵建模。
- Self-Attention 怎么算？Q/K/V 线性映射，`QK^T` 得注意力分数，除以 `sqrt(d_k)` 缩放，softmax 得权重，再乘 V。
- 多头注意力有什么用？多个 head 学不同关系子空间，最后拼接并线性变换。
- 位置编码解决什么？Attention 本身对顺序不敏感，需要注入位置信息。
- Lost in the Middle 是什么？长上下文中，模型对中间位置相关信息的利用可能弱于开头和结尾。

**回答模板**

> Transformer 的核心是用注意力机制替代循环结构。Self-Attention 会把输入映射成 Q、K、V，通过 `softmax(QK^T / sqrt(d_k))V` 得到每个 token 对其他 token 的加权表示。多头注意力让模型从多个子空间捕捉关系，位置编码补足序列顺序信息。工程上我会关注上下文长度、Token 成本和 Lost in the Middle，因此在多轮客服对话里用结构化状态追踪减少关键信息丢失。

### 5.2 RAG 工程

**必会问题**

- RAG 三阶段：检索、增强、生成。
- RAG 解决什么：外部知识接入、私有数据问答、知识更新、可追溯性。
- RAG 不能解决什么：检索错、上下文污染、模型推理错都会导致错误回答。
- 如何优化检索：语义切块、Overlap、父子文档、Embedding 选型、Query 改写、混合检索、Rerank、阈值拒答。
- 如何评估：Context Recall、Faithfulness、Answer Relevancy、Execution Accuracy、人工采纳率、Bad Case 分类。

**追问卡片**

- 文档切块：优先按标题、段落、业务实体切，不要只按固定长度；保留 10%-20% overlap。
- Query 改写：短 Query 或口语 Query 可扩展成多个更完整的检索意图。
- 混合检索：Dense 负责语义，Sparse/BM25 负责精确词。
- RRF：按排名融合多路召回，适合分数不可直接比较的检索器。
- Rerank：Cross-Encoder 对 Query 和候选文档做更精细相关性判断。
- 阈值拒答：相似度过低时不要硬答，返回信息不足或转人工。

### 5.3 Milvus 与向量数据库

**必会问题**

- 向量数据库做什么：存储 embedding，支持相似度检索。
- 常见距离：Cosine、Inner Product、L2。
- HNSW 适合什么：追求低延迟、高召回，且内存较充足的场景。
- 标量过滤怎么用：先按时间、类别、状态等元数据缩小范围，再做向量检索。
- 版本管理怎么做：元数据记录 `version/effective_date/status/source`，检索时过滤 `active`，保留旧版本便于审计和回滚。

**回答模板**

> 我选择索引时会看数据量、向量维度、内存、延迟和召回要求。比如问答系统希望秒级响应且数据量在十万到百万级时，可以考虑 HNSW；如果要按月份、药品类别或知识状态过滤，我会用 Milvus 标量过滤先缩小候选范围，再做向量相似度检索。

### 5.4 微调：LoRA 与 QLoRA

**必会问题**

- LoRA 原理：冻结原模型，在部分线性层加入低秩矩阵，只训练增量参数。
- rank 怎么选：从小到大实验，简单任务 r=8/16，复杂任务可尝试 32/64；实际看验证集。
- target modules 怎么选：可从 `q_proj/v_proj` 开始，欠拟合再扩展到 `k_proj/o_proj` 或 MLP。
- LoRA vs RAG：RAG 解决知识接入，LoRA 更适合行为、格式、语气、任务模式学习。
- QLoRA：4-bit 量化基座模型，梯度回传到 LoRA，结合 NF4、双重量化、分页优化器节省显存。

**回答模板**

> RAG 更像给模型外挂知识库，不改模型参数，适合私有知识、实时知识和需要溯源的场景。LoRA 是参数高效微调，适合让模型学会特定输出格式、对话风格或任务行为。实际项目里二者经常结合：RAG 提供事实知识，LoRA 让模型更会使用这些上下文并遵循业务话术。

### 5.5 推理与部署

**必会问题**

- vLLM 为什么快：PagedAttention 更高效管理 KV Cache，连续批处理提升吞吐。
- KV Cache 是什么：缓存历史 token 的 Key/Value，避免每步重复计算。
- 显存 OOM 怎么排查：看模型大小、上下文长度、batch、并发、KV Cache、量化、显存碎片。
- FastAPI 异步坑：同步 IO 放在 `async def` 里会阻塞事件循环。
- SSE/流式输出：用 `StreamingResponse` 或 SSE 协议逐步返回 token，避免用户长时间等待。

**回答模板**

> 大模型服务的瓶颈常在 KV Cache 和并发调度。vLLM 的 PagedAttention 借鉴分页内存管理，降低 KV Cache 碎片和冗余复制；同时通过连续批处理提升 GPU 利用率。落地时我不会直接承诺固定倍数，而是根据序列长度、并发和延迟目标做压测调参。

### 5.6 Dify 与 LangChain

**必会问题**

- Dify 优势：可视化 Workflow/Chatflow、知识库、工具接入、快速原型和迭代。
- LangChain 优势：代码级灵活、适合复杂定制和精细控制。
- 如何选择：快速业务验证用 Dify；复杂定制、强控制、深度集成用代码框架。

**回答模板**

> 我会根据项目阶段选择工具。原型验证和业务流程编排阶段，Dify 的知识库和 Workflow 可以快速落地；当流程需要复杂状态管理、定制检索策略或深度后端集成时，LangChain 或自研服务更适合做细粒度控制。

## 6. 项目复盘卡片

### 6.1 小啄 GPT 智能回复模型

- 背景：家电客服场景，多轮对话需要收集故障现象、设备信息、预约信息。
- 问题：上下文过长、关键信息丢失、回复流程不可控、商品/促销/维修知识更新快。
- 方案：Qwen 微调 + 动态指令注入 + 三层记忆管理 + DST 状态追踪 + RAG 知识库。
- 指标：Hit Rate +20% 仅在项目测试口径确认后使用；否则说“改善长尾 Query 召回”。
- 面试追问：
  - 多轮对话如何避免上下文丢失？
  - 为什么用结构化状态而不是只靠历史对话？
  - 混合检索怎么融合？
  - 如何处理模型幻觉？

**一分钟回答**

> 这个项目的核心不是简单调用大模型，而是让客服对话可控。我主要解决两类问题：一是长轮次对话里关键信息丢失，所以设计了短期窗口、长期摘要和结构化状态追踪，用 JSON 维护家电类型、故障现象、预约时间等槽位，并动态注入 Prompt；二是商品手册、维修手册里型号和故障码很多，单纯向量检索不稳，所以做了 Dense + BM25 的双路召回，再用 RRF 融合和 Rerank 精排，提高长尾问题的检索质量。

### 6.2 智能家电识别与自动入库系统

- 背景：根据图片/OCR 识别家电产品，补齐产品信息并自动入库。
- 问题：OCR 结果不完整、联网信息噪声大、字段不规范、重复入库。
- 方案：Docker/Miniconda 环境隔离；OCR/视觉模型识别；联网搜索补全；字段校验；向量相似度去重；FastAPI 封装接口。
- 指标：如无压测，不写具体吞吐提升倍数。
- 面试追问：
  - OCR 识别错怎么办？
  - 多 Agent 怎么分工？
  - 如何去重？
  - vLLM 如何控制显存？

**一分钟回答**

> 这个系统的目标是把图片或 OCR 文本转成可入库的结构化产品信息。我参与了模型环境部署、Dify 多 Agent 流程设计和 FastAPI 接口封装。流程上先由 OCR/视觉模型识别基础信息，再调用联网搜索补齐品牌、型号和规格，随后用 Prompt 约束字段格式，用规则和向量相似度做去重，最后自动入库。工程上用 Docker/Miniconda 做环境隔离，并接入 vLLM 优化推理服务。

### 6.3 智能数据分析问答助手

- 背景：医药采购、零售、库存数据表复杂，业务人员希望自然语言查询。
- 问题：专业术语召回不准、多表关联复杂、LLM 容易生成错误 SQL 或编造字段。
- 方案：Dify/LangChain 工程化部署；Milvus 知识库；Schema 元数据增强；问题分类；样例对；CoT；SQL 试执行与 Self-Correction；RAGAS/Execution Accuracy 评估。
- 指标：SQL 70% -> 90%+、500 条 Golden Dataset 均需确认真实口径。
- 面试追问：
  - Text-to-SQL 最难的点是什么？
  - 如何评估 SQL 是否正确？
  - 如何避免查错库存/销售额？
  - Dify 和 LangChain 怎么分工？

**一分钟回答**

> 这个项目面向医药供应链数据问答，核心是把自然语言问题转成可靠 SQL。我负责 LLM 应用架构、RAG 知识库和 Text-to-SQL 质量优化。检索层面，我没有只把表名丢进向量库，而是把表名、字段名、字段含义和枚举值做成富文本再向量化，并结合 Milvus 标量过滤提升召回。生成层面，我通过问题分类、样例对和约束 Prompt 引导 SQL 生成，再用 SQL 试执行捕获 MySQL 报错，让模型自修正，最后结合 Golden Dataset 和 RAGAS/Execution Accuracy 做离线评估。

## 7. 面试前 30 分钟速查清单

### 7.1 必背项目亮点

- 小啄 GPT：三层记忆 + DST 状态追踪 + 混合检索。
- 家电识别入库：OCR/视觉模型 + 联网补全 + 向量去重 + FastAPI 封装。
- 数据分析问答：Schema 元数据增强 + Text-to-SQL 自修正 + RAGAS/Execution Accuracy 评估。

### 7.2 必背技术关键词

- Transformer: Q/K/V、Scaled Dot-Product Attention、多头、位置编码。
- RAG: Chunking、Embedding、Milvus、BM25、RRF、Rerank、阈值拒答、Bad Case 回流。
- LoRA: 冻结基座、低秩矩阵、rank、target modules、与 RAG 的适用边界。
- QLoRA: 4-bit NF4、双重量化、分页优化器。
- vLLM: PagedAttention、KV Cache、连续批处理、吞吐与延迟权衡。
- FastAPI: async/sync 边界、StreamingResponse、线程池、lifespan。

### 7.3 三个高频追问的短答

**为什么选择 Qwen？**

> 主要看业务匹配度、中文能力、开源生态和工程落地成本。Qwen 在 HuggingFace、PEFT、vLLM 等工程链路中的支持较成熟，方便做微调实验、推理部署和后续维护。

**RAG 和微调怎么选？**

> RAG 适合知识接入和更新，尤其是私有知识、实时知识和需要溯源的问答；微调适合模型行为、格式、语气和任务模式学习。真实项目里常组合使用：RAG 提供事实依据，微调或 Prompt 让模型更会按业务规则回答。

**如何防止幻觉？**

> 我会从三层做：检索层设置相似度阈值和拒答；Prompt 层约束只能基于上下文或 Schema 回答；执行层对 SQL 先试执行和结果校验，再通过 Bad Case 回流优化知识库和 Prompt。

### 7.4 面试中慎说的话

- 不说“RAG 解决幻觉”，说“RAG 降低无依据回答风险，但需要评估和约束”。
- 不说“vLLM 一定提升几倍”，说“论文报告 2-4 倍，项目里需压测确认”。
- 不说“LoRA 几乎等于全量微调”，说“在合适 rank 和高质量数据下可接近全量微调效果”。
- 不说“我实现了 K8s/Celery/Nginx 高可用”，除非你确实在项目里做过。
- 不说“工程师招聘成本下降 10%”，除非你能把指标和项目业务链路讲清楚。

## 8. 参考资料

- Attention Is All You Need: https://arxiv.org/abs/1706.03762
- Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks: https://arxiv.org/abs/2005.11401
- LoRA: Low-Rank Adaptation of Large Language Models: https://arxiv.org/abs/2106.09685
- QLoRA: Efficient Finetuning of Quantized LLMs: https://arxiv.org/abs/2305.14314
- Efficient Memory Management for Large Language Model Serving with PagedAttention: https://arxiv.org/abs/2309.06180
- Lost in the Middle: How Language Models Use Long Contexts: https://arxiv.org/abs/2307.03172
- Milvus Index Vector Fields: https://milvus.io/docs/index-vector-fields.md
- Milvus Filtered Search: https://milvus.io/docs/filtered-search.md
- RAGAS Faithfulness: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/
- RAGAS Context Recall: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/
- FastAPI Custom Response and StreamingResponse: https://fastapi.tiangolo.com/advanced/custom-response/
- Starlette Thread Pool: https://www.starlette.io/threadpool/
- Dify Knowledge: https://docs.dify.ai/en/guides/knowledge-base
