# django-cors-headers

用于处理跨域资源共享（CORS）所需的服务器头。

## 安装

```sh
pip install django-cors-headers
```

修改 `settings.py`

```py
# 将其添加到已安装的应用程序中
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
```

## 