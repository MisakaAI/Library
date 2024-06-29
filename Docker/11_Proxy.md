# 使用代理

## 在 Docker 镜像的拉取中使用代理

1. 为 Docker 服务创建 systemd 目录：

```sh
sudo mkdir -p /etc/systemd/system/docker.service.d
```

2. 创建一个名为 `/etc/systemd/system/docker.service.d/http-proxy.conf` 的文件，添加 `HTTP_PROXY` 环境变量：

```conf
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:7890"
Environment="HTTPS_PROXY=http://127.0.0.1:7890"
```

3. 应用更改并重新启动 Docker

```sh
sudo systemctl daemon-reload
sudo systemctl restart docker
```

4. 验证配置是否已加载并与所做的更改匹配

```sh
sudo systemctl show --property=Environment docker
# Environment=HTTP_PROXY=http://proxy.example.com:3128 HTTPS_PROXY=https://proxy.example.com:3129 NO_PROXY=localhost,127.0.0.1,docker-registry.example.com,.corp
```

## 在 Docker 容器的运行中使用代理

编辑 `~/.docker/config.json`

```json
{
  "proxies": {
    "http-proxy": "http://127.0.0.1:7890",
    "https-proxy": "https://127.0.0.1:7890",
    "no-proxy": "localhost,127.0.0.0/8"
  }
}
```

更改配置文件后，重新启动守护程序以使代理配置生效：

```sh
sudo systemctl restart docker
```

## 参考文献

- [Configure the daemon to use a proxy](https://docs.docker.com/config/daemon/proxy/#systemd-unit-file)
