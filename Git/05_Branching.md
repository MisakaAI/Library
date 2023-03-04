# 分支

主分支通常是 `master` 或者 `main`

Git 有一个名为 `HEAD` 的特殊指针，用于指向当前所在的本地分支。

## 分支管理

```bash
# 创建分支 <name>
git branch <name>

# 查看所有分支
git branch

# 查看每一个分支的最后一次提交
git branch -v

# 已合并到当前分支的分支
git branch --merged

# 未合并到当前分支的分支
git branch --no-merged

# 切换到 <name> 分支
git checkout <name>
git switch <name>

# 创建并切换到 <name> 分支，等于一下两条命令
git checkout -b <name>
git switch -c <name>

# 切换到上一个切换的分支
git switch -

# 删除合并后的分支
git branch -d <name>

# 强制删除分支
git branch -D <name>
```

## 分支合并

任何因包含合并冲突而有待解决的文件，都会以未合并状态标识出来。
Git 会在有冲突的文件中加入标准的冲突解决标记，这样你可以打开这些包含冲突的文件然后手动解决冲突。

```bash
# 合并指定分支到当前分支
git merge <name>

# 查看因包含合并冲突而处于未合并状态的文件
git status
```

## 远程分支

```bash
# 显式地获得远程引用的完整列表
git ls-remote <remote>

# 获得远程分支的更多信息
git remote show <remote>

# 当克隆一个仓库时，它通常会自动地创建一个跟踪 origin/master 的 master 分支。
# 设置其他的跟踪分支
git checkout -b <name> <remote>/<name>
# Git 提供了 --track 快捷方式实现这个操作
git checkout --track <remote>/<name>
# 由于这个操作太常用了，该捷径本身还有一个捷径。
# 尝试检出的分支 (a) 不存在且 (b) 刚好只有一个名字与之匹配的远程分支，那么 Git 就会为你创建一个跟踪分支
git checkout <name>
# 将本地分支与远程分支设置为不同的名字，就可以使用
git checkout -b abc <remote>/<name>

# 查看设置的所有跟踪分支
git branch -v

#删除远程分支
git push origin --delete <name>
```
