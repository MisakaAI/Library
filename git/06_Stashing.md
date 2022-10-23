# 暂存

```bash
# 暂存当前正在进行的工作
git stash

# 查看已暂存的工作
git stash list

# 恢复暂存的工作同时把暂存内容删除
git stash pop

# 恢复暂存的工作
git stash apply stash@{0}

# 将暂存内容删除
git stash drop stash@{0}
```
