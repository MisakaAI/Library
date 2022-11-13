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

### 使用凭证提交 Aka.免密提交

```bash
# 创建SSH Key
ssh-keygen -t rsa -b 4096 -C "youremail@example.com"

# 查看SSH Key
cat ~/.ssh/id_rsa.pub
# id_rsa		私钥，不可泄漏
# id_rsa.pub	公钥
```

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