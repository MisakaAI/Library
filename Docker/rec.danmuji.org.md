# B站录播姬

[Docker 镜像](https://rec.danmuji.org/user/install/docker/)

```bash
# 拉取镜像
docker pull bililive/recorder:latest

# 启动录播姬

docker run -d -v 宿主机路径:/rec -p 2356:2356 --name="BililiveRecorder" bililive/recorder run --bind "http://*:2356" --http-basic-user "用户名" --http-basic-pass "密码" --cert-pem-path "证书文件路径" --cert-key-path "私钥文件路径" /rec

# -d 后台运行
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
```
