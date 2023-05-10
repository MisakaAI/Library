# 模型

## 创建模型

编辑 `<app name>/models.py`

```python
from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```

然后，应用数据模型

```sh
python manage.py makemigrations
python manage.py migrate
```

## 使用 API 访问数据

```python
# 导入创建的模型
from news.models import Article, Reporter

# 获取全部的对象
Reporter.objects.all()

# 创建一个新的对象
r = Reporter(full_name='John Smith')

# 将对象保存到数据库中。
r.save()

# 保存后将产生一个ID
r.id

# 在Python对象上，字段表示为属性。
r.full_name

# 数据库查询 API
Reporter.objects.get(id=1)
Reporter.objects.get(full_name__startswith='John')

# a = Article(pub_date=date.today(), headline='Django is cool', content='Yeah.', reporter=r)
# a.save()
# Article.objects.filter(reporter__full_name__startswith='John')

# 删除对象
r.delete()
```