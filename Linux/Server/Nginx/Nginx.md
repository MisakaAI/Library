# Nginx

## 仅ssl访问下使用http协议访问自动跳转至https

```conf
# 将 497 错误重定向到 https 协议
proxy_set_header X-Real-Port $remote_port;
error_page 497 https://$host:$remote_port$request_uri;
```
