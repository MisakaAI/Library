# Cockpit

[Cockpit](https://cockpit-project.org/) 是一个基于Web的服务器图形界面。

## 启用

[running](https://cockpit-project.org/running.html)

```sh
# 安装
dnf install cockpit

# 启用
systemctl enable --now cockpit.socket

# 打开防火墙：
firewall-cmd --add-service=cockpit
firewall-cmd --add-service=cockpit --permanent
```

然后访问：`https://<机器的IP地址>:9090`

## 启用 SSL

cockpit 将从 `/etc/cockpit/ws-certs.d` 目录加载证书。
它将按字母顺序使用具有 `.cert` 或 `.crt` 扩展名的最后一个文件。
该文件应包含一个或多个 OpenSSL 样式的 BEGIN CERTIFICATE 块，用于服务器证书和中间证书颁发机构。

私钥必须包含在具有相同名称但后缀为 `.key` 的单独文件中。密钥不能加密。

如果没有找到证书，则会创建自签名证书并将其存储在 `0-self-signed.cert` 文件中。
在某些平台上，cockpit 还将在该目录中生成 `ca.crt`，该文件可以安全地导入到客户端浏览器中。

cockpit 将以 root 用户身份读取文件，因此它们可以具有严格的权限。

要检查 `cockpit-ws` 将使用哪个证书，请运行以下命令。

```sh
/usr/libexec/cockpit-certificate-ensure --check
```

## 虚拟机

```sh
# 安装扩展模块
# https://github.com/cockpit-project/cockpit-machines
dnf install cockpit-machines
```

## 使用 Nginx 代理

```conf
server {
    listen      443 ssl;
    listen      [::]:443 ssl;
    server_name localhost;

    location / {
        # 需要代理到 Cockpit 的连接
        proxy_pass https://127.0.0.1:9090;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;

        # 运行所必需的 websocket
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        # 将 ETag 标头从 Cockpit 传递给客户端。
        # See: https://github.com/cockpit-project/cockpit/issues/5239
        gzip off;
    }

    # 使用正则的方法匹配其他目录
    location ~* /(file1|file2)/(.*) {
        root   /var/www/html;
        index index.html;
    }
}
```

## 参考文献

- [使用 RHEL 9 web 控制台管理系统](https://access.redhat.com/documentation/zh-cn/red_hat_enterprise_linux/9/html/managing_systems_using_the_rhel_9_web_console/index#doc-wrapper)