# 使用镜像

- 从仓库获取镜像
- 管理本地主机上的镜像
- 介绍镜像实现的基本原理

## 获取镜像

```bash
# docker pull [选项] [镜像仓库地址[:端口号]/]仓库名[:标签]
docker pull ubuntu:22.04
```

### 运行

```bash
## 运行镜像
# -i 交互式
# -t 终端
# --rm 容器退出后随之将其删除
# ubuntu:22.04 镜像名
# bash 执行的命令
docker run -it --rm ubuntu:22.04 bash

# 查看系统信息
cat /etc/os-release
```

## 列出镜像

列出已经下载的镜像
列表包含了 `仓库名`、`标签`、`镜像 ID`、`创建时间` 以及 `所占用的空间`。

```bash
# 列出镜像
docker image ls
```

通过 `docker system df` 命令可以便捷的查看镜像、容器、数据卷所占用的空间。

### 虚悬镜像

镜像既没有仓库名，也没有标签，均为 \<none\>

一般来说，虚悬镜像已经失去了存在的价值，是可以随意删除的。

```bash
# 删除虚悬镜像
docker image prune
```

### 中间层镜像

为了加速镜像构建、重复利用资源，Docker 会利用 中间层镜像。
在使用一段时间后，可能会看到一些依赖的中间层镜像。
默认的 `docker image ls` 列表中只会显示顶层镜像。
希望显示包括中间层镜像在内的所有镜像的话，需要加 `-a` 参数

```bash
# 列出全部镜像
docker image ls -a
```

### 列出部分镜像

```bash
# 根据仓库名列出镜像
docker image ls ubuntu
# 列出特定的某个镜像 指定仓库名和标签
docker image ls ubuntu:22.04
```

### 以特定格式显示

- [格式化命令和日志输出](https://docs.docker.com/engine/cli/formatting/)
- [有效占位符](https://docs.docker.com/reference/cli/docker/image/ls/#format)

```bash
# 仅显示镜像ID
docker image ls -q
# 直接列出镜像结果，并且只包含镜像ID和仓库名
docker image ls --format "{{.ID}}: {{.Repository}}"
# 以表格等距显示，并且有标题行，和默认一样，不过自己定义列
docker image ls --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}"
```

## 删除本地镜像

```bash
# 删除本地镜像
# docker image rm [选项] <镜像1> [<镜像2> ...]

# 可以用镜像的完整 ID，也可以用短ID来删除
# 例如 5a2 为 IMAGE ID 的前3位（一般取前3个字符以上足够）
docker image rm 5a2

# 也可以用镜像名，也就是 <仓库名>:<标签>，来删除镜像。
docker image rm debian
```

## Commit

对容器进行修改后，将其保存下来形成镜像。

```bash
# docker commit [选项] <容器ID或容器名> [<仓库名>[:<标签>]]

# --author 修改的作者，可以省略
# --message 记录本次修改的内容，可以省略
# webserver 容器名
# nginx:v2 镜像名

docker commit \
    --author "Tao Wang <twang2218@gmail.com>" \
    --message "修改了默认网页" \
    webserver \
    nginx:v2
```

实际环境中不要使用 `Commit` 生成镜像，请使用 `Dockerfile` 定制镜像。
使用 `docker commit` 意味着所有对镜像的操作都是黑箱操作，生成的镜像也被称为 **黑箱镜像**
除了制作镜像的人之外，其他人不知道执行过什么命令、怎么生成的镜像。

## 参考文献

- [获取镜像](https://yeasy.gitbook.io/docker_practice/image/pull)
- [列出镜像](https://yeasy.gitbook.io/docker_practice/image/list)
- [删除本地镜像](https://yeasy.gitbook.io/docker_practice/image/rm)
- [利用 commit 理解镜像构成](https://yeasy.gitbook.io/docker_practice/image/commit)
- [其它制作镜像的方式](https://yeasy.gitbook.io/docker_practice/image/other)