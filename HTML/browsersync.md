# Browsersync

[Browsersync]()能让浏览器实时、快速响应您的文件更改（html、js、css、sass、less等）并自动刷新页面。

## 安装

```sh
# 全局安装
npm install -g browser-sync
```

## 使用

```sh
# 启动 BrowserSync
# 使用 **（表示任意目录）匹配，任意目录下任意.css
browser-sync start --server --files "**/*.html, **/*.css, **/*.js"

# 简化
echo -e alias bwsync=\'browser-sync start --server --files \"**/*.html, **/*.css, **/*.js\"\' >> /etc/zsh/zshrc
```