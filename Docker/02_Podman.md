# Podman

Podman是一个无守护进程的容器引擎

## 安装

```bash
dnf install podman
```

## 使用

与 docker 命令完全兼容，基本可以认为 `alias docker=podman`

## 开机启动

```text
语法：podman generate systemd [options] {CONTAINER|POD}
选项：
--container-prefix string   //容器的Systemd单元名称前缀（默认为“容器”）
--files, -f                 //生成.service文件
--format string             //以指定格式（json）打印创建的单位
--name, -n                  //使用容器/容器名称，而不是ID
--new                       //创建新容器，而不是启动现有容器
--no-header                 //跳过标题生成
--pod-prefix string         //pod的Systemd单元名称前缀（默认为“pod”）
--restart-policy string     //Systemd重新启动策略（默认为“故障时”）
--separator string          //Systemd单元名称：名称/id和前缀之间的分隔符（默认“-”）
--time uint, -t             //停止超时覆盖（默认值为10）
```

```bash
## Root用户
# 生成 service 文件
# podman generate systemd -f --name BililiveRecorder

# 生成 service 文件 并写入systemd目录
podman generate systemd --name BililiveRecorder > /etc/systemd/system/BililiveRecorder.service

# 开机启动
systemctl enable BililiveRecorder.service

## 普通用户

# 创建目录
# mkdir -p ~/.config/systemd/user/
# cd ~/.config/systemd/user/

# 生成配置文件
# podman generate systemd -f --name BililiveRecorder

# 启用服务
# https://wiki.archlinuxcn.org/wiki/Systemd/%E7%94%A8%E6%88%B7

# --user 在用户登陆时启动
# systemctl --user enable --now  container-BililiveRecorder.service
# 启用延迟 退出登录不会注销服务
# loginctl enable-linger [username]
```

## 参考

- [Podman and Buildah for Docker users](https://developers.redhat.com/blog/2019/02/21/podman-and-buildah-for-docker-users/)
