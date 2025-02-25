# Last 显示系统的登录记录

## 用法

```sh
# 默认情况下，last 读取的是 /var/log/wtmp 文件（记录成功的登录）。
# last -f /var/log/wtmp
last

# 查看失败的登录尝试
# last -f /var/log/btmp | more
lastb

# 仅显示 IP 地址
last -f /var/log/btmp | awk '{print $3}' | sort | uniq -c

# 统计失败次数
last -f /var/log/btmp | wc -l
```
