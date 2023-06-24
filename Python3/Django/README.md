# Django

[Django](https://www.djangoproject.com/)是一个开放源代码的 Web 应用框架，由 Python 写成。
这里根据[官方文档](https://docs.djangoproject.com/zh-hans/4.2/)整理了一些日常开发中常用的内容，方便查询。

## 快速入门

- [安装](quick/install.md)
- [创建项目](quick/creating.md)

```sh
# Django
pip install django

# Django 跨域
# https://pypi.org/project/django-cors-headers/
pip install django-cors-headers

# psycopg3 用于连接 PostgreSQL 数据库
pip install "psycopg[binary]"

# uwsgi
# dnf install python3-devel
pip install uwsgi

# 创建项目
django-admin startproject <project name>

# 创建应用
python manage.py startapp <app name>

# 用于开发的简易服务器
python manage.py runserver 0.0.0.0 8000

# 为模型的改变生成迁移文件
# python manage.py makemigrations <app name>
python manage.py makemigrations

# 来应用数据库迁移，在数据库里创建新定义的模型的数据表
python manage.py migrate

# 创建一个管理员账号
python manage.py createsuperuser
```

## 模型层

- [模型](model/models.md)
- [模型字段](model/model-field-types.md)

## 视图层

- [视图](view/view.md)
- [URL调度器](view/urls.md)
- [静态文件](view/staticfiles.md)

## 模板层

- [模板](template/template.md)

## 表单

- [表单](form/forms.md)

## 部署

- [Apache 部署](deployment/mod_wsgi.md)
- [Nginx 部署](deployment/uwsgi.md)

## 管理

- [管理站点](admin/admin.md)