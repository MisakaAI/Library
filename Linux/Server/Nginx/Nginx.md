# Nginx

## 仅ssl访问下使用http协议访问自动跳转至https

```conf
# 将 497 错误重定向到 https 协议
proxy_set_header X-Real-Port $remote_port;
error_page 497 https://$host:$remote_port$request_uri;
```

## Config

### gzip

```conf
    gzip on;

    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_buffers 16 8k;
    gzip_http_version 1.1;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
```

### ssl

```conf
server {
    listen      443 ssl;
    listen      [::]:443 ssl;
    server_name localhost;

    ssl_certificate /etc/ssl/1.crt;
    ssl_certificate_key /etc/ssl/1.key;

    ssl_session_timeout 30m;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
    ssl_prefer_server_ciphers on;
    ssl_session_cache  builtin:1000  shared:SSL:10m;
}

server {
    listen 80;
    server_name localhost;
    return 301 https://$host$request_uri;
}
```

### php

```conf
# 定义反向代理服务器
upstream php-fpm {
    server unix:/run/php-fpm/www.sock;
}
```

```conf
# 定义 .php 或 。phar 结尾文件的处理方式
# 
location ~ \.(php|phar)(/.*)?$ {
    # 这个指令将$fastcgi_script_name变量拆分成两个部分：一个是PHP脚本的实际路径，另一个是额外的URL路径信息（如果存在）。
    # 这个指令将使用正则表达式来匹配路径信息，将其拆分为两个变量：$fastcgi_script_name和$fastcgi_path_info。
    # 这样可以确保Nginx正确地将请求转发给PHP-FPM，以便PHP-FPM能够正确地解析脚本路径和额外的URL路径信息。
    fastcgi_split_path_info ^(.+\.(?:php|phar))(/.*)$;

    # 告诉Nginx要拦截FastCGI服务器返回的错误，并根据Nginx的错误处理机制进行处理。
    # 这可以确保当PHP脚本返回错误时，Nginx能够正确地处理错误信息并向客户端发送错误响应。
    fastcgi_intercept_errors on;
    # 定义了默认的索引文件名称，当请求的URL路径没有指定具体的文件名时，Nginx将使用这个指令定义的文件名作为索引文件名称。
    # 这里，index.php是默认的索引文件。
    fastcgi_index  index.php;
    # 这个指令将包含一个外部的FastCGI参数文件，其中包含一些常用的FastCGI参数和变量。
    # 这可以确保Nginx正确地将请求转发给PHP-FPM，并将适当的FastCGI参数传递给PHP-FPM。
    include        fastcgi_params;
    # 这个指令将FastCGI参数SCRIPT_FILENAME设置为请求文件的完整路径。
    # 这个路径由$document_root和$fastcgi_script_name变量组成。
    # 这个指令告诉PHP-FPM在哪里查找脚本文件。
    fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
    # 这个指令将FastCGI参数PATH_INFO设置为从fastcgi_split_path_info指令中拆分出来的额外URL路径信息。
    # 这个指令告诉PHP-FPM如何处理额外的URL路径信息。
    fastcgi_param  PATH_INFO $fastcgi_path_info;
    # 这个指令将客户端请求转发给名为php-fpm的upstream组，该组定义了后端的PHP-FPM服务器。
    # 这个指令告诉Nginx将请求转发给PHP-FPM进行处理。
    fastcgi_pass   php-fpm;
}
```