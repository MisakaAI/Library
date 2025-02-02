# DNS

## 阿里云

- [阿里云公共DNS](https://www.alidns.com/)
- [DoT](https://help.aliyun.com/zh/dns/dns-over-tls)
- [DoH](https://help.aliyun.com/zh/dns/dns-over-https)

```sh
# IPv4地址
223.5.5.5
223.6.6.6

# IPv6地址
2400:3200::1
2400:3200:baba::1

# DNS over HTTPs(DoH)
https://dns.alidns.com/dns-query
```

## Google

- [Google Public DNS](https://developers.google.com/speed/public-dns?hl=zh-cn)

```sh
# IPv4地址
8.8.8.8
8.8.4.4

# IPv6地址
2001:4860:4860::8888
2001:4860:4860::8844

# 些设备要求为 IPv6 地址的所有八个字段提供显式值， 不能接受缩写的 :: IPv6 地址语法。
2001:4860:4860:0:0:0:0:8888
2001:4860:4860:0:0:0:0:8844

# DNS over HTTPs(DoH)
https://dns.google/dns-query
```

## Cloudflare

```sh
# IPv4地址
1.1.1.1
1.0.0.1

# IPv6地址
2606:4700:4700::1111
2606:4700:4700::1001

# DNS over HTTPs(DoH)
https://cloudflare-dns.com/dns-query
```
