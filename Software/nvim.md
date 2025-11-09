# Neovim

- [Neovim](https://neovim.io/)

## 安装

```sh
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz
sudo rm -rf /opt/nvim-linux-x86_64
sudo tar -C /opt -xzf nvim-linux-x86_64.tar.gz

echo 'export PATH="$PATH:/opt/nvim-linux-x86_64/bin"' >> /etc/zsh/zshrc
echo "alias vim='nvim'" >> /etc/zsh/zshrc
source /etc/zsh/zshrc

# 创建配置文件
mkdir ~/.config/nvim/
touch ~/.config/nvim/init.lua

# 配置代理
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
git config --global http.proxy 'socks5://127.0.0.1:7890'
git config --global https.proxy 'socks5://127.0.0.1:7890'

# 安装插件管理器
git clone https://github.com/folke/lazy.nvim ~/.local/share/nvim/lazy/lazy.nvim

# Python LSP 服务器
npm install -g pyright
pyright --version

# Python 格式化 / 调试
# sudo pip install --break-system-packages ruff debugpy
pip install ruff debugpy
ruff --version
debugpy --version
```

## 配置

配置文件目录 `~/.config/nvim/`
配置文件 [init.lua](init.lua)

文件/目录|说明
-|-
init.lua|主配置文件（Neovim 用 Lua 配置，而不是 vimscript）
lua/|存放模块化配置（推荐方式）
plugin/|插件配置或脚本
lazy-lock.json|插件锁定文件（由插件管理器生成）
