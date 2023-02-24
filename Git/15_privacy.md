# 移除个人隐私

## 清除全部提交历史

### 方法1：换个新仓库

- 新建另一个远程仓库，命名为B
- 将现有的本地代码提交到远程仓库B
- 删除现有的远程仓库A
- 将远程仓库B命名为A

### 方法2：切换到新的空白分支

1.切换到新的分支

git checkout --orphan 的核心用途是 以类似git init的状态创建新的非父分支，也就是创建一个无提交记录的分支。

```bash
git checkout --orphan latest_branch
```

2.缓存所有文件

不会包含 `.gitignore` 中声明排除的

```bash
git add -A
```

3.提交跟踪过的文件（Commit the changes）

```bash
git commit -am "commit message"
```

4.删除master分支（Delete the branch）

```bash
git branch -D master
```

5.重命名当前分支为master（Rename the current branch to master）

```bash
git branch -m master
```

6.提交到远程master分支 （Finally, force update your repository）

```bash
git push -f origin master
```

## 从提交历史中移除单个文件

假设要移除的文件路径（相对路径）为 `django/settings.py`

执行如下指令：

```bash
git filter-branch --index-filter \
'git rm --cached --ignore-unmatch django/settings.py' \
--tag-name-filter cat -- --all
```

使用指令硬更新到远程仓库：

```bash
git push origin HEAD --force
```
