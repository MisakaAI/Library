# dotenv

从 `.env` 文件中读取键值对，并可以将它们设置为环境变量。

- [python-dotenv](https://github.com/theskumar/python-dotenv)

## 安装

```sh
pip install python-dotenv
```

## 通过环境变量读取配置

```.env
DOMAIN=example.org
```

```sh
import os
from dotenv import load_dotenv
load_dotenv()

DOMAIN = os.getenv("DOMAIN")
print(DOMAIN)
```

## 在不改变环境的情况下加载配置

```py
from dotenv import dotenv_values

# config = dotenv_values(".env")
config = dotenv_values()

print(config["DOMAIN"])
```
