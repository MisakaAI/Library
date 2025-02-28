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

## cron 无法正确执行命令

`%` 需转义为 `\%`，否则 `cron` 会解析为换行符

```sh
# 单引号 ' 在终端中可以正常运行，在 .sh 脚本中也可以正常运行，但是直接写如 cron 中会出错。
# 0 3 * * * /usr/bin/pg_dump -h localhost -U postgres -d database > "/Backup/$(date +'%Y%m%d').sql.zst"
0 3 * * * /usr/bin/pg_dump -h localhost -U postgres -d database > "/Backup/$(date +\%Y\%m\%d).sql.zst"
```
