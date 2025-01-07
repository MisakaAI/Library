# OpenSSL

openssl 是目前最流行的 SSL 密码库工具，其提供了一个通用、健壮、功能完备的工具套件，用以支持SSL/TLS 协议的实现。

[openssl](https://www.openssl.org/source/)

## 安装

```bash
apt install oopenssl
```

## 使用

### 创建自签名CA证书

```bash
# 生成RSA私钥(无加密)
openssl genrsa -out ca_private.key 2048

## 生成rsa私钥，des3算法，4096位强度，server.key是秘钥文件名。
openssl genrsa -des3 -out server.key 4096

## 删除私钥中的密码
openssl rsa -in server.key -out server.key

# 生成公钥
openssl rsa -in ca_private.key -pubout -out rsa_public.key

# 生成证书请求文件
## openssl req -new -key server.key -out server.csr
openssl req -new -key ca_private.key -x509 -days 365 -out cert.crt

# 国家名称（2字母代码）[AU]：
# 州或省名称（全名）[州]：
# 地点名称（如城市）[]：
# 组织名称（如公司）[]：
# 组织单位名称（如部门）[]：
# 公用名称（例如服务器FQDN或您的名称）[]：
# 电子邮件地址[]:

## 生成自签名证书
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```
