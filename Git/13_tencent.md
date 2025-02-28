# 腾讯工蜂

[腾讯工蜂](https://code.tencent.com/)
[帮助文档](https://code.tencent.com/help/ssh#git)

## no matching host key type found

修改 `~/.ssh/config`

```config
Host git.code.tencent.com
    HostName git.code.tencent.com
    HostKeyAlgorithms +ssh-rsa
    PubkeyAcceptedAlgorithms +ssh-rsa
```

## Permission denied (publickey).

腾讯工蜂不支持 `ed25519`，需要创建 `rsa` 密钥，并指定使用。
修改 `~/.ssh/config`

```sh
ssh-keygen -t rsa -b 4096 -f ~/.ssh/tencent_rsa -N "" -C "youremail@example.com"
```

```config
Host git.code.tencent.com
    IdentityFile ~/.ssh/tencent_rsa
    IdentitiesOnly yes
```

## 快速使用

```sh
echo "Host git.code.tencent.com
    HostName git.code.tencent.com
    HostKeyAlgorithms +ssh-rsa
    PubkeyAcceptedAlgorithms +ssh-rsa
    IdentityFile ~/.ssh/tencent_rsa
    IdentitiesOnly yes" >> ~/.ssh/config
```
