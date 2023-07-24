# 定制镜像

镜像的定制实际上就是定制每一层所添加的配置、文件。
如果我们可以把每一层修改、安装、构建、操作的命令都写入一个脚本，用这个脚本来构建、定制镜像。
那么之前提及的无法重复的问题、镜像构建透明性的问题、体积的问题就都会解决。
这个脚本就是 `Dockerfile`

```bash
# FROM 指定基础镜像
FROM ubuntu:22:04

# RUN 执行命令
RUN sed -i "s@http://.*archive.ubuntu.com@http://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list \
    && sed -i "s@http://.*security.ubuntu.com@http://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list \
    && apt update && apt upgrade -y \
    && apt install -y aria2 unzip \
    && apt clean && apt autoclean \
    && mkdir /etc/aria2

COPY 
# EXPOSE 声明容器运行时提供服务的端口，这只是一个声明，在容器运行时并不会因为这个声明应用就会开启这个端口的服务。
EXPOSE 6800
# CMD 容器启动命令
CMD /usr/bin/aria2c --conf-path=/etc/aria2/aria2.conf

```

## 参考文献

- [使用 Dockerfile 定制镜像](https://yeasy.gitbook.io/docker_practice/image/build)
- [Dockerfile 指令详解](https://yeasy.gitbook.io/docker_practice/image/dockerfile)
- [Dockerfile 多阶段构建](https://yeasy.gitbook.io/docker_practice/image/multistage-builds)