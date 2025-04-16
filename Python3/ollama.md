# 在 Python 中使用 Ollama

## 安装

```sh
pip install ollama
```

## 使用

```py
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])

# or access fields directly from the response object
# 或直接从响应对象访问字段
print(response.message.content)
```

```py
from ollama import generate

response = generate('gemma3', 'Why is the sky blue?')
print(response['response'])
```

### 流式响应

```py
from ollama import chat

stream = chat(
    model='gemma3',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
```

## API

```py
# 本地模型列表
ollama.list()

# 拉取模型
ollama.pull('gemma3')

# 删除模型
ollama.delete('gemma3')

# 进程
ollama.ps()

# 显示模型信息
ollama.show('gemma3')

# 对话
ollama.chat(model='gemma3', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])

# 生成
ollama.generate(model='gemma3', prompt='Why is the sky blue?')
```

## 参考文献

- [ollama-python](https://github.com/ollama/ollama-python)
