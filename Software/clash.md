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
Description=mihomo Daemon, Another Clash Kernel.
After=network.target NetworkManager.service systemd-networkd.service iwd.service

[Service]
Type=simple
LimitNPROC=500
LimitNOFILE=1000000
CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_RAW CAP_NET_BIND_SERVICE CAP_SYS_TIME CAP_SYS_PTRACE CAP_DAC_READ_SEARCH CAP_DAC_OVERRIDE
AmbientCapabilities=CAP_NET_ADMIN CAP_NET_RAW CAP_NET_BIND_SERVICE CAP_SYS_TIME CAP_SYS_PTRACE CAP_DAC_READ_SEARCH CAP_DAC_OVERRIDE
Restart=always
ExecStartPre=/usr/bin/sleep 1s
ExecStart=/usr/local/bin/clash -d /etc/clash
ExecReload=/bin/kill -HUP $MAINPID

[Install]
WantedBy=multi-user.target
```

## 启动服务

```bash
systemctl daemon-reload
systemctl enable --now clash.service
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

```python
#!/usr/bin/env python3
# Subscribe for updates

import subprocess
import signal
import os
import urllib.request
from urllib.parse import quote
from pathlib import Path

target = "clash"
subscription = quote("")
config = "https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online.ini"
yaml = Path("/etc/mihomo/config.yaml")

proc = subprocess.Popen(
    ["/usr/local/bin/subconverter"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    start_new_session=True,
)

try:
    print(f"[{proc.pid}] Subconverter background program running...")
    url = f"http://127.0.0.1:25500/sub?target={target}&url={subscription}&config={config}&insert=false&emoji=true&list=false&tfo=false&scv=true&fdn=false&expand=true&sort=false&new_name=true"
    print("Subscribe for updates: " + url)

    with urllib.request.urlopen(url) as response:
        content = response.read()

    config = content.decode("utf-8")
    config = (
        config.replace("port: 7890\nsocks-port: 7891", "mixed-port: 7890 # HTTP(S) 和 SOCKS 代理混合端口")
        .replace("mode: Rule", "mode: rule")
        .replace("allow-lan: true", "allow-lan: true # 允许局域网连接")
        .replace("log-level: infoe", "log-level: info # 日志等级 silent/error/warning/info/debug")
        .replace(
            "external-controller: :9090",
            """external-ui: '/etc/mihomo/metacubexd-gh-pages'
external-controller: '0.0.0.0:9090'
geox-url:
  geoip: "https://fastly.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geoip.dat"
  geosite: "https://fastly.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geosite.dat"
  mmdb: "https://fastly.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geoip.metadb"
geo-auto-update: false # 是否自动更新 geodata
geo-update-interval: 24 # 更新间隔，单位：小时
ipv6: false # 开启 IPv6 总开关，关闭阻断所有 IPv6 链接和屏蔽 DNS 请求 AAAA 记录
dns:
  enable: true
  ipv6: false
  default-nameserver: [223.5.5.5, 223.6.6.6]
  proxy-server-nameserver: ['https://doh.pub/dns-query', 'https://dns.alidns.com/dns-query', 'https://223.5.5.5/dns-query', 'https://223.6.6.6/dns-query', 'tls://dns.alidns.com', 'tls://223.5.5.5:853', 'tls://223.6.6.6:853']
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  fake-ip-filter: ['*.lan', localhost.ptlogin2.qq.com]
  use-hosts: true
  nameserver: ['https://doh.pub/dns-query', 'https://dns.alidns.com/dns-query', 'https://223.5.5.5/dns-query', 'https://223.6.6.6/dns-query', 'tls://dns.alidns.com', 'tls://223.5.5.5:853', 'tls://223.6.6.6:853']
  fallback: ['https://doh.pub/dns-query', 'https://dns.alidns.com/dns-query', 'https://223.5.5.5/dns-query', 'https://223.6.6.6/dns-query', 'tls://dns.alidns.com', 'tls://223.5.5.5:853', 'tls://223.6.6.6:853']
  fallback-filter: { geoip: true, ipcidr: [240.0.0.0/4, 0.0.0.0/32] }""",
        )
    )

    # 写入文件
    print(f"Subscribe save to {yaml}")
    with yaml.open("w", encoding="utf-8") as f:
        f.write(config)

    # 重启服务
    print("Restart service")
    subprocess.run(
        ["systemctl", "restart", "mihomo.service"],
        capture_output=True,
        text=True,
        check=True,  # 如果返回非零状态码会抛出 CalledProcessError
    )

finally:
    print(f"[{proc.pid}] Python is about to exit; kill this child process.")
    os.killpg(proc.pid, signal.SIGTERM)
```

### 参数说明

调用参数|必要性|示例|解释
-|-|-|-
target|必要|surge&ver=4|指想要生成的配置类型，详见上方 支持类型 中的参数
url|可选|https%3A//www.xxx.com|指机场所提供的订阅链接或代理节点的分享链接，需要经过 URLEncode 处理，可选的前提是在 default_url 中进行指定。也可以使用 data URI。可使用 tag:xxx,https%3A//www.xxx.com 指定该订阅的所有节点归属于xxx分组，用于配置文件中的!!GROUP=XXX 匹配
config|可选|https%3A//www.xxx.com|指 外部配置 的地址 (包含分组和规则部分)，需要经过 URLEncode 处理，详见 外部配置 ，当此参数不存在时使用 主程序目录中的配置文件
insert|可选|true / false|用于设置是否将配置文件中的 insert_url 插入，默认为 true
emoji|可选|true / false|用于设置节点名称是否包含 Emoji，默认为 true
list|可选|true / false|用于输出 Surge Node List 或者 Clash Proxy Provider 或者 Quantumult (X) 的节点订阅 或者 解码后的 SIP002
tfo|可选|true / false|用于开启该订阅链接的 TCP Fast Open，默认为 false
scv|可选|true / false|用于关闭 TLS 节点的证书检查，默认为 false
fdn|可选|true / false|用于过滤目标类型不支持的节点，默认为 true
expand|可选|true / false|用于在 API 端处理或转换 Surge, QuantumultX, Clash 的规则列表，即是否将规则全文置入订阅中，默认为 true，设置为 false 则不会将规则全文写进订阅
sort|可选|true / false|用于对输出的节点或策略组按节点名进行再次排序，默认为 false
new_name|可选|true / false|如果设置为 true，则将启用 Clash 的新组名称 (proxies, proxy-groups, rules)

## 参考文献

- [subconverter](https://github.com/tindy2013/subconverter/blob/master/README-cn.md)
- [metacubex](https://wiki.metacubex.one/)
- [mihomo](https://github.com/MetaCubeX/mihomo)
    - [完整示例](https://github.com/MetaCubeX/mihomo/blob/Meta/docs/config.yaml)
- [metacubexd](https://github.com/MetaCubeX/metacubexd)
