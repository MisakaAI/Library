# BeautifulSoup

## 安装

```bash
pip install beautifulsoup4
```

## 使用

```py
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
soup.find(text="bad")
soup.i

soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "xml")
print(soup.prettify())
```

## 参考文献

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [中文文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)
