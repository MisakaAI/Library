# Fail2Ban

- [Github](https://github.com/fail2ban/fail2ban)

## 安装

```sh
apt update && apt upgrade
apt install fail2ban
```

## 配置

修改 `/etc/fail2ban/fail2ban.local`

```conf
[DEFAULT]
# 是否允许 IPv6 地址。
# 默认值是 auto，表示自动检测。
allowipv6 = auto
```

修改 `/etc/fail2ban/jail.local`

```conf
[DEFAULT]
# 禁止时间：被封禁 IP 地址的时长，单位是秒。
# 1 Day = 1 天
bantime  = 1d
# 查找时间：在这个时间段内超过最大失败尝试次数会被封禁，单位是秒。
# 3600 秒 = 1 小时
findtime = 3600
# 最大失败尝试次数：在查找时间段内允许的最大失败尝试次数。
maxretry = 3
# 白名单
ignoreip = 127.0.0.1/8 192.168.0.100
# 封禁动作
# iptables-multiport：默认的多端口封禁动作。
# iptables-allports：封禁所有端口的动作。
# iptables：基本的 iptables 封禁动作。
# firewalld：适用于使用 firewalld 作为防火墙的系统。
# hostsdeny：使用 /etc/hosts.deny 文件来封禁 IP 地址。
banaction = iptables
[sshd]
# 是否启用此 jail。true 表示启用，false 表示禁用。
enabled  = true
# 指定使用的过滤器。
# fail2ban 将使用这个过滤器从日志中提取失败的 SSH 登录尝试。
filter = sshd
# 监听的端口。默认是 ssh，可以根据需要修改。
port     = ssh
# 日志文件的后端。使用 systemd 来读取 journald 日志。
backend = systemd
```

## 服务

```sh
# 启动服务
systemctl start fail2ban

# 查看服务状态
systemctl status fail2ban
```

## 查看状态

```sh
# 查看 fail2ban 状态
fail2ban-client status

# 查看 fail2ban 的 sshd 状态
fail2ban-client status sshd
```

## 查看日志

```sh
# 查看 fail2ban 日志
tail -f /var/log/fail2ban.log
```

## 解封 IP

```sh
# 解封所有IP
fail2ban-client unban --all

# 解封指定IP
fail2ban-client unban 192.168.1.1
```

## 参考文献

- [使用Fail2Ban进行SSH强制保护](https://www.linode.com/docs/guides/how-to-use-fail2ban-for-ssh-brute-force-protection/)
- [fail2ban wiki](https://github.com/fail2ban/fail2ban/wiki)
- [Fail 2ban PostgreSQL](https://warlord0blog.wordpress.com/2022/09/14/fail2ban-postgresql/)
