# Aria2 Pro Docker

```bash
# 拉取镜像
docker pull p3terx/aria2-pro

# 配置文件目录
mkdir -p /data/.config/aria2
# 创建目录
mkdir -p /data/download

# 启动
docker run -d \
    --name aria2-pro \
    --restart unless-stopped \
    --log-opt max-size=1m \
    --network host \
    -e PUID=1000 \
    -e PGID=1000 \
    -e RPC_SECRET=<TOKEN> \
    -e RPC_PORT=6800 \
    -e LISTEN_PORT=6888 \
    -e DISK_CACHE=256M \
    -e IPV6_MODE=true \
    -v /data/.config/aria2:/config \
    -v /data/download:/downloads \
    p3terx/aria2-pro

# 防火墙
firewall-cmd --zone=public --permanent --add-port=6800/tcp
firewall-cmd --zone=public --permanent --add-port=6888/tcp
firewall-cmd --zone=public --permanent --add-port=6888/udp
firewall-cmd --reload

# 生成 service 文件 并写入systemd目录
podman generate systemd --name aria2-pro > /etc/systemd/system/aria2-pro.service

# 启动
systemctl start aria2-pro.service
systemctl enable aria2-pro.service

# AriaNg
# https://github.com/mayswind/AriaNg/releases/download/1.3.2/AriaNg-1.3.2.zip
```

## 选项参数说明

### Docker 基本选项

- `--name aria2-pro` - 容器名称，可自定义以示区分。
- `--restart unless-stopped` - 设置容器重启策略，详情参见 Docker 官方文档。
- `--log-driver json-file` - 设置日志记录格式为 json 格式。这是 Docker 的默认值，某些特殊情况可能需要设置。
- `--log-opt max-size=1m` - 日志大小限制为1MB，防止 Aria2 持续下载产生大量的日志占用磁盘空间。某些 GUI 可能没有相关选项。所以说有什么理由不用 CLI 一把梭？
- `--network host` - 使用 host 网络模式。直接使用宿主机网络，免去端口映射导致的部分性能损失，且灵活性更高，可更方便的配置使用 IPv6 网络。host 网络模式仅适用于 Docker 17.06+ ，如果你的 Docker 版本低于此，请先升级。

### 容器目录映射/挂载

- `-v $PWD/aria2-config:/config` - 配置目录映射，配置文件持久化。左边为宿主机路径供自定义，**不要有中文、不要混用配置文件，首次使用请确保目录为空**。
- `-v $PWD/aria2-downloads:/downloads` - 下载目录映射。左边为宿主机路径供自定义，**不要有中文**。

### 用户文件权限设置

- `-e PUID=$UID` - 用户映射。设置文件管理账户的UID(用户 ID)。忽略则默认为nobady用户，并权限最大化。
- `-e PGID=$GID` - 用户组映射。设置文件管理账户的GID(用户组 ID)。忽略则默认为nogroup用户组，并权限最大化。

### Aria2 配置选项环境变量

- `-e RPC_SECRET=<TOKEN>` - RPC 密钥设置，即 WebUI 连接时需要填写的密码，只建议使用字母和数字。如果没有设置，配置文件中的默认密码为P3TERX。
- `-e RPC_PORT=6800` - RPC 端口设置。
- `-e LISTEN_PORT=6888` - BT 监听端口（TCP）、DHT 监听端口（UDP）设置，即 Aria2 配置中listen-port与dht-listen-port选项定义的端口。如果没有设置，配置文件中的默认值为6888。
- `-e DISK_CACHE=<SIZE>` - 磁盘缓存设置，默认值64M。建议在有足够的内存空闲情况下设置为适当增加大小，以减少磁盘 I/O ，提升读写性能，延长硬盘寿命。比如128M、256M等。此项值仅决定上限，实际对内存的占用取决于网速(带宽)和设备性能等其它因素。当下载文件超过这个大小且网速足够快时最多会占用所设置大小的内存，所以不宜过大，设置不当轻则进程终结、重则宕机。
- `-e IPV6_MODE=true` - 开启 IPv6 模式。此变量等同于设定配置文件中的选项disable-ipv6=false与enable-dht6=true。可间接提升 BT 下载速率，但需要网络完整支持 IPv6 ，否则会导致部分功能异常，甚至无法下载。

### 其它环境变量

- `-e UPDATE_TRACKERS=false` - 禁用自动更新 BT tracker 。PT 下载和想手动填写设置 BT tracker 需求必须禁用。
- `-e CUSTOM_TRACKER_URL=<URL>` ：自定义 BT tracker 列表获取链接，多个链接可以用半角逗号(,)进行分隔。如果没有指定则默认从 `https://trackerslist.com/all_aria2.txt` 进行获取。
- `-e UMASK_SET=022` - umask 设置，默认值022。决定你下载下来的文件的权限，对权限不敏感或不理解直接填写000。
- `-e TZ=<TIME_ZONE>` - 时区设置，默认时区为Asia/Shanghai，若无特殊需求无需自定义。

### 网络模式

- `-p 6800:6800` - RPC 通讯端口映射。
- `-p 6888:6888` - BT 监听端口（TCP）映射，即 Aria2 配置中listen-port选项定义的端口。
- `-p 6888:6888/udp` - DHT 监听端口（UDP）映射，即 Aria2 配置中dht-listen-port选项定义的端口。
