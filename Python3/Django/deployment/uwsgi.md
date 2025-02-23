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
uid=www-data
gid=www-data
module=mysite.wsgi:application
master=True
home=/usr/venv/django
processes=2
threads=4
vacuum=True
logto=/var/log/uwsgi/mysite.log
log-maxsize = 10000
max-requests = 5000
pidfile=/tmp/mysite.pid
socket=/var/www/mysite/uwsgi.sock
```

### 注意事项

```txt
uwsgi.service: Start request repeated too quickly.
uwsgi.service: Failed with result 'protocol'.
Failed to start uwsgi.service - uWSGI HomePage
```

如果`uwsgi`配置文件中配置了`daemonize=/path/uwsgi.log` (uwsgi服务以守护进程运行)
会导致`sytemctl`启动时多次重启而导致启动失败
需改为`logto=/path/uwsgi.log`

如果出现了多次重启导致重启过快的问题，需要先清除失败标记，再启动。

```sh
systemctl reset-failed uwsgi.service
```

## 创建系统服务

创建并编辑 `/etc/systemd/system/uwsgi.service`

```service
[Unit]
Description=uWSGI
After=syslog.target

[Service]
User=www-data
Group=www-data
ExecStart=/usr/local/bin/uwsgi --ini /var/www/mysite/uwsgi.ini
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
