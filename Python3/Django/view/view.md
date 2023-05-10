# 视图

编辑 `<app name>/views.py`

```python
from django.http import HttpResponse

# 直接输出
def index(request):
    return HttpResponse("Hello, world.")

# JSON
from django.http import JsonResponse

def index(request):
    return JsonResponse({'foo': 'bar'})

# render
from django.shortcuts import render
from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
```