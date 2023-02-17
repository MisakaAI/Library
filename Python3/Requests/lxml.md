# lxml

## 安装

```bash
pip install lxml
```

## 使用

```py
import requests
from lxml import etree
res = requests.get("http://www.baidu.com")
html = res.text
root_element = etree.HTML(html)
print(root_element)
```