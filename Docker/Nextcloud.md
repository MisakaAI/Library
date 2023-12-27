# Nextcloud All-in-One

- [Nextcloud AIO Github](https://github.com/nextcloud/all-in-one)

```sh
docker run \
    --init \
    --sig-proxy=false \
    --name nextcloud-aio-mastercontainer \
    --restart always \
    --publish 8088:8080 \
    --env APACHE_PORT=11000 \
    --env APACHE_IP_BINDING=0.0.0.0 \
    --volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config \
    --volume /var/run/docker.sock:/var/run/docker.sock:ro \
    --env NEXTCLOUD_DATADIR=/data/nextcloud \
    --env SKIP_DOMAIN_VALIDATION=true \
    --env NEXTCLOUD_ENABLE_DRI_DEVICE=true \
    nextcloud/all-in-one:latest
```

- `SKIP_DOMAIN_VALIDATION`: 跳过域名验证
- `NEXTCLOUD_DATADIR`: 存储目录
- `NEXTCLOUD_ENABLE_DRI_DEVICE`: 启用硬件转码

执行后进入`https://ip:8088`进行设置。（默认为8080，但是和qb冲突，此处修改为8088）

## 修改 Nginx 配置

`/etc/nginx/conf.d/default.conf`

```conf
# Nextcloud
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
    listen 80;
    listen [::]:80;            # comment to disable IPv6

    if ($scheme = "http") {
        return 301 https://$host$request_uri;
    }

    listen 443 ssl http2;      # for nginx versions below v1.25.1
    listen [::]:443 ssl http2; # for nginx versions below v1.25.1 - comment to disable IPv6

    server_name cloud.zi-o.com;

    location / {
        proxy_pass http://127.0.0.1:11000$request_uri;

        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Port $server_port;
        proxy_set_header X-Forwarded-Scheme $scheme;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Accept-Encoding "";
        proxy_set_header Host $host;

        client_body_buffer_size 512k;
        proxy_read_timeout 86400s;
        client_max_body_size 0;

        # Websocket
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
    }

    ssl_certificate /etc/ssl/cloud.zi-o.com_nginx/cloud.zi-o.com_bundle.crt;   # managed by certbot on host machine
    ssl_certificate_key /etc/ssl/cloud.zi-o.com_nginx/cloud.zi-o.com.key; # managed by certbot on host machine

    ssl_session_timeout 1d;
    ssl_session_cache shared:MozSSL:10m; # about 40000 sessions
    ssl_session_tickets off;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305;
    ssl_prefer_server_ciphers on;
}
```
