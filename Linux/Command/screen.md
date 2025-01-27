# Screen

GNU Screen 是一款由GNU计划开发的用于命令行终端切换的自由软件。
用户可以通过该软件同时连接多个本地或远程的命令行会话，并在其间自由切换。

GNU Screen 可以看作是窗口管理器的命令行界面版本。
它提供了统一的管理多个会话的界面和相应的功能。

Screen 也可以让一个或多个用户从不同终端多次登录一个会话，并共享会话的所有特性（比如可以看到完全相同的输出）。

## 安装

```sh
# Debian/Ubuntu
apt install screen
#  RHEL/Fedora
dnf install screen
```

## 使用

```sh
# 创建一个 screen 终端，命名为 test
screen -S test

# 临时离开终端
# 按下 Ctrl+A 键，再按 D 键

# 查看目前所有的 screen 终端
screen -ls
screen -list

# 重新连接到 test
screen -r test
```

## 语法

```sh
screen [-AmRvx -ls -wipe][-d <作业名称>][-h <行数>][-r <作业名称>][-s ][-S <作业名称>]
```

- `-A` 将所有的窗口都调整为目前终端机的大小
- `-d <作业名称>` 将指定的screen作业离线
- `-h <行数>` 指定窗口的缓冲区行数
- `-m` 即使目前已在作业中的screen作业，仍强制建立新的screen作业
- `-r <作业名称>` 恢复离线的screen作业
- `-R` 先试图恢复离线的作业。若找不到离线的作业，即建立新的screen作业
- `-s` 指定建立新窗口时，所要执行的shell
- `-S <作业名称>` 指定screen作业的名称
- `-v` 显示版本信息
- `-x` 恢复之前离线的screen作业
- `-ls` 或 `--list` 显示目前所有的screen作业
- `-wipe` 检查目前所有的screen作业，并删除已经无法使用的screen作业
