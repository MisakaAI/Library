# 基本概念

## 镜像（Image）

**Docker 镜像** 是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像 不包含 任何动态数据，其内容在构建之后也不会被改变。

### 分层存储

镜像包含操作系统完整的 root 文件系统，其体积往往是庞大的。
在 Docker 设计时，利用 Union FS 的技术，将其设计为分层存储的架构。
镜像多层文件系统联合组成。

镜像构建时，会一层层构建，前一层是后一层的基础。
每一层构建完就不会再发生改变，后一层上的任何改变只发生在自己这一层。

分层存储的特征使得镜像的复用、定制变的更为容易。

## 容器（Container）

容器是镜像运行时的实体。
容器可以被创建、启动、停止、删除、暂停等。

容器的实质是进程，但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的[命名空间](https://en.wikipedia.org/wiki/Linux_namespaces)。
容器可以拥有自己的 root 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。

容器运行时读写而准备的存储层为**容器存储层**
容器消亡时，容器存储层也随之消亡。

容器不应该向其存储层内写入任何数据，容器存储层要保持无状态化。
所有的文件写入操作，都应该使用 数据卷（Volume）、或者 绑定宿主目录。

数据卷的生存周期独立于容器，容器消亡，数据卷不会消亡。

## 仓库（Repository)

一个 Docker Registry 中可以包含多个 仓库（Repository）
每个仓库可以包含多个 标签（Tag）
每个标签对应一个镜像。

Docker Registry 公开服务是开放给用户使用、允许用户管理镜像的 Registry 服务。
一般这类公开服务允许用户免费上传、下载公开的镜像，并可能提供收费服务供用户管理私有镜像。

### 镜像加速

在国内访问这些服务可能会比较慢。
国内的一些云服务商提供了针对 Docker Hub 的镜像服务（Registry Mirror），这些镜像服务被称为 加速器。

- **阿里云** [容器镜像服务 ACR](https://cn.aliyun.com/product/acr?from_alibabacloud=&source=5176.11533457&userCode=8lx5zmtu)

## 参考文献

- [镜像](https://yeasy.gitbook.io/docker_practice/basic_concept/image)
- [容器](https://yeasy.gitbook.io/docker_practice/basic_concept/container)
- [仓库](https://yeasy.gitbook.io/docker_practice/basic_concept/repository)
