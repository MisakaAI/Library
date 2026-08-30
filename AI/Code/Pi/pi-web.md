# Pi Web

## 部署

```sh
# 安装 pi-web
npm install -g @agegr/pi-web@latest

# 启动脚本
sudo install -m 755 pi-web-start.sh /usr/local/bin/pi-web-start

# 配置密码和 HTTP Proxy
sudo mkdir /etc/pi-web
sudo cp pi-web.env.example /etc/pi-web/pi-web.env
sudo chown $USER:$USER /etc/pi-web/pi-web.env
sudo chmod 600 /etc/pi-web/pi-web.env

## 一定要配置正确的路径
echo "PI_WEB_BIN='$(command -v pi-web 2>/dev/null)'"
echo "PI_CODING_AGENT_DIR='/home/$USER/.pi/agent'"

# 注册为系统服务
## 特别注意 User=不要写 root，要写运行的普通用户。
sudo cp pi-web.service /etc/systemd/system/pi-web.service
sudo sed -i "s/YOUR_USER/$USER/g" /etc/systemd/system/pi-web.service
sudo cat /etc/systemd/system/pi-web.service
sudo systemctl daemon-reload
sudo systemctl enable --now pi-web
systemctl status pi-web
```

## 远程访问

可基于 Cloudflare Access + Tunnels 实现
