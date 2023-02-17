# requests

## 安装

```bash
pip install requests
```

## 使用

```py
import requests

# Get
r = requests.get('https://www.baidu.com/')
print(r.text)

# Post

data = {'name': 'germey', 'age': '25'}
r = requests.post("https://www.baidu.com/", data=data)
print(r.text)

# 添加 headers
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

r = requests.post('https://www.baidu.com/', headers=headers, data=data)

# 获取响应信息
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)

# 文件上传

files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)

# Session
s = requests.Session()
s.get('https://www.baidu.com/')
r = s.get('https://www.baidu.com/')

# SSL 证书验证
response = requests.get('https://www.baidu.com/', verify=False)

# 超时设置
r = requests.get('https://www.baidu.com/', timeout=1)

# 代理设置
proxies = {
  'http': 'http://10.10.10.10:1080',
  'https': 'http://10.10.10.10:1080',
}
requests.get('https://www.baidu.com/', proxies=proxies)
```
