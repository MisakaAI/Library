# Git Squash

将多个连续的提交合并成一个提交，保留最终更改内容，但清理中间过程的冗余提交记录。

## 交互式变基

```sh
# 合并最近3个提交
git rebase -i HEAD~3
```

执行后，Git 会打开编辑器

```git
pick a1b2c3d Commit 1
pick b2c3d4e Commit 2
pick c3d4e5f Commit 3
```

将需要合并的提交的 `pick` 改为 `squash`（或简写 `s`），保留第一个提交为 `pick`

- `squash` 合并提交并保留所有提交信息，可编辑最终信息。
- `fixup` 合并提交但丢弃被合并提交的信息，仅保留目标提交的信息。（最终提交信息仅保留 "Commit 1"）

```git
pick a1b2c3d Commit 1
squash b2c3d4e Commit 2
s c3d4e5f Commit 3
```

将变更推送到远程仓库

```sh
# 仅适用于已推送过的分支，需谨慎使用
git push --force
```

## 非交互式变基

```sh
# 切换到目标分支（如 main）
git checkout main

# 执行 squash 合并（将 feature-branch 的提交合并为一个）
git merge --squash feature-branch

# 手动提交合并后的结果
git commit -m "Squashed commit from feature-branch"
```
