# 阅读3服务器版

- [Github](https://github.com/hectorqin/reader)
- [文档](https://github.com/hectorqin/reader/blob/master/doc.md)

## 下载

```bash
# 拉取镜像
docker pull hectorqin/reader

# 创建工作目录

# 启动
# docker run -d --restart=always --name=reader -e "SPRING_PROFILES_ACTIVE=prod" -v $(pwd)/logs:/logs -v $(pwd)/storage:/storage -p 8080:8080 hectorqin/reader
docker run -d --restart=unless-stopped --name=reader -v /data/reader/log:/log -v /data/reader/storage:/storage -p 8081:8080 hectorqin/reader

# 生成 service 文件 并写入systemd目录
# podman generate systemd --name reader > /etc/systemd/system/reader.service

# 启动
# systemctl enable --now reader.service
```

## 书源

- [aoaostar](https://github.com/aoaostar/legado)
- [shidahuilang](https://github.com/shidahuilang/shuyuan)
- [XIU2](https://github.com/XIU2/Yuedu)
- [破冰](https://github.com/PB-pobing/pobing)

## 使用 Nginx 作为反向代理

```conf
# /etc/nginx/sites-available/your-domain-name.com
server {
    server_name your-domain-name.com;

    location /reader/ {
        # auth_basic "Restricted";
        # auth_basic_user_file /etc/nginx/htpasswd;
        proxy_pass http://localhost:8081/;
        proxy_http_version 1.1;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header Upgrade           $http_upgrade;
        proxy_set_header Connection        "upgrade";
        proxy_set_header Host              $host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host  $host;
        proxy_set_header X-Forwarded-Port  $server_port;
    }
}
```

使用 `sudo systemctl restart nginx` 重启 Nginx 服务。
