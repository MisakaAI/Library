# CLI Proxy API

## 安装

```sh
curl -fsSL https://raw.githubusercontent.com/router-for-me/cliproxyapi-installer/refs/heads/master/cliproxyapi-installer | bash
```

### 配置

修改 `config.yaml`

```yaml
# Server host/interface to bind to. Default is empty ("") to bind all interfaces (IPv4 + IPv6).
# Use "127.0.0.1" or "localhost" to restrict access to local machine only.
host: "127.0.0.1"
# Server port
port: 8317
# TLS settings for HTTPS. When enabled, the server listens with the provided certificate and key.
tls:
  enable: false
  cert: ""
  key: ""
# Management API settings
remote-management:
# Whether to allow remote (non-localhost) management access.
# When false, only localhost can access management endpoints (a key is still required).
  allow-remote: true
# Management key. If a plaintext value is provided here, it will be hashed on startup.
# All management requests (even from localhost) require this key.
# Leave empty to disable the Management API entirely (404 for all /v0/management routes).
  secret-key: "<密钥>"
# Disable the bundled management control panel asset download and HTTP route when true.
```

### 持久化

```sh
# 非 root 用户需要检查
# 用户退出登录后，这个用户自己的 systemd --user 服务要不要继续活着
# Linger=no
loginctl show-user <user> -p Linger

# 设置退出登录后服务继续运行
sudo loginctl enable-linger <user>

# 再次检查，应得到结果为
# Linger=yes
loginctl show-user <user> -p Linger

# 开机启动 & 启动服务
systemctl --user enable --now cliproxyapi.service
```

## 登录 CodeX

```sh
# 服务器登录 CodeX
./cli-proxy-api --codex-login

# 需要在自己的电脑上执行
# OpenAI 的 OAuth callback 需要转发 1455 端口
ssh -N -L 1455:127.0.0.1:1455 <user>@<server>
```

### Nginx

创建 `/etc/nginx/conf.d/cliproxyapi.conf`

```conf
server {
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name api.example.net;

    ssl_certificate /etc/ssl/api.example.net/fullchain.pem;
    ssl_certificate_key /etc/ssl/api.example.net/privkey.pem;

    client_max_body_size 100m;

    location / {
        proxy_pass http://127.0.0.1:8317;

        proxy_http_version 1.1;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # 禁止 Nginx 缓冲 AI 流式响应
        proxy_buffering off;
        proxy_cache off;

        # 避免长请求被 Nginx 提前断掉
        proxy_connect_timeout 60s;
        proxy_send_timeout 600s;
        proxy_read_timeout 600s;
    }
}
```

```sh
nginx -t
systemctl restart nginx.service
```

## Web UI

```sh
# http://localhost:8317/management.html
https://api.example.net/management.html#/login
```