# 代理

```bash
# 设置代理
git config --global http.proxy 'socks5://127.0.0.1:7890'
git config --global https.proxy 'socks5://127.0.0.1:7890'

# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 使用 443 端口

解决：`ssh: connect to host github.com port 22: Connection timed out` 的问题。

修改 `~/.ssh/config`

```config
Host github.com
    Hostname ssh.github.com
    Port 443
```

## 参考文献

- [Git-Tools-Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- [git-submodule](https://www.atlassian.com/git/tutorials/git-submodule)
- [Git submodule 子模块的管理和使用](https://www.jianshu.com/p/9000cd49822c)
