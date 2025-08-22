# Ollama

启动并运行大型语言模型。

```sh
curl -fsSL https://ollama.com/install.sh | sh
# 拉取模型
ollama pull gemma3:4b
# 运行模型
ollama run gemma3:4b
# 显示模型信息
ollama show gemma3:4b
# 删除模型
ollama rm gemma3:4b
# 列出模型
ollama list
# 列出当前加载的模型
ollama ps
# 停止当前正在运行的模型
ollama stop gemma3:4b
```

## REST API

```sh
# Generate a response
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt":"Why is the sky blue?"
}'

# Chat with a model
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}'
```
