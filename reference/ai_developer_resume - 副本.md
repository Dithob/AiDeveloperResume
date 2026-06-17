李鱼皮

男

｜24 岁｜

Java 后端开发（具备 AI Agent 全栈开发经验）｜3 年工作经验

手机：138xxxx8888｜邮箱：yupi@codefather.cn | 微信：xxxxxx

个人博客（作品集）：dogyupi.com | GitHub：github.com/liyupi

教育经历

XX大学

软件工程

本科 ｜ 排名:前 5% 通过 CET-6

2019-09 ~ 2023-06

上海市挑战杯特等奖 | 上海市优秀毕业生 | 国家级创新创业项目负责人 | 蓝桥杯 Java 组省一等奖 | 软件设计师认证

专业技能

**开发技术**

-  掌握 Java8~26 新特性，熟悉集合框架、反射、动态代理等核心机制，能运用 Hutool、Lombok 等工具库提高开发效率 
- 掌握 Spring Boot3+MyBatis-Plus 独立开发后端项目，熟悉 Spring Cloud 微服务全家桶，能独立完成微服务项目的拆分和治理 
- 熟悉 MySQL 数据库设计和 SQL 调优，实践过分库分表、索引优化,能使用 Druid 进行 SQL 监控和慢查询分析 
- 熟悉 Redis 缓存中间件，实践过 Caffeine 多级缓存架构、分布式锁、缓存雪崩/穿透解决方案、哨兵集群搭建 
- 熟悉 Docker 容器化和 Nginx 反向代理部署，能编写 Dockerfile 打包项目并通过 Serverless 平台快速上线 
- 熟悉 Prometheus + Grafana + 阿里云 ARMS 监控告警体系，能构建从网关到数据库的全链路追踪和 JVM 诊断大盘 
- 掌握 SEO 搜索引擎优化和 GEO 生成式引擎优化，能通过结构化内容和 TDK 优化等手段提升搜索收录和 AI 推荐排名

 **AI应用开发**

-  熟悉 Spring AI、LangChain4j 等 AI 开发框架，独立开发过涉及 RAG、工具调用、MCP、多 Agent 协作的企业级 AI 智能体应用 
- 掌握 Prompt 工程和优化技巧，能基于 PGvector 向量数据库构建 RAG 知识库，实现文档 ETL、向量检索和查询增强的完整流程 
- 能利用 Cursor / Claude Code / GitHub Copilot 等 AI 编程工具高效开发全栈项目，掌握 MCP Server 和 Agent Skills 的开发和发布 
- 熟悉 Vibe Coding、SDD、Harness Engineering 等多种 AI 编程模式，能利用 Spec-Kit、OpenSpec 等工具驱动 AI 完成大型项目

工作经历

老鱼公司 ｜ Java后端 + AI 应用开发

2023-04 ~ 至今

负责产品：编程导航 [codefather.cn](https://codefather.cn/) (日活 20K 的程序员学习社区)、面试鸭 [mianshiya.com](https://www.mianshiya.com/) (日活 15K 的面试刷题平台) 

- 独立完成从需求分析、架构设计、后端开发到部署上线的全流程，并搭建监控体系，支撑共计日均 PV 35K+ 产品的稳定运行 
- 主导统一支付中心从 0 到 1 的设计和研发，基于策略模式 + 工厂模式屏蔽微信 / 支付宝 / Apple 底层差异，支持 Web / H5 / 小程序 / App 四端支付，新业务线可在 **2 小时内** 完成接入 
- 设计类语雀风格的多级目录知识库体系，支持文字教程、视频教程等核心内容的结构化阅读，兼容 Web / 小程序 / App 多端访问 
- 主导 AI 方向技术选型和落地，将大模型能力融入现有业务系统，如 RAG 知识库问答、AI 互动式学习、三层内容风控审核，UGC 违规内容拦截率提升至 **98%**
- 基于 ElasticSearch + IK 分词构建全站聚合搜索引擎，设计复合评分算法融合关键词匹配、热度权重和时间衰减因子，搜索结果点击率提升 **35%** 
- 负责平台可观测性建设，集成阿里云 ARMS 构建 APM 监控体系，利用 TraceID 实现分布式链路追踪，系统故障发现时间从小时级缩短至 **分钟级**

项目经历

AI 超级智能体(AI Agent 项目)

在线访问：[codefather.cn](https://codefather.cn/)   GitHub 开源：[github.com/liyupi/yu-ai-agent ](https://github.com/liyupi/yu-ai-agent)

**项目介绍**：基于 Spring Boot3 + Spring AI + RAG + Tool Calling + MCP 的企业级 AI 智能体。支持多轮对话、记忆持久化、RAG 知识库检索，基于 ReAct 模式能够自主思考并调用工具完成复杂任务，如利用联网搜索、资源下载和 PDF 生成工具制定完整计划并生成文档。 

**主要工作：** 

1. 利用 Spring AI 框架接入通义、Ollama 等 5 种 AI大模型，封装统一调用接口实现灵活切换，通过 Ollama 本地部署处理简单对话，API 调用成本降低 **60%** 
2. 通过 Spring AI 的 ChatMemory + Advisor 实现多轮对话记忆，并自实现了基于 MySQL + Redis + Kryo 高性能序列化的记忆持久化方案，服务重启后对话上下文恢复率达 **99%** 以上 
3. 基于 Spring AI 构建完整的 RAG 知识库,实现文档 ETL处理、PGvector 向量存储、自动元信息标注、多查询扩展和查询重写，知识问答准确率相比纯大模型提升 **45%** 
4. 利用 Spring AI 的 @Tool 注解实现了联网搜索、网页抓取、PDF 生成、资源下载等 6 种工具调用，并基于单例模式实现集中式工具注册管理；通过 ToolContext 上下文传递用户身份信息，结合参数校验防止工具调用幻觉导致的无效执行 
5. 利用 Spring AI 开发了图片搜索 MCP 服务，实现 Stdio 和 SSE 双传输模式并以 Serverless 方式部署，便于其他 AI 项目接入 
6. 参考 OpenManus 实现了支持 Human-in-the-Loop 的分层智能体架构，并通过最大步骤限制、状态管理和死循环检测保障稳定运行 
7. 使用 SseEmitter + CompletableFuture 实现 SSE 流式 AI接口，将推理任务异步化，实时输出智能体思考和执行过程，用户等待感知时间减少 **80%；**并通过自定义 SSE 数据封装格式，解决流式传输中换行符和特殊字符丢失问题

AI 热点监控工具(AI 应用开发项目)

在线访问：[codefather.cn](https://codefather.cn/)   GitHub 开源：[github.com/liyupi/yupi-hot-monitor ](https://github.com/liyupi/yupi-hot-monitor)

**项目介绍**：基于 Express5+React 19 + OpenRouter + Socket.io 的 AI 驱动热点监控工具。支持多数据源聚合采集、AI 内容审核、WebSocket 实时推送,并将热点监控能力封装为 Agent Skills,支持在 Cursor、GitHub Copilot 等多种 AI 编程工具中复用。 

**主要工作：**

1. 使用 GitHub Copilot + MCP + Agent Skills 进行 AI 辅助开发,遵循企业级 AI 工程流程,通过 Git 保障每个迭代的可回滚性,项目中 **90%** 以上的代码由 AI 生成,大幅提高开发效率 
2. 基于 Axios + Cheerio 实现了 Bing、HackerNews、B 站等 8+ 搜索引擎的爬虫采集,同时通过第三方 API 对接 Twitter 高级搜索,经人工标注样本对比验证,信息覆盖面相比单一来源提升 **5 倍以上** 
3. 通过 OpenRouter 接入 AI大模型,设计了结构化分析 Prompt,对采集内容进行真实性验证、相关性评分、重要性分级和智能摘要生成,经人工标注数据对比测试,AI 过滤准确率达 **90%** 以上 
4. 利用 AI 大模型实现查询扩展,将用户输入的关键词自动扩展为 5 ~ 15 个语义变体以提升搜索召回率,信息召回率提升 **300%** 以上;同时通过本地缓存机制避免重复调用,节省 AI 调用成本 
5. 基于 Socket.io 实现了事件驱动的关键词订阅机制,当后台采集到新热点时实时推送给已订阅的客户端,实现毫秒级通知 
6. 利用 Skill Creator 将热点监控能力封装为标准化的 Agent Skills 技能包，实现和 10+ 主流 AI 编程工具的集成，无需后端服务即可开箱使用

其他个人作品

可以在我的作品集中查看详情 [dogyupi.com](http://dogyupi.com/) 

1. AI 万能视频下载总结器：基于 FastAPI + yt-dlp + DeepSeek，实现了主流平台的视频下载和 AI 内容总结，集成 Stripe 国际支付 
2. AI 零代码应用生成平台：基于 Spring Cloud + LangGraph4j 工作流，实现了多 Agent 协作自动生成完整项目代码和部署访问 
3. AI 爆款文章创作器：基于 Spring AI Alibaba + StateGraph，实现了 5 智能体协作 + 三阶段人机协作的全流程图文自动创作
4. 手写 RPC 框架(技术轮子)：基于 Etcd + Vert.x + SPI 机制，实现了自定义网络协议、多种负载均衡策略和重试容错机制

个人优势

1. 具备 **AI Agent 全栈开发能力**，从需求分析、架构设计、AI应用开发、前端界面到部署运维均能独立完成，已上线 **10+** 个可访问产品 
2. 热爱开源，在 GitHub 独立创作 **20+** 开源项目，收获 **2 万+** Followers，其中 AI知识库 [github.com/liyupi/ai-guide](https://github.com/liyupi/ai-guide) 的 Star 突破 **1 万** 
3. 具备产品商业化能力，熟悉百度统计、友盟等数据分析平台，独立完成过产品内微信支付和 Stripe 国际支付的对接和上线运营 
4. 自主学习能力强，能独立阅读 Spring AI 等官方文档快速掌握新技术；善于利用 Claude Code 等 AI 工具辅助学习；还借助了 OpenClaw 持续跟进 AI大模型、Agent Skills 生态的最新发展