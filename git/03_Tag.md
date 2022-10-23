# Git 标签

Git 可以给仓库历史中的某一个提交打上标签，以示重要。
比较有代表性的是人们会使用这个功能来标记版本。

## 列出标签

```bash
# 列出标签
git tag
# 以字母顺序列出标签
git tag -l '<tagname>'
```

## 创建标签

Git 支持两种标签：轻量标签（lightweight）与附注标签（annotated）。

```bash
# 附注标签
git tag -a <tagname> -m "这里是一段注释"
# 轻量标签
## 创建轻量标签，不需要使用 -a、-s 或 -m 选项，只需要提供标签名字
git tag <tagname>

# 后期打标签，可以对过去的提交打标签
git tag -a <tagname> <commit id>
```

## 共享标签

默认情况下，`git push` 命令并不会传送标签到远程仓库服务器上。
在创建完标签后你必须显式地推送标签到共享服务器上。

```bash
# 推送标签
git push origin <tagname>

# 推送全部标签到远程仓库
$ git push origin --tags
```

## 删除标签

```bash
# 删除标签
# 并不会从任何远程仓库中删除这个标签。
git tag -d <tagname>

# 从远程仓库删除标签
# 将冒号前面的空值推送到远程标签名，从而高效地删除它。
git push <remote> :refs/tags/<tagname>
# 更直观的删除远程标签的方式。
git push origin --delete <tagname>
```

## 检出标签

直接检出标签会使你的仓库处于“分离头指针（detached HEAD）”的状态。
在“分离头指针”状态下，如果你做了某些更改然后提交它们，标签不会发生变化，但你的新提交将不属于任何分支，并且将无法访问，除非通过确切的提交哈希才能访问。
因此，如果你需要进行更改，比如你要修复旧版本中的错误，那么通常需要创建一个新分支。

```bash
# 查看某个标签所指向的文件版本
git checkout <tagname>

# 创建一个名为 <name> 的新分支，这个分支指向标签 <tagname>
git checkout -b <name> <tagname>
```
