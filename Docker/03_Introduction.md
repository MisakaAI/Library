# Docker 简介

## 什么是Docker

Docker是一个开放源代码的开放平台软件，用于开发应用、交付（shipping）应用、运行应用。
Docker允许用户将基础设施（Infrastructure）中的应用单独分割出来，形成更小的颗粒（容器），从而提高交付软件的速度。

## 为什么要用 Docker

1. 更高效的利用系统资源
2. 更快速的启动时间
3. 一致的运行环境
4. 持续交付和部署
5. 更轻松的迁移
6. 更轻松的维护和扩展

### 对比传统虚拟机总结

特性|容器|虚拟机
-|-|-
启动|秒级|分钟级
硬盘使用|一般为`MB`|一般为`GB`
性能|接近原生|弱于
系统支持量|单机支持上千个容器|一般几十个

## 参考文献

- [什么是 Docker](https://yeasy.gitbook.io/docker_practice/introduction/what)
- [为什么要用 Docker](https://yeasy.gitbook.io/docker_practice/introduction/why)