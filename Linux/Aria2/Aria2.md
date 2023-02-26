# Aria2

[aria2](https://github.com/aria2/aria2)
[AriaNg](https://github.com/mayswind/AriaNg/)

## Install

```bash
# 设置版本号
AriaNG_Version=1.1.7
AriaNG_Download="https://github.com/mayswind/AriaNg/releases/download/$AriaNG_Version/AriaNg-$AriaNG_Version.zip"

# 创建下载目录
mkdir /var/download

# 安装 Aria2
apt install -y aria2 unzip

# 创建配置目录
mkdir /etc/aria2

# 复制配置文件到目录
cp aria2.conf /etc/aria2/aria2.conf

# 创建缓存文件
touch /etc/aria2/aria2.session

# 修改文件权限
chmod 644 /etc/aria2/*

# 创建服务
cp aria2.service /etc/systemd/system/aria2.service
# 启动服务
systemctl start aria2.service
# 开机启动
systemctl enable aria2.service
```
