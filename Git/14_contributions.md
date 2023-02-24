# Github Contributions

参考：[为什么我的贡献没有在我的个人资料中显示？](https://docs.github.com/zh/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/why-are-my-contributions-not-showing-up-on-my-profile)

如果提交符合以下所有条件，则会在贡献图中显示：

- 用于提交的电子邮件地址与你在 GitHub.com上的帐户关联。
- 提交在独立的仓库而不是复刻中进行。
- 提交在以下位置进行：
  - 在仓库的默认分支中
  - 在 `gh-pages` 分支（对于具有项目网站的存储库）中

提交时的邮箱如果和 github.com 账户所关联的邮箱不一直，则不会显示。

```bash
# 查看哪些用户提交过
git shortlog -sne --all

# 修改历史提交记录
# OLD_EMAIL 为你提交代码时错误的邮箱地址
# CURRENT_NAME 为正确的用户名
# CURRENT_EMAIL 为正确的邮箱地址

git filter-branch --env-filter '
OLD_EMAIL="错误的邮箱地址"
CORRECT_NAME="正确的用户名"
CORRECT_EMAIL="正确的邮件地址"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags

# 将正确的信息 push
git push --force --tags origin 'refs/heads/*'
```

## Git 提示 Force overwriting the backup with -f 解决办法

使用指令批量清除了历史提交记录时，强制推送到远端，本地还留有缓存造成的问题。

可以删掉整个库，重新 `git clone`。
或者直接删除 `.git/refs/original` 目录后，再次执行指令即可。
