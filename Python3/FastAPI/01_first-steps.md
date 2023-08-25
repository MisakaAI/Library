# 第一步

```python
# 导入 FastAPI
from fastapi import FastAPI

# 创建一个 FastAPI「实例」
app = FastAPI()

# 创建一个路径操作
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

- **实例**：是 `app`。
- **操作**：是 `get`。
- **路径**：是 `/`。
- **函数**：是位于「装饰器」下方的函数（位于 `@app.get("/")` 下方）。
- **返回**：`return` 返回内容。

## 启动

```sh
uvicorn main:app --reload
```

`uvicorn main:app` 命令含义如下:

- **main**：main.py 文件（一个 Python「模块」）。
- **app**：在 main.py 文件中通过 app = FastAPI() 创建的对象。
- **--reload**：让服务器在更新代码后重新启动。仅在开发时使用该选项。

## 查看

[API](http://127.0.0.1:8000)
[交互式 API 文档](http://127.0.0.1:8000/docs)
[可选的 API 文档](http://127.0.0.1:8000/redoc)
[OpenAPI](http://127.0.0.1:8000/openapi.json)

## 操作

常见的操作：

- 获取：`@app.get()` 用于从服务器获取资源。
- 发送：`@app.post()` 用于向服务器提交数据，通常用于创建新资源。
- 更新：`@app.put()` 用于向服务器更新资源。
- 删除：`@app.delete()` 用于请求服务器删除指定的资源。

以及更少见的：

- 选项：`@app.options()` 用于请求服务器删除指定的资源。
- 头部：`@app.head()` 用于请求服务器删除指定的资源。
- 部分更新：`@app.patch()` 类似于PUT请求，但用于部分更新资源，即只发送需要更新的部分。
- 跟踪：`@app.trace()` 用于在请求-响应链上执行追踪诊断。它允许客户端获取发送到服务器的请求的副本，以便进行故障排除或调试。
