# 配置 Git

```bash
# 全局 设置姓名
git config --global user.name "Your Name"

# 全局 设置邮箱
git config --global user.email "email@example.com"

# 单个仓库 设置姓名
git config user.name "Your Name"

# 单个仓库 设置邮箱
git config user.email "email@example.com"

# 查看当前姓名
git config user.name

# 查看当前邮箱
git config user.email
```

## 基础

```bash
# 系统级 /etc/gitconfig 文件
git config --system

# 每个用户的 ~/.gitconfig 或 ~/.config/git/config 文件
git config --global

# 正在操作的仓库所对应的 Git 目录下的配置文件 .git/config
git config --local
```

```bash
# 修改默认的编辑器
git config --global core.editor vim

# 让Git适当的显示颜色
git config --global color.ui true

# 显示历史记录时，每个提交的信息只显示一行
git config --global format.pretty oneline

# 中文文件名或者路径不转义
git config --global core.quotepath false
```

## 安全的存储库

Git 添加了新的目录安全限制。

```bash
# 将当前目录设置为安全的存储库
git config --global --add safe.directory $(pwd)

# 可以通过加通配符为*，忽略所有文件夹。
git config --global --add safe.directory "*"
```

## 推送

```bash
# 只会推送本地当前分支，如果上游分支的名称与本地分支不同，则拒绝推送。
# Git2.0之后的默认模式
git config --global push.default simple

# 一次性的推送远端和本地都存在的同名分支（如果目前只在一个分支上完成工作，其他分支还未完成，则这种方式不适合你）
# Git2.0之前的默认模式
git config --global push.default matching
```

## 混合换行符

```bash
# core.autocrlf
git config --global core.autocrlf input
# true: push 时把 CRLF 转换成 LF，pull 时把 LF 转换成 CRLF
# input: push 时把 CRLF 转换成 LF，pull 时不转换
# false: 不转换

# safecrlf
git config --global core.safecrlf true
# warn: 提交包含混合换行符的文件时给出警告(默认值)
# true: 拒绝提交包含混合换行符的文件
# false: 允许提交包含混合换行符的文件
```

## 凭证存储

```bash
# credential.helper
git config --global credential.helper store
# (默认)：不保存凭证。
# cache: 将凭证存放在内存中一段时间。 密码永远不会被存储在磁盘中，并且在15分钟后从内存中清除。
# store 将凭证用明文的形式存放在磁盘中，并且永不过期。即：push 提交不需要输入密码。
# osxkeychain: MAC专用，将凭证缓存到你系统用户的钥匙串中。 这种方式将凭证存放在磁盘中，并且永不过期，但是是被加密的。

# 取消设置
git config --global --unset credential.helper
```

## 代理

```bash
# 设置代理
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'

# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy
```
