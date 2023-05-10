# 管理

```bash
# 创建一个管理员账号
python manage.py createsuperuser
```

## 管理模型

编辑 `<app name>/admin.py`

```python
from django.contrib import admin
from . import models

admin.site.register(models.Article)
```