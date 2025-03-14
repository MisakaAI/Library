# acme.sh

- [acme.sh](https://github.com/acmesh-official/acme.sh/wiki/%E8%AF%B4%E6%98%8E)

## 安装

```sh
curl https://get.acme.sh | sh -s email=ai@misaka.cn

# https://github.com/acmesh-official/acme.sh/wiki/Install-in-China
# 如果你的安装服务器位于中国大陆境内, 访问 github 可能会不成功. 所以安装可能会失败.
# 推荐从这里下载安装
git clone https://gitee.com/neilpang/acme.sh.git
cd acme.sh
./acme.sh --install -m my@example.com
```

程序被安装在 `~/.acme.sh/` 目录下

### 添加 alias

```sh
alias acme.sh=~/.acme.sh/acme.sh
```

## 生成证书

### dns 方式

手动在域名上添加一条 txt 解析记录，验证域名所有权。
可使用域名解析商提供的 api 自动添加 txt 记录完成验证。

使用 `dnspod.cn`，创建 `DNSPod Token`。
（注意：不要创建为 `腾讯云 API 密钥`）

#### 参考

- [DNSPod.cn](https://github.com/acmesh-official/acme.sh/wiki/dnsapi#dns_dp)
- [CloudFlare](https://github.com/acmesh-official/acme.sh/wiki/dnsapi#dns_cf)

```sh
# DNSPod.cn
export DP_Id="<id>"
export DP_Key="<key>"
# CloudFlare Global API Key
# https://dash.cloudflare.com/profile/api-tokens
export CF_Key="763eac4f1bcebd8b5c95e9fc50d010b4"
export CF_Email="alice@example.com"
# CloudFlare 用户 API 令牌 区域 ID （域名概述右下角）
export CF_Token="Y_jpG9AnfQmuX5Ss9M_qaNab6SQwme3HWXNDzRWs"
export CF_Zone_ID="763eac4f1bcebd8b5c95e9fc50d010b4"
# CloudFlare 用户 API 令牌 帐户 ID （域名概述右下角）
export CF_Token="Y_jpG9AnfQmuX5Ss9M_qaNab6SQwme3HWXNDzRWs"
export CF_Account_ID="763eac4f1bcebd8b5c95e9fc50d010b4"
```

```sh
# DNSPod.cn
./acme.sh --issue --dns dns_dp -d misaka.cn -d '*.misaka.cn'
# CloudFlare
./acme.sh --issue --dns dns_cf -d misaka.cn -d '*.misaka.cn'
```

证书就会自动生成了. 这里给出的 `api id` 和 `api key` 会被自动记录下来, 将来你在使用 `dnspod api` 的时候, 就不需要再次指定了. 直接生成就好了:

`~/.acme.sh/account.conf`
`~/.acme.sh/misaka.cn/misaka.cn.conf`

```sh
acme.sh --issue -d misaka.cn --dns dns_dp
```

## 安装证书

### Apache example

```sh
acme.sh --install-cert -d example.com \
--cert-file      /path/to/certfile/in/apache/cert.pem  \
--key-file       /path/to/keyfile/in/apache/key.pem  \
--fullchain-file /path/to/fullchain/certfile/apache/fullchain.pem \
--reloadcmd     "service apache2 force-reload"
```

### Nginx example

```sh
acme.sh --install-cert -d misaka.cn \
--key-file       /etc/ssl/misaka.cn/privkey.pem  \
--fullchain-file /etc/ssl/misaka.cn/fullchain.pem \
--reloadcmd     "systemctl force-reload nginx.service"
```

## 查看已安装证书

```sh
# 查看已安装证书
acme.sh --list

# 查看已安装证书信息
acme.sh --info -d misaka.cn
```

## 自动更新证书

使用 `crontab  -l` 查看

```cron
56 * * * * "/root/.acme.sh"/acme.sh --cron --home "/root/.acme.sh" > /dev/null
```

## 更新 acme.sh

```sh
# 升级 acme.sh 到最新版
acme.sh --upgrade

# 自动升级
acme.sh --upgrade --auto-upgrade

# 关闭自动更新
acme.sh --upgrade --auto-upgrade  0
```

## 卸载

```sh
acme.sh --uninstall
```
