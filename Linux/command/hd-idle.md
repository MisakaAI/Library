# hd-idle

`hd-idle` 是一个非常适合用于管理硬盘休眠的守护进程，尤其是对于外置 USB 硬盘。

## 安装

```sh
apt-get install hd-idle
```

## 配置

编辑 `/etc/default/hd-idle`

```txt
HD_IDLE_OPTS="-a /dev/sda -i 600 -a /dev/sdb -i 600"
```

## 重启

```sh
systemctl restart hd-idle
```

## 检查状态

```sh
systemctl status hd-idle
```
