# Clash

Clash是一款用Go语言开发，可以在Linux/MacOS/Windows等多平台使用的代理工具，配置也非常简单（特别是在Windows平台），支持ss/v*2ray（不支持ssr），支持规则分流（类似于 Surge 的配置）。

- [clash](https://github.com/Dreamacro/clash)
  - [archive](https://web.archive.org/web/20231102080544/https://github.com/Dreamacro/clash/releases)
- [clash for windows](https://github.com/Fndroid/clash_for_windows_pkg)
  - [archive](https://web.archive.org/web/20231030023222/https://github.com/Fndroid/clash_for_windows_pkg/releases)
- [clash for android](https://github.com/Kr328/ClashForAndroid)
  - [archive](https://web.archive.org/web/20231103071433/https://github.com/Kr328/ClashForAndroid)
- [Dashboard](https://github.com/Dreamacro/clash-dashboard)
  - [archive](https://web.archive.org/web/20231017032906/https://github.com/Dreamacro/clash-dashboard)
- [wiki](https://clash.wiki/)

## 下载

Clash项目为开源项目，可以下载各平台的安装包：

从 `Github` 的 [releases](https://github.com/Dreamacro/clash/releases) 中下载对应的版本。

```bash
# 下载
wget -O clash.gz https://github.com/Dreamacro/clash/releases/download/v1.16.0/clash-linux-amd64-v1.16.0.gz

# 解压
gzip -dc clash.gz > /usr/local/bin/clash
chmod +x /usr/local/bin/clash
rm -f clash.gz
```

## 配置

```bash
# 创建配置文件目录
mkdir /etc/clash

# 下载 MMDB 文件
# wget -O /etc/clash/Country.mmdb https://www.sub-speeder.com/client-download/Country.mmdb
wget -O /etc/clash/Country.mmdb https://cdn.jsdelivr.net/gh/Dreamacro/maxmind-geoip@release/Country.mmdb

# 导入已有的Catnet的订阅链接
wget -O /etc/clash/config.yaml <你的订阅链接>

```

### 获取订阅链接

- [获取订阅链接](https://api.nameless13.com/)

选择基础模式，客户端不用动，在URL里面粘贴你的订阅链接，然后点击生成订阅链接。

## 设置系统代理

添加配置文件 `/etc/profile.d/proxy.sh` 并在其中写入如下内容

```bash
export http_proxy="127.0.0.1:7890"
export https_proxy="127.0.0.1:7890"
export no_proxy="localhost, 127.0.0.1"
```

## 防火墙放行端口

```bash
firewall-cmd --zone=public --permanent --add-port=7890/tcp
firewall-cmd --reload
```

## 创建系统服务

创建 `systemd` 脚本，脚本文件路径为 `/etc/systemd/system/clash.service`，内容如下：

```systemd
[Unit]
Description=clash daemon

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/clash -d /etc/clash/
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## 启动服务

```bash
systemctl daemon-reload
systemctl start clash
systemctl enable clash
```

## 配置 WEB UI

```bash
# 克隆项目到 /var/www/clash-dashboard
git clone -b gh-pages --depth 1 https://github.com/Dreamacro/clash-dashboard /var/www/html/clash
# 修改 clash 配置文件中 external-ui 的值为 /var/www/clash-dashboard
# sed -i "s/^#\{0,1\} \{0,1\}external-ui.*/external-ui: \/var\/www\/clash-dashboard/" /etc/clash/config.yaml
# echo 'external-ui: /var/www/html/clash/' >> /etc/clash/config.yaml
# 密钥?
echo "secret: '<你的密钥>'" >> /etc/clash/config.yaml
# 重启服务
systemctl restart clash
```

## 配置定时更新订阅

使用如下脚本填写相关配置项目并放入 `/etc/cron.daily` 目录下，每周自动更新订阅配置文件即可

```bash
#!/usr/bin/env bash

# 订阅链接地址
SUBSCRIBE=""
# web-ui存放目录，留空则保持默认不修改
WEB_UI=""
# API 端口，留空则保持默认不修改
CONTROLLER_API_PROT=""
# API 口令，留空则保持默认不修改
SECRET=""

CLASH_CONFIG="/etc/clash/config.yaml"


if [ -z "${SUBSCRIBE}" ]; then
    echo "Subscription address cannot be empty"
    exit 1
fi

systemctl stop clash

wget --no-proxy -O ${CLASH_CONFIG} ${SUBSCRIBE}

if [ -n "${WEB_UI}" ]; then
# sed -i "s?^#\{0,1\} \{0,1\}external-ui.*?external-ui: ${WEB_UI}?" ${CLASH_CONFIG}
fi

if [ -n "${CONTROLLER_API_PROT}" ]; then
# sed -i "s?^external-controller.*?external-controller: '0.0.0.0:${CONTROLLER_API_PROT}'?" ${CLASH_CONFIG}
sed -i "s?^external-controller.*?external-ui: \"/var/www/clash\"\nexternal-controller: '0.0.0.0:${CONTROLLER_API_PROT}'?" ${CLASH_CONFIG}
fi

if [ -n "${SECRET}" ]; then
sed -i "s?^secret.*?secret: '${SECRET}'?" ${CLASH_CONFIG}
fi

sed -i "s?^mode: .*?mode: global?" ${CLASH_CONFIG}

systemctl start clash
```

上述脚本写入 `/etc/cron.daily/clash.sh` 并配置好相关变量后，保存退出并赋予可执行权限

```bash
chmod 0755 /etc/cron.daily/clash.sh
```
