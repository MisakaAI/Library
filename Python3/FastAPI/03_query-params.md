# 查询参数

声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数

```python
from fastapi import FastAPI
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

```

例如，在 `http://127.0.0.1:8000/items/?skip=0&limit=10` 中

- `skip`：对应的值为 `0`
- `limit`：对应的值为 `10`

## 多个路径和查询参数

你可以同时声明多个路径参数和查询参数，FastAPI 能够识别它们。
而且你不需要以任何特定的顺序来声明。
它们将通过名称被检测到：

```python
from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

```

## 必需查询参数

当你为非路径参数声明了默认值时（目前而言，我们所知道的仅有查询参数），则该参数不是必需的。
如果你不想添加一个特定的值，而只是想使该参数成为可选的，则将默认值设置为 `None`。
但当你想让一个查询参数成为必需的，不声明任何默认值就可以

## 查询参数类型转换

声明 `bool` 类型，它们将被自动转换：

```python
from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, short: bool = False):
    item = {"item_id": item_id}
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

```

访问：

```txt
http://127.0.0.1:8000/items/foo?short=1
http://127.0.0.1:8000/items/foo?short=True
http://127.0.0.1:8000/items/foo?short=true
http://127.0.0.1:8000/items/foo?short=on
http://127.0.0.1:8000/items/foo?short=yes
```

或任何其他的变体形式（大写，首字母大写等等），你的函数接收的 short 参数都会是布尔值 True。
对于值为 False 的情况也是一样的。
