# qBittorrent

专业磁力种子下载工具。

[github](https://github.com/linuxserver/docker-qbittorrent)
[docker](https://hub.docker.com/r/linuxserver/qbittorrent)

```bash
# 拉取镜像
docker pull linuxserver/qbittorrent

# 创建工作目录
mkdir -p /data/qbittorrent/downloads /data/qbittorrent/config

# 启动
# 本例中，使用 63739 为 BT客户端的 P2P 端口。
docker run -d \
    --name=qbittorrent \
    -e PUID=1000 \
    -e PGID=1000 \
    -e TZ=Asia/Shanghai \
    -e WEBUI_PORT=8080 \
    -e TORRENTING_PORT=63739 \
    -p 8080:8080 \
    -p 63739:63739 \
    -p 63739:63739/udp \
    -v /data/qbittorrent/config:/config \
    -v /data/qbittorrent/downloads:/downloads \
    --restart unless-stopped linuxserver/qbittorrent:latest

# 防火墙
firewall-cmd --zone=public --permanent --add-port=8080/tcp
firewall-cmd --zone=public --permanent --add-port=63739/tcp
firewall-cmd --zone=public --permanent --add-port=63739/tcp

firewall-cmd --reload

# 生成 service 文件 并写入systemd目录
podman generate systemd --name qbittorrent > /etc/systemd/system/qbittorrent.service

# 启动
systemctl start qbittorrent.service
systemctl enable qbittorrent.service
```

## 参数说明

- `-p 8080:8080` WebUI
- `-p 6881:6881` TCP连接端口
- `-p 6881:6881/udp` UDP连接端口
- `-e PUID=1000` User ID 确保主机上的所有卷目录都归您指定的同一用户所有
- `-e PGID=1000` Group ID 确保主机上的所有卷目录都归您指定的同一用户组所有
- `-e TZ=Etc/UTC` 指定要使用时区，请参阅此[列表](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)。
- `-e WEBUI_PORT=8080` Web UI的端口
- `-e TORRENTING_PORT=6881` TCP/UDP连接的端口
- `-v /config` 包含所有相关的配置文件。
- `-v /downloads` 磁盘上下载的位置。
- `--read-only=true` 使用只读文件系统运行容器。请[阅读文档](https://docs.linuxserver.io/misc/read-only/#why)。
- `--user=1000:1000` 使用非root用户运行容器。请[阅读文档](https://docs.linuxserver.io/misc/non-root/)。

## 端口选择

BT 客户端向 Tracker 服务器报告它正在使用某个默认的BT协议端口(6881-6889)或是任何其他常见 P2P 端口来作为连接端口。
有的 PT 站不允许这些通常被 P2P 协议默认使用的端口。
原因是目前 ISP 常常对这些端口进行限速。

常见的 P2P 协议默认使用的端口：

- Direct Connect    411 - 413
- BitTorrent        6881 - 6889
- Kazza             1214
- Gnutella          6346 - 6347
- Emule             4662
- WinMX             6699

最好给 BT 客户端使用未在上面列出的端口范围(从 **49152** 到 **65535** 都是不错的选择，参看[IANA](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml))。
注意某些客户端，如Azureus 2.0.7.0或更高版本，对所有的种子都使用同一端口。
而其他大多数客户端为每一个种子开放一个端口，你在选择端口范围应考虑到这个问题。
一般来说端口范围小于10。设置一个过大的范围并不一定有好处，而且可能有安全隐患。
