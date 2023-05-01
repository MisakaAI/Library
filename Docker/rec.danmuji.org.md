# B站录播姬

[Docker 镜像](https://rec.danmuji.org/user/install/docker/)

```bash
# 拉取镜像
docker pull bililive/recorder:latest

# 启动录播姬

# 公网使用推荐：配置 https + 用户名&密码
docker run -d -u 1000:1000 -v 宿主机路径:/rec -p 2356:2356 --mount type=bind,source=/etc/ssl,target=/etc/ssl,readonly --name="BililiveRecorder" bililive/recorder run --bind "http://*:2356" --http-basic-user "用户名" --http-basic-pass "密码" --cert-pem-path "证书文件路径" --cert-key-path "私钥文件路径" /rec

# 仅本地：仅http
docker run -d -u 1000:1000 -v 宿主机路径:/rec -p 2356:2356 --name="BililiveRecorder" bililive/recorder

# -d 后台运行
# -u 用户 <name|uid>[:<group|gid>] 用于处理保存文件的权限
# -v 挂载目录
# -p 映射端口 宿主机端口:容器端口
# --name=""，指定容器名称
# 绑定端口
# --bind "http://*:2356"

# 设置用户密码
# --http-basic-user "用户名"
# --http-basic-pass "密码"

# https 协议
# --cert-pem-path "证书文件路径"
# --cert-key-path "私钥文件路径"

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