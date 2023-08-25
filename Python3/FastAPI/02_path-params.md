# 路径参数

```python
from fastapi import FastAPI
app = FastAPI()

# 使用与 Python 格式化字符串相同的语法来声明路径"参数"或"变量"
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

## 有类型的路径参数

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

### 数据转换

运行示例并打开浏览器访问 `http://127.0.0.1:8000/items/3`

```json
{"item_id":3}
```

### 数据校验

运行示例并打开浏览器访问 `http://127.0.0.1:8000/items/foo`

```json
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```

因为路径参数 `item_id` 传入的值为 `"foo"`，它不是一个 `int`。

## 路径顺序

比如 `/users/me`，我们假设它用来获取关于当前用户的数据。
然后，你还可以使用路径 `/users/{user_id}` 来通过用户 ID 获取关于特定用户的数据。
由于路径操作是按顺序依次运行的，你需要确保路径 /users/me 声明在路径 /users/{user_id}之前

## 预设值

可以使用标准的 Python `Enum` 类型

### 创建一个 `Enum` 类

```python
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

## 包含路径的路径参数

假设你有一个路径操作，它的路径为 `/files/{file_path}`。
但是你需要 `file_path` 自身也包含路径，比如 `home/johndoe/myfile.txt`。
因此，该文件的URL将类似于这样：`/files/home/johndoe/myfile.txt`。

OpenAPI 不支持任何方式去声明路径参数以在其内部包含路径，因为这可能会导致难以测试和定义的情况出现。
不过，你仍然可以通过 Starlette 的一个内部工具在 FastAPI 中实现它。

### 路径转换器

你可以使用直接来自 Starlette 的选项来声明一个包含路径的路径参数：
`/files/{file_path:path}`

在这种情况下，参数的名称为 `file_path`，结尾部分的 `:path` 说明该参数应匹配任意的路径。

因此，你可以这样使用它：

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```
