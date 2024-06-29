# 镜像加速器

 自 2024-06-06 开始，中国境内的 Docker Hub 镜像加速器相继停止服务。
 需要使用代理等其他方式访问 Docker Hub。

- [阿里云](https://www.aliyun.com/product/acr?source=5176.11533457&userCode=8lx5zmtu) `(点击管理控制台 -> 登录账号(淘宝账号) -> 右侧镜像工具 -> 镜像加速器 -> 复制加速器地址)`
- [网易云](https://www.163yun.com/help/documents/56918246390157312) `https://hub-mirror.c.163.com`
- [百度云](https://cloud.baidu.com/doc/CCE/s/Yjxppt74z#%E4%BD%BF%E7%94%A8dockerhub%E5%8A%A0%E9%80%9F%E5%99%A8) `https://mirror.baidubce.com`

## 配置镜像加速器

### Docker

请首先执行以下命令，查看是否在 `docker.service` 文件中配置过镜像地址。

```bash
systemctl cat docker | grep '\-\-registry\-mirror'
```

如果该命令有输出，那么请执行 `systemctl cat docker` 查看 `ExecStart=` 出现的位置，修改对应的文件内容去掉 `--registry-mirror` 参数及其值，并按接下来的步骤进行配置。

如果以上命令没有任何输出，那么就可以在 `/etc/docker/daemon.json` 中写入如下内容（如果文件不存在请新建该文件）：

```json
{
  "registry-mirrors": [
    "https://hub-mirror.c.163.com",
    "https://mirror.baidubce.com"
  ]
}
```

注意，一定要保证该文件符合 `json` 规范，否则 `Docker` 将不能启动。
之后重新启动服务。

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

### Podman

1. 备份原配置文件
`cp /etc/containers/registries.conf /etc/containers/registries.conf.bak`
2. 修改配置文件
`vim /etc/containers/registries.conf`

```conf
# unqualified-search-registries
# 一组主机[:端口]注册表，按顺序在拉取不合格的镜像时尝试。
unqualified-search-registries = ["docker.io"]

# 命名[[registry]]空间设置

# prefix: 用户指定的镜像名称的前缀，即使用以下格式之一：

# host[:port]
# host[:port]/namespace[/namespace…]
# host[:port]/namespace[/namespace…]/repo
# host[:port]/namespace[/namespace…]/repo(:_tag|@digest)
# [*.]host

# location : 接受与前缀字段相同的格式，并指定以前缀为根的名称空间的物理位置。

# insecure : true or false. 默认情况下，容器运行时在从注册表中检索镜像时需要 TLS。
# 如果 insecure 被设置为 "true"，则允许未加密的 HTTP 以及带有不受信任的证书的 TLS 连接。

# blocked : true 或 false。禁止拉取具有匹配名称的图像。

## short-name-mode 选项支持三种模式来控制短名称解析的行为。
# enforcing 如果只设置了一个无限定搜索注册中心，则使用它，因为没有歧义。如果存在不止一个注册表并且用户程序正在终端中运行（即，stdout和stdin是TTY），提示用户选择指定的搜索注册表之一。如果程序不在终端中运行，则不能解决歧义，这将导致错误。
# permissive 如果程序不在终端上运行，则表现为强制，但不会导致错误。相反，回退到使用所有不合格搜索注册中心。
# disabled 使用所有未限定搜索注册表而不提示。

short-name-mode = "enforcing"

[[registry]]
prefix = "docker.io"
insecure = false
blocked = false
location = "docker.io"

# [[registry.mirror]]
# location = "docker.mirrors.ustc.edu.cn"

[[registry.mirror]]
location = "hub-mirror.c.163.com"

[[registry.mirror]]
location = "mirror.baidubce.com"
```

- 手册页：[registries.conf.5](https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md)

## 检查加速器是否生效

执行 `docker info`，如果从结果中看到了如下内容，说明配置成功。

```text
Registry Mirrors:
    https://hub-mirror.c.163.com/
```

## 参考文献

- [镜像加速器](https://yeasy.gitbook.io/docker_practice/install/mirror)