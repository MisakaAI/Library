# App Transport Security

自2017年01月01日起，根据苹果公司要求，所有iOS应用必须使用ATS（App Transport Security），即iOS应用内的连接必须使用安全的HTTPS连接。

## ATS默认的安全要求

- 服务器必须支持传输层安全（TLS）协议1.2以上版本；
- 通讯加密套件仅限支持完全正向加密的套件；
- 证书必须使用SHA256或更高的哈希算法签名；以及2048位以上RSA密钥或256位以上ECC密钥。

不满足以上条件，ATS会拒绝连接。

## Nginx

- 证书文件 `cloud.tencent.com_bundle.crt`
- 证书文件 `cloud.tencent.com_bundle.pem`
- 私钥文件 `cloud.tencent.com.key`
- CSR 文件 `cloud.tencent.com.csr`

[SSL Configuration Generator](https://ssl-config.mozilla.org/)

```nginx.conf
http {

    server {
        listen 443 ssl;
        listen [::]:443 ssl;

        http2 on;
        charset utf-8;
        server_tokens off;

        ssl_certificate /etc/ssl/cloud.tencent.com_bundle.crt;
        ssl_certificate_key /etc/ssl/cloud.tencent.com.key;

        # HSTS (ngx_http_headers_module is required) (63072000 seconds)
        add_header Strict-Transport-Security "max-age=63072000" always;
    }

    # 中间配置
    # intermediate configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ecdh_curve X25519:prime256v1:secp384r1;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305;
    ssl_prefer_server_ciphers off;

    # 启用有状态的 TLS 会话缓存
    # see also ssl_session_ticket_key alternative to stateful session cache
    ssl_session_timeout 1d;
    ssl_session_cache shared:MozSSL:10m;  # about 40000 sessions

    # curl https://ssl-config.mozilla.org/ffdhe2048.txt > /etc/nginx/dhparam
    ssl_dhparam "/etc/nginx/dhparam";
}
```

## 检测

- [TrustAsia ATS检测](https://myssl.com/ats.html)
- [腾讯云域名服务检测工具](https://cloud.tencent.com/product/tools)

## 参考文献

- [Preventing Insecure Network Connections](https://developer.apple.com/documentation/security/preventing-insecure-network-connections)
