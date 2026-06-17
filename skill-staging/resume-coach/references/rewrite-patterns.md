# Resume Rewrite Patterns

Use this reference when rewriting bullets, summaries, skills, work experience, project entries, or self-evaluation lines.

## Evidence-first editing

Before rewriting, identify:

- What the candidate actually did
- What problem or constraint existed
- What technology, method, or decision was used
- What changed afterward
- What proof exists: metric, link, user count, benchmark, award, review, deployment, demo, or artifact

If a bullet lacks evidence, ask for it or write a conservative version.

## Bullet formulas

Use these as flexible patterns, not rigid templates.

### STAR

`在 [场景] 下，承担 [任务]，通过 [行动/技术]，取得 [结果]。`

### CAR

`面对 [挑战]，采用 [行动/方案]，带来 [结果/收益]。`

### Technical depth

`基于 [技术栈] 设计/实现 [模块]，解决 [具体问题]，并通过 [验证方式] 达到 [结果]。`

### Ownership

`负责/主导 [系统/模块] 的 [设计/开发/优化/上线]，覆盖 [范围]，支撑 [规模/场景]。`

### English version

`Built/led/optimized [system or feature] using [technology/method] to solve [problem], resulting in [measurable outcome].`

## Action verbs

Chinese:

- 负责
- 主导
- 设计
- 实现
- 重构
- 优化
- 接入
- 搭建
- 迁移
- 上线
- 排查
- 沉淀
- 推动
- 支撑

English:

- Built
- Led
- Designed
- Implemented
- Optimized
- Refactored
- Migrated
- Integrated
- Deployed
- Automated
- Diagnosed
- Reduced
- Improved
- Scaled

Use stronger verbs only when the user's facts support them. Do not change `参与` into `主导` unless ownership is confirmed.

## Weak-to-strong examples

Weak:

`参与系统开发。`

Stronger:

`负责 Spring Boot 前后端分离系统的订单查询模块开发，完成接口设计、数据分页查询和异常处理，支撑后台运营人员按订单状态快速检索。`

Evidence still needed:

- System scale
- Performance or usage metric
- Link or deployment proof

Weak:

`使用 Redis 优化性能。`

Stronger:

`针对热点数据重复查询问题，引入 Redis 缓存并设计过期策略，降低数据库读取压力；如有压测数据，可补充 QPS、响应时间或数据库查询次数变化。`

Weak:

`熟悉 AI 工具。`

Stronger:

`在 XX 项目中使用 AI 编程工具辅助需求拆解、方案设计和单元测试编写，并通过人工 review、测试和部署验证保证交付质量。`

Only use the stronger version if those steps actually happened.

## Skills section patterns

Prefer category bullets:

- `后端开发：熟悉 Java、Spring Boot 和 RESTful API 设计，能独立完成业务模块开发、异常处理和接口调试。`
- `数据库与缓存：熟悉 MySQL 索引优化、事务和慢 SQL 排查，了解 Redis 缓存策略与常见一致性问题。`
- `AI 应用：了解 RAG、MCP、Agent 和向量检索流程，完成过 [项目名称] 中的 [真实模块]。`

Do not overstate depth. Use `熟悉`, `掌握`, `了解`, and `实践过` consistently.

## Project entry pattern

Recommended order:

1. Project name and role
2. One-line project context
3. Tech stack
4. Personal contribution bullets
5. Results, proof, links, or demo

Keep the context line short:

`一个基于 Vue3 + Spring Boot 的在线题库系统，支持题目管理、刷题记录和用户权限管理。`

Then spend most space on contribution:

- `负责题目检索模块，基于 MySQL 索引和分页查询优化列表加载，减少大数据量下的查询等待。`
- `设计用户权限校验流程，结合拦截器统一处理登录态和接口权限，降低重复鉴权代码。`

## Self-evaluation pattern

Only include self-evaluation when backed by proof.

Weak:

`学习能力强，热爱编程，善于沟通。`

Stronger:

`学习能力强：独立阅读 Spring AI 官方文档并完成 RAG 问答 Demo，沉淀技术笔记 X 篇。`

If proof is absent, remove the section.

## Metrics

Good metrics can include:

- QPS, latency, error rate, memory, CPU
- Cost reduction
- User count, DAU, PV, retention
- Revenue, conversion, registration
- Number of documents, tests, modules, APIs, issues, PRs
- Delivery time reduction

Never invent metrics. When the user has no metric, suggest what could be measured or write the impact qualitatively.

## Cleanup rules

- Remove `我`, `本人`, and excessive subjective adjectives.
- Replace vague words like `负责一些`, `参与部分`, `优化了性能`, `提高效率` with concrete scope.
- Keep bullet length controlled; one bullet should usually express one achievement or contribution.
- Avoid unexplained abbreviations unless common in the target field.
- Keep technology capitalization consistent.
