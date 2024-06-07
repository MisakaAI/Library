# 配置静态文件

1. 确保 `INSTALLED_APPS` 包含了 `django.contrib.staticfiles`。
2. 在配置文件中，定义 `STATIC_URL`

    ```py
    STATIC_URL = "static/"
    ```

3. 在模板中，可以使用 `static` 模板标签来使用配置的 `staticfiles` STORAGES 别名构建给定相对路径的 URL

    ```django
    {% load static %}
    <img src="{% static 'my_app/example.jpg' %}" alt="My image">
    ```

4. 将你的静态文件保存至程序中名为 `static` 的目录中。

## 部署静态文件目录

将 `STATIC_ROOT` 配置成你喜欢的目录，在这个目录提供服务。

```py
STATIC_ROOT = "/var/www/example.com/static/"
```

运行 `collectstatic` 管理命令，将静态文件收集至独立目录。

```sh
python manage.py collectstatic
```

选一个 Web 服务器为这些文件提供服务。

- [Nginx](../deployment/uwsgi.md#配置-nginx)
