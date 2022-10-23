# 安装 Git

## Linux

[Download for Linux and Unix](https://git-scm.com/download/linux)

```bash
# Debian / Ubuntu
sudo apt install git

# RHEL / Fedora
sudo dnf install git
```

还有一个合集的包叫 `git-all`，包括了下面几个软件包。

- **git-cvs**：git-cvs 互操作性
- **git-doc**：git 文档
- **git-email**：git 电子邮件 add-on
- **git-gui**：git GUI
- **git-mediawiki**：MediaWiki 远程助手
- **git-svn**：git-svn 互操作性
- **gitk**：git 版本树可视化器
- **gitweb**：git Web 界面

此外，还有两个简单的 git 仓库的服务，非常适合只读更新，即通过网络从 git 仓库拉取。

- **git-daemon-run**：一个简单的 git 仓库的服务器，比 git-daemon-sysvinit 更简单、更可靠，代价是对习惯于 sysvinit 的管理员来说不太熟悉。
- **git-daemon-sysvinit**：一个简单的 git 仓库的服务器，这个包为 git-daemon 提供了通常的 sysvinit 服务管理命令 `service git-daemon start/stop`

## Windows

[Download for Windows](https://git-scm.com/download/win)

下载，然后一直下一步就可以了。

范例：(2.38.1) 64-bit version

## Macos

[Download for macOS](https://git-scm.com/download/mac)

```sh
# Homebrew
brew install git
```
