# 腾讯工蜂

[腾讯工蜂](https://code.tencent.com/)
[帮助文档](https://code.tencent.com/help/ssh#git)

## no matching host key type found

修改 `~/.ssh/config`

```txt
HostKeyAlgorithms +ssh-rsa
PubkeyAcceptedAlgorithms +ssh-rsa
```
