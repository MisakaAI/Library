# FastAPI

FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.6+ 并基于标准的 Python 类型提示。

## 安装

```sh
# FastAPI
pip install fastapi

# ASGI 服务器
pip install "uvicorn[standard]"
```

## 示例

创建一个 main.py 文件并写入以下内容:

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

## 运行服务器

```sh
uvicorn main:app --reload
```
