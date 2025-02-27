# Github

- Overview 概况
- Repositories 仓库
- Projects 项目
- Packages 软件包
- Stars 星星 -> 仓库
- Follow 关注 -> 用户
- Issues 问题
- Fork 分支
- Pull request 提交请求
- Gist 代码片段 // 这个功能是被墙了的

## Fork

Fork 可以 Clone 一个开源的仓库，到自己的账号下。
自己拥有 Fork 后的仓库的读写权限。

## Pull request

修改 Fork 后的仓库之后，可以再推送回别人的仓库。
但是毕竟是别人的仓库，对方是否接受这个 Pull request 看他心情。

## 一些神奇的操作

### 使用 443 端口

解决：`ssh: connect to host github.com port 22: Connection timed out` 的问题。

修改 `~/.ssh/config`

```config
Host github.com
    Hostname ssh.github.com
    Port 443
```

### 将https方式改为ssh方式

```sh
# 查看远程仓库地址
git remote -v

# 移除远程仓库
git remote rm origin

# 添加新的远程仓库
git remote add origin <git@github.com>

# 显示本地 Git 分支的详细信息
# 包括每个分支的上游（远程跟踪分支）及其与远程分支的同步状态。
git branch -vv

# 推送
git push --set-upstream origin main
```

### 使用凭证提交 Aka.免密提交

```bash
# 创建SSH Key
# ssh-keygen -t rsa -b 4096 -C "youremail@example.com"
# 推荐使用 ed25519
ssh-keygen -t ed25519 -C "youremail@example.com"

# 查看SSH Key
cat ~/.ssh/id_ed25519.pub
```

- `id_ed25519` 私钥，不可泄漏
- `id_ed25519.pub` 公钥

将 `id_rsa.pub` 的内容添加到 [Github](https://github.com/settings/keys)

### 删除 Github 中的所有提交历史记录

不会保留以前的提交历史

```bash
# 创建并和切换到一个全新的分支
git checkout --orphan latest_branch

# 添加所有文件
git add -A

# 提交更改
git commit -am "commit message"

# 删除分支
git branch -D master

# 将当前分支重命名为master
git branch -m master

# 最后，强制更新存储库
git push -f origin master
```
