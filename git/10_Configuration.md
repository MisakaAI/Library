# 配置 Git

```bash
# 设置姓名
git config --global user.name "Your Name"

# 设置邮箱
git config --global user.email "email@example.com"

# 执行 git push 没有指定分支时，只有当前分支会被 push 到你使用 git pull 获取的代码
git config --global push.default simple

# 让Git适当的显示颜色
git config --global color.ui true

# 只会推送本地当前分支
git config --global push.default simple

# Git在push时把CRLF转换成LF，pull时不转换
git config --global core.autocrlf input

# 拒绝提交包含混合换行符的文件
git config --global core.safecrlf true

# 设置代理
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'

# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy
```
