#!/bin/bash

# 用于 树莓派 安装后的自动配置环境。

# 检测是否是 ROOT 用户

if [ "$UID" != "0" ]; then
	echo "Error, This script must be run as root !"
	exit 0
fi

# 配置变量

username='MisakaAI'
usermail='i@zi-o.com'

# 支持 https

apt install apt-transport-https ca-certificates -y

# 检测软件源是否存在备份，如果不存在则创建。

if [ ! -f /etc/apt/sources.list.bak ]
then
    sudo cp -a /etc/apt/sources.list /etc/apt/sources.list.bak
else
    sudo cp -a /etc/apt/sources.list.bak /etc/apt/sources.list
fi

# 使用 清华大学 源

echo "# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free

deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free

deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free

# deb https://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free

deb https://security.debian.org/debian-security bullseye-security main contrib non-free
# deb-src https://security.debian.org/debian-security bullseye-security main contrib non-free" > /etc/apt/sources.list

# Raspberry 专属软件源

if [ ! -f /etc/apt/sources.list.d/raspi.list.bak ]
then
    sudo cp -a /etc/apt/sources.list.d/raspi.list /etc/apt/sources.list.d/raspi.list.bak
else
    sudo cp -a /etc/apt/sources.list.d/raspi.list.bak /etc/apt/sources.list.d/raspi.list
fi

sudo sed -i "s@http://archive.raspberrypi.org/debian@https://mirrors.tuna.tsinghua.edu.cn/raspberrypi@g" /etc/apt/sources.list.d/raspi.list

# 更新软件源

apt update && apt upgrade -y && apt autoremove -y

# 设置系统时区为 亚洲/上海
# dpkg-reconfigure tzdata
timedatectl set-timezone Asia/Shanghai

# 设置系统语言为 en_US.UTF-8
# dpkg-reconfigure locales
locale-gen zh_CN.UTF-8
locale-gen en_US.UTF-8
localectl set-locale en_US.UTF-8
echo -e "LANG=en_US.UTF-8\nLC_ALL=en_US.UTF-8" > /etc/default/locale

# BBR

cat /etc/sysctl.conf | grep bbr
if [ $? != 0 ]
then
    echo "net.core.default_qdisc = fq" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_congestion_control = bbr" >> /etc/sysctl.conf
    sysctl -p
fi

# C & C++

apt install -y gcc g++ make

# Python3

apt install -y python3 python3-dev python3-pip
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Git
apt install -y git wget curl

git config --global user.name $username
git config --global user.email $usermail

git config --global color.ui true
git config --global push.default simple
git config --global core.autocrlf input

# Vim
apt install -y vim exuberant-ctags

# Vim Config
git clone --depth=1 https://github.com/MisakaAI/vim-config.git
cd vim-config
bash ./install.sh
cd ..
rm -rf vim-config

# SSH
apt install -y ssh openssl

# 防止SSH自动断开
sed -i "s/#TCPKeepAlive yes/TCPKeepAlive yes\nClientAliveInterval 60\nClientAliveCountMax 120/g" /etc/ssh/sshd_config

# ROOT用户可以SSH登录
sed -i "s/#PermitRootLogin prohibit-password/PermitRootLogin yes/g" /etc/ssh/sshd_config

# 重启 SSH 服务
systemctl restart sshd.service

# Zsh
apt install -y zsh zsh-syntax-highlighting zsh-autosuggestions

cat /etc/zsh/zshrc | grep zsh-syntax-highlighting
if [ $? != 0 ]
then
    sh -c 'echo "source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> /etc/zsh/zshrc'
    sh -c 'echo "setopt no_nomatch" >> /etc/zsh/zshrc'
    sh -c 'echo "zstyle \":completion:*\" rehash true" >> /etc/zsh/zshrc'
    sh -c 'echo "plugins=(zsh-autosuggestions)" >> /etc/zsh/zshrc'
fi

# Oh My Zsh
git clone https://mirrors.tuna.tsinghua.edu.cn/git/ohmyzsh.git
cd ohmyzsh/tools
REMOTE=https://mirrors.tuna.tsinghua.edu.cn/git/ohmyzsh.git sh install.sh
cd ../..
rm -rf ohmyzsh

# Other
apt install -y screenfetch htop

# 检验安装结果
echo "----- 检验安装结果 -----"
screenfetch
echo "----- BBR -----"
sysctl net.ipv4.tcp_available_congestion_control
sysctl net.ipv4.tcp_congestion_control
lsmod | grep bbr
echo "----- Python3 -----"
python -V
pip -V
pip config list