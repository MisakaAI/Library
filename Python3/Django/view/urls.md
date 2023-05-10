# Urls

`News/urls.py`

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
]
```

`index/urls.py`

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
]
```