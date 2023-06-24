# uwsgi

假设目录为 `/var/www/mysite`

```sh
# 即
cd /var/www
django-admin startproject mysite
```

## 安装 uwsgi

```sh
pip install uwsgi
```

## 创建配置文件

创建并编辑 `/var/www/mysite/uwsgi.ini`

```ini
[uwsgi]
chdir=/var/www/mysite
wsgi-file=mysite/wsgi.py
processes=1
threads=1
module=mysite.wsgi:application
master=True
vacuum=True
pidfile=/var/www/djnago/uwsgi.pid
logto=/var/www/mysite/uwsgi.log
log-maxsize = 100000
max-requests = 1000
uid=nginx
gid=nginx
socket=/var/www/mysite/uwsgi.sock
```

## 创建系统服务

创建并编辑 `/etc/systemd/system/uwsgi.service`

```service
[Unit]
Description=uWSGI Emperor
After=syslog.target

[Service]
User=nginx
Group=nginx
ExecStart=/usr/local/bin/uwsgi --ini /var/www/mysite/uwsgi.ini

# Requires systemd version 211 or newer
RuntimeDirectory=uwsgi
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

启动服务 & 设置开机启动

```sh
# 可以先进行测试，看是否可以运行
/usr/local/bin/uwsgi --ini /var/www/mysite/uwsgi.ini

# 重新加载系统服务
systemctl daemon-reload
# 启动系统服务，并设置为开机启动
systemctl enable --now uwsgi.service
```

## 收集 STATIC 文件到 STATIC_ROOT 目录中

```sh
cd /var/www/mysite
python manage.py collectstatic
```

## 配置 Nginx

修改 `nginx.conf` 文件，通常为：`/etc/nginx/conf.d/default.conf`

```conf
server {
    listen 80;
    charset utf-8;

    location / {
        uwsgi_pass   unix://{Django Pwd}/uwsgi.sock;
        include     /etc/nginx/uwsgi_params;
    }

    client_max_body_size 100M;

    location /static {
        alias $(STATIC_ROOT);
    }
}
```

重启 Nginx

```sh
systemctl restart nginx
```






