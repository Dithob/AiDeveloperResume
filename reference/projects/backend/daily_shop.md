# 天天购物平台（电商微服务）

> 岗位适配：**首选** 后端开发（Java / 微服务方向）、全栈；**次选** 后端 + AI 应用研发

> 理由：Spring Cloud 全家桶 + Sentinel 限流熔断 + Seata 分布式事务 + 容器化部署，覆盖微服务治理全链路，后端岗核心项目；与小麦购票同质（均含 Redis 库存 + 消息解耦），择一投递即可。

- **时间**：2025.06--2025.08
- **角色**：后端开发
- **技术栈**：Spring Cloud、Nacos、Spring Cloud Gateway、OpenFeign、RabbitMQ、Sentinel、Seata、Redis、Redisson、Docker

## 项目简介

基于 Spring Cloud、Nacos、Spring Cloud Gateway、OpenFeign、RabbitMQ、Sentinel、Seata、Redis 与 Redisson 构建类似天猫的电商微服务系统，包含商品展示、搜索、购物车、下单和支付等核心功能。

## 主要工作

- **微服务架构与治理**：使用 Nacos 完成服务注册发现与配置管理，基于 OpenFeign 实现服务间调用，通过 Gateway 统一路由和请求过滤；接入 Sentinel 完成流量控制与熔断降级，提升高并发场景下服务稳定性。
- **性能与异步解耦**：使用 Redis 缓存购物车和热点商品数据，将购物车访问耗时由 119ms 优化至 28ms，商品详情访问耗时由 86ms 优化至 17ms；使用 RabbitMQ 解耦下单/支付流程，通过补偿机制将用户感知支付时间由 3s 降至 0.5s 内。
- **一致性与部署**：使用 Redisson 分布式锁处理库存扣减，防止高并发超卖；使用 Seata AT 模式处理跨服务分布式事务，并通过 Docker 完成服务容器化部署，降低环境差异带来的发布风险。
