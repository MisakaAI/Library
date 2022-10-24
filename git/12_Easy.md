# 简易指南

```bash
# 安装
apt install git

# 设置用户名及邮箱
git config --global user.name "Your Name"
git config --global user.email "email@example.com"

# 创建新仓库
git init

# 检出仓库
git clone username@host:/path/to/repository

# 添加到暂存区
git add .

# 提交到仓库
git commit -m "代码提交信息"

# 提交到远程仓库
git push origin master

# 连接到某个远程服务器
git remote add origin <server>

# 创建一个叫做“feature_x”的分支，并切换过去
git checkout -b feature_x

# 切换回主分支
git checkout master

# 把新建的分支删掉
git branch -d feature_x

# 将分支推送到远端仓库
git push origin <branch>

# 更新本地仓库至最新改动，并自动合并
git pull

# 要合并其他分支到当前分支
git merge <branch>

# 自动合并出现冲突需要手动合并，然后提交
git add <file>

# 预览差异
git diff <source_branch> <target_branch>

# 创建一个叫做 1.0.0 的标签
# 1b2e1d63ff 是提交 ID 的前 10 位字符
git tag 1.0.0 1b2e1d63ff

# 查看本地仓库的历史记录
git log

# 只看某一个人的提交记录
git log --author=bob

# 一个压缩后的每一条提交记录只占一行的输出
git log --pretty=oneline

# 展示所有的分支
git log --graph --oneline --decorate --all

# 看看哪些文件改变了
git log --name-status

# 替换掉本地改动
# 使用 HEAD 中的最新内容替换掉你的工作目录中的文件。
# 已添加到暂存区的改动以及新文件都不会受到影响。
git checkout -- <filename>

# 丢弃你在本地的所有改动与提交
# 到服务器上获取最新的版本
# 并将你本地主分支指向它
git fetch origin
git reset --hard origin/master

# 彩色的 git 输出
git config color.ui true

# 显示历史记录时，每个提交的信息只显示一行
git config format.pretty oneline
```