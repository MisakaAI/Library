# 创建一个 Django 应用

```bash
# 创建项目
django-admin startproject <project>

# 创建应用
python manage.py startapp <app>
```

## 视图

```
# 在数据库中创建一些表
python manage.py migrate

# 检测你对模型文件的修改，并且把修改的部分储存为一次迁移。
python manage.py makemigrations <app>
```

## 管理

```
# 创建一个管理员账号
python manage.py createsuperuser
```

## 数据库配置

[数据库配置](https://docs.djangoproject.com/zh-hans/4.1/ref/settings/)

`mysite/settings.py`

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

```