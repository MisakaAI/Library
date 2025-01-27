# 常见或者不常见的一些问题记录

## 启动终端错误提示

启动终端时出现 To run a command as administrator (user root) use sudo command See man sudo_root

解决方法：

```bash
touch ~/.sudo_as_admin_successful
```

## 调整 SSH 登陆后显示的内容

- 修改 `/etc/motd`
- 修改 `/etc/update-motd.d/*`
- 修改 `/etc/ssh/sshd_config`

```conf
PrintLastLog no
```

重启 `ssh`

```sh
systemctl restart ssh.service
```
