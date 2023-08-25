# 请求体

当你需要将数据从客户端（例如浏览器）发送给 API 时，你将其作为「请求体」发送。
请求体是客户端发送给 API 的数据。响应体是 API 发送给客户端的数据。
你的 API 几乎总是要发送响应体。但是客户端并不总是需要发送请求体。

## 导入 Pydantic 的 `BaseModel`

```python
from fastapi import FastAPI

# 从 pydantic 中导入 BaseModel
from pydantic import BaseModel

# 创建数据模型
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
# 使用与声明路径和查询参数的相同方式声明请求体
async def create_item(item: Item):
    return item
```

- 将请求体作为 JSON 读取。
- 转换为相应的类型（在需要时）。
- 校验数据。
  - 如果数据无效，将返回一条清晰易读的错误信息，指出不正确数据的确切位置和内容。
- 将接收的数据赋值到参数 item 中。
  - 由于你已经在函数中将它声明为 Item 类型，你还将获得对于所有属性及其类型的一切编辑器支持（代码补全等）。
- 为你的模型生成 JSON 模式 定义，你还可以在其他任何对你的项目有意义的地方使用它们。
- 这些模式将成为生成的 OpenAPI 模式的一部分，并且被自动化文档 UI 所使用。

## 使用模型

```python
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:

        # 可以直接访问模型对象的所有属性
        price_with_tax = item.price + item.tax

        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

```

## 同时声明

```python
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

# 请求体 + 路径参数
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# 请求体 + 路径参数 + 查询参数
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
```

函数参数将依次按如下规则进行识别：

- 如果在路径中也声明了该参数，它将被用作路径参数。
- 如果参数属于单一类型（比如 `int`、`float`、`str`、`bool` 等）它将被解释为查询参数。
- 如果参数的类型被声明为一个 `Pydantic` 模型，它将被解释为请求体。

