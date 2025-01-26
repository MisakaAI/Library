# B站录播姬

[Docker 镜像](https://rec.danmuji.org/user/install/docker/)

```bash
# 拉取镜像
docker pull bililive/recorder:latest

# 启动录播姬
docker run -d \
  --name bililive-recorder \
  --restart unless-stopped \
  -p 2356:2356 \
  -v /data/rec:/rec \
  -e BREC_HTTP_BASIC_USER=用户名 \
  -e BREC_HTTP_BASIC_PASS=密码 \
  -e UMASK=022 \
  -e PUID=1000 \
  -e PGID=1000 \
  bililive/recorder:latest

# 从 2.11.0 开始，如果没有设置用户名密码，录播姬检查请求的 IP、Header 等参数并拒绝疑似来源不是局域网的请求。
# 如果你使用了带身份验证功能的反向代理、或使用域名访问内网服务等，可以通过设置环境变量 BREC_HTTP_OPEN_ACCESS 为【任意非空值】来禁用这个限制。

# 指定工作目录
# /rec

# 防火墙
firewall-cmd --zone=public --permanent --add-port=2356/tcp
firewall-cmd --reload

# 生成 service 文件 并写入systemd目录
podman generate systemd --name BililiveRecorder > /etc/systemd/system/BililiveRecorder.service

# 启动
systemctl start BililiveRecorder.service
systemctl enable BililiveRecorder.service
```

## Nginx

```conf
location /rec/ {
    auth_basic "Restricted";
    auth_basic_user_file /etc/nginx/htpasswd;
    proxy_pass http://localhost:2356/;
}
```
