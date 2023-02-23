# 安装

本处介绍以 `ubuntu 22.04` 为范例。
RHEL / CentOS / RockyLinux 建议直接使用 `podman`

[install](https://docs.docker.com/desktop/install/linux-install/)

## 卸载旧版本

```bash
sudo apt-get remove docker \
               docker-engine \
               docker.io
```

## 使用 APT 安装

```bash
$ sudo apt-get update

$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

## 安装 Docker

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### 使用脚本自动安装

```bash
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh --mirror Aliyun
```

## 启动 Docker

```bash
sudo systemctl enable docker
sudo systemctl start docker
```