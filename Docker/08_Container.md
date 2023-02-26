# 容器

**容器** 是独立运行的一个或一组应用，以及它们的运行环境。

**虚拟机** 可以理解为模拟运行的一整套操作系统和跑在上面的应用，虚拟机的操作系统提供了运行环境和其他系统环境。

## 启动

### 新建并启动

当利用 `docker run` 来创建容器时，Docker 在后台运行的标准操作包括：

- 检查本地是否存在指定的镜像，不存在就从 [registry](09_Repository.md) 下载
- 利用镜像创建并启动一个容器
- 分配一个文件系统，并在只读的镜像层外面挂载一层可读写层
- 从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中去
- 从地址池配置一个 ip 地址给容器
- 执行用户指定的应用程序
- 执行完毕后容器被终止

```bash
## 运行镜像
docker run -it ubuntu:22.04 bash
```

- `-d, --detach=false` 指定容器运行于前台还是后台，默认为false
- `-i, --interactive=false` 打开STDIN，用于控制台交互
- `-t, --tty=false` 分配tty设备，该可以支持终端登录，默认为false
- `-u, --user=""` 指定容器的用户 `<name|uid>[:<group|gid>]`
- `-a, --attach=[]` 登录容器（必须是以docker run -d启动的容器）
- `-w, --workdir=""` 指定容器的工作目录
- `-c, --cpu-shares=0` 设置容器CPU权重，在CPU共享场景使用
- `-e, --env=[]` 指定环境变量，容器中可以使用该环境变量
- `-m, --memory=""` 指定容器的内存上限
- `-P, --publish-all=false` 指定容器暴露的端口（随机分配一个端口）
- `-p, --publish=[]` 指定容器暴露的端口 [宿主机端口:容器端口]
- `-h, --hostname=""` 指定容器的主机名
- `-v, --volume=[]` 给容器挂载存储卷，挂载到容器的某个目录
- `--rm=false` 指定容器停止后自动删除容器(不支持以docker run -d启动的容器)
- `--name=""` 指定容器名字，后续可以通过名字进行容器管理，links特性需要使用名字
- `--volumes-from=[]` 给容器挂载其他容器上的卷，挂载到容器的某个目录
- `--device=[]` 添加主机设备给容器，相当于设备直通
- `--dns=[]` 指定容器的dns服务器
- `--dns-search=[]` 指定容器的dns搜索域名，写入到容器的 `/etc/resolv.conf` 文件
- `--env-file=[]` 指定环境变量文件，文件格式为每行一个环境变量
- `--link=[]` 指定容器间的关联，使用其他容器的IP、env等信息
- `--expose=[]` 指定容器暴露的端口，即修改镜像的暴露端口
- `--net="bridge"` 容器网络设置:
  - `bridge` 使用docker daemon指定的网桥
  - `host` 容器使用主机的网络
  - `container:NAME_or_ID` 使用其他容器的网路，共享IP和PORT等网络资源
  - `none` 容器使用自己的网络（类似--net=bridge），但是不进行配置
- `--restart="no"` 指定容器停止后的重启策略:
  - no：容器退出时不重启
  - on-failure：容器故障退出（返回值非零）时重启
  - always：容器退出时总是重启
- **ubuntu:22.04**
镜像名，一般使用`仓库名[:标签]`，这是一个缩写。
完整的镜像名为 `地址[:端口号]/]仓库名[:标签]`
- **bash** 执行的命令

## 控制容器状态

```bash
# 查看运行中容器的信息
# 使用 -a 参数可以查看所有容器的信息
docker container ls

# 获取容器的输出信息
docker container logs

# 终止一个运行中的容器
docker container stop

# 启动终止的容器
# 将一个已经终止（exited）的容器启动运行
docker container start

# 将一个运行态的容器终止，然后再重新启动它
docker container restart

# 删除容器
# 如果要删除一个运行中的容器，可以添加 -f 参数。
docker container rm ada5e335252d

# 清理所有处于终止状态的容器
docker container prune
```

## 后台运行 Daemon

`-d` 参数可以让 Docker 在后台运行而不是直接把执行命令的结果输出在当前宿主机下
如果不使用 `-d` 参数运行容器，容器会把输出的结果 (STDOUT) 打印到宿主机上面

容器是否会长久运行，是和 `docker run` 指定的命令有关，和 `-d` 参数无关

## 进入容器

在使用 `-d` 参数时，容器启动后会进入后台。

使用 `docker attach` 命令，可以进入容器。
如果从这个 `stdin` 中 `exit`，会导致容器的停止。

`docker exec -it` 也可以进入容器。
并且从这个 `stdin` 中 `exit`，不会导致容器的停止。

## 导入和导出

```bash
# 查看容器的 TAG
docker container ls -a

# 导出容器快照
docker export ada5e335252d > ubuntu.tar

# 导入容器快照
# 从容器快照文件中再导入为镜像
cat ubuntu.tar | docker import - test/ubuntu:v1.0

# 通过指定 URL 或者某个目录来导入
$ docker import http://example.com/exampleimage.tgz example/imagerepo
```
