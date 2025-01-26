# Memos

一个可用于知识管理和社交网络的开源、自托管的备忘录中心。

[Memos](https://usememos.com/)
[github](https://github.com/usememos/memos)

```bash
# 拉取镜像
docker pull ghcr.io/usememos/memos:latest

# 创建工作目录
mkdir /data/memos

# 启动
docker run -d --name memos -p 5230:5230 --restart=unless-stopped -v /data/memos:/var/opt/memos neosmemo/memos:stable

# 防火墙
firewall-cmd --zone=public --permanent --add-port=5230/tcp
firewall-cmd --reload

# 生成 service 文件 并写入systemd目录
podman generate systemd --name memos > /etc/systemd/system/memos.service

# 启动
systemctl start memos.service
systemctl enable memos.service
```

## 使用 Nginx 作为反向代理

```conf
# /etc/nginx/sites-available/your-domain-name.com
server {
    server_name your-domain-name.com;

    location / {
        proxy_pass http://localhost:5230;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # 启用 SSL
        # ssl_certificate /etc/letsencrypt/live/your-domain-name.com/fullchain.pem;
        # ssl_certificate_key /etc/letsencrypt/live/your-domain-name.com/privkey.pem;
        # include /etc/letsencrypt/options-ssl-nginx.conf;
        # ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
    }
}
```

使用 `sudo systemctl restart nginx` 重启 Nginx 服务

## 更新

```更新
# 停止镜像运行，并删除镜像。
systemctl stop memos.service
docker rm memos
docker image rm memos:stable

# 重新拉取及启动
docker pull neosmemo/memos:stable
docker run -d --name memos -p 5230:5230 --restart=unless-stopped -v /data/memos:/var/opt/memos neosmemo/memos:stable

# 重新生成 service 文件 并写入systemd目录
# podman generate systemd --name memos > /etc/systemd/system/memos.service

# 重新加载 systemd 配置
# systemctl daemon-reload

# 启动
systemctl start memos.service
```
