# 创建一个 Django 应用

```bash
# 创建项目
django-admin startproject <project>

# 创建应用
python manage.py startapp <app>

# 用于开发的简易服务器，默认端口 8000
python manage.py runserver

# 更换端口 & 监听所有服务器的公开IP
python manage.py runserver 0.0.0.0 8080
```

## 数据库配置

[数据库配置](https://docs.djangoproject.com/zh-hans/4.2/ref/settings/#databases)

修改 `<project>/settings.py`

```python
# SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PostgreSQL
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

- ENGINE：可以使用`django.db.backends.sqlite3` `django.db.backends.postgresql` `django.db.backends.mysql` `django.db.backends.oracle`

## 创建模型

1. 编辑 `<app>/models.py` 文件

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
```

2. 激活模型

编辑 `<project>/settings.py` 文件

```python
INSTALLED_APPS = [
    "<app>.apps.<App>Config",
    "django.contrib.admin",
    ...
]
```

3. 根据模型在数据库中创建表

```bash
# 为模型的改变生成迁移文件
python manage.py makemigrations <app>

# 来应用数据库迁移，在数据库里创建新定义的模型的数据表
python manage.py migrate
```