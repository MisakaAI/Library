# 运行服务器

`llama serve` 只需一条命令即可启动快速、轻量的 LLM 推理 HTTP 服务器。它提供：

- [与 OpenAI 兼容的 API](api)（聊天补全、文本补全、嵌入向量等）
- 内置的[网页界面](webui)，用于在浏览器中聊天
- 支持多用户和连续批处理的并行解码

## 启动服务器

```sh
# 从 Hugging Face 仓库启动（自动下载并缓存）
llama serve -hf ggml-org/gemma-4-e4b-it-GGUF:Q4_0

# 从本地 GGUF 文件启动
llama serve -m my-model.gguf
```

默认情况下，服务器监听 `http://127.0.0.1:8080`。在浏览器中打开此地址即可使用网页界面，也可以向该地址发送 API 请求：

```sh
curl http://localhost:8080/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{"messages": [{"role": "user", "content": "你好！"}]}'
```

## 常用配置

```sh
llama serve -m model.gguf \
    -c 16384 \ # 上下文大小（传入 0 使用模型的原生最大值）
    -ngl all \          # GPU 卸载（默认：自动）
    --host 0.0.0.0 \    # 监听所有接口（默认：127.0.0.1）
    --port 8080
```

| 标志                   | 作用                                                                 |
| ---------------------- | -------------------------------------------------------------------- |
| `-c, --ctx-size N`     | 以令牌数表示的上下文大小；`-c 0` 使用模型的完整上下文窗口             |
| `-ngl, --gpu-layers N` | 要卸载到 GPU 的层数（`auto`、`all` 或具体数字）                       |
| `-np, --parallel N`    | 可并发处理请求的服务器槽数量（默认：自动）                            |
| `--host`、`--port`     | 绑定地址和端口（默认 `127.0.0.1:8080`）                               |
| `-a, --alias NAME`     | API 报告的模型名称                                                    |
| `--api-key KEY`        | 要求 API 密钥（多个密钥以逗号分隔）                                   |
| `--no-webui`           | 禁用网页界面，仅提供 API 服务                                          |

每个选项也都有对应的环境变量形式（可在 `llama serve --help` 中查看），这对容器环境很方便：

```yml
services:
  llamacpp-server:
    image: ghcr.io/ggml-org/llama.cpp:server
    ports:
      - '8080:8080'
    volumes:
      - ./models:/models
    environment:
      LLAMA_ARG_HOST: '0.0.0.0'
      LLAMA_ARG_MODEL: /models/my_model.gguf
      LLAMA_ARG_CTX_SIZE: 4096
      LLAMA_ARG_N_PARALLEL: 2
      LLAMA_ARG_PORT: 8080
```

## 为多个用户提供服务

服务器开箱即用地处理并发请求。每个并行 _slot_ 保存一个会话；所有槽共享上下文：

```sh
# 最多同时处理 4 个请求
llama serve -m model.gguf -c 16384 -np 4
```

提示词缓存默认启用，因此对于具有共享前缀的重复请求（例如系统提示词或持续进行的聊天），服务器可以跳过对已经处理过的内容进行重复处理。

## 不止聊天：嵌入向量、重排序和多模态

`llama serve` 可用于为检索工作流提供嵌入向量和重排序模型，也支持多模态模型（图像、音频、PDF）。

```sh
# 嵌入向量服务器（配合 /v1/embeddings 端点使用）
llama serve \
  -hf unsloth/embeddinggemma-300m-GGUF \
  --embedding \
  --port 8080

# 发送文本对
curl http://127.0.0.1:8080/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"input": ["猫坐在垫子上", "一只猫科动物躺在地毯上"]}'
```

同样，也可以按以下方式使用 llama serve 提供重排序模型服务。

```sh
# 重排序模型（配合 /v1/rerank 端点使用）
llama serve -m reranker-model.gguf --rerank

# Hugging Face Hub 上的重排序模型
llama serve \
  -hf ggml-org/Qwen3-reranker-0.6B-Q8_0-GGUF:Q8_0 \
  --embedding --rerank --pooling rank \
  --port 8080

# 查询重排序端点
curl http://127.0.0.1:8080/v1/rerank \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "熊猫是什么？",
    "top_n": 3,
    "documents": [
      "你好",
      "它是一种熊",
      "大熊猫是一种原产于中国的熊科动物。"
    ]
  }'

# {"model":"ggml-org/Qwen3-reranker-0.6B-Q8_0-GGUF:Q8_0","object":"list","usage":{"prompt_tokens":241,"total_tokens":241},"results":[{"index":2,"relevance_score":0.14964470267295837},{"index":1,"relevance_score":0.0058668069541454315},{"index":0,"relevance_score":0.00028348760679364204}]}%
```

你可以在 Hugging Face Hub 上搜索支持 llama.cpp 的[重排序模型](https://huggingface.co/models?pipeline_tag=text-ranking&apps=llama.cpp&sort=trending)和[嵌入向量模型](https://huggingface.co/models?pipeline_tag=sentence-similarity&apps=llama.cpp&sort=trending)。

任何多模态模型都可以像纯文本模型一样运行。

```sh
llama serve -hf ggml-org/gemma-4-e4b-it-GGUF:Q4_0
```

服务启动后，可以通过[网页界面](webui#attachments)的拖放或下拉菜单发送图像，也可以使用标准的 OpenAI 聊天格式发送，详见 [API 文档](api)。

## 推测解码

将模型与小型草稿模型配对，以加快生成速度：

```bash
llama serve -m big-model.gguf -md small-draft-model.gguf --spec-type draft-simple
```

对于包含主模型和草稿模型的模型仓库（以及分别存放它们的仓库），可以按以下方式运行 llama 服务器。

```bash
llama serve -hf ggml-org/gemma-4-e4b-it-GGUF:Q4_0 --hf-repo-draft ggml-org/gemma-4-e4b-it-GGUF:Q4_0 --spec-type draft-mtp
```

## 提供多个模型（路由器模式）

在**不指定模型**的情况下启动时，`llama serve` 会启动一个路由器，按需加载和卸载模型，并将每个请求转发到正确的实例：

```sh
llama serve
```

模型可以来自三个来源：

1. **缓存**——之前通过 `-hf` 下载的所有内容（使用 `llama serve -cl` 查看）
2. **模型目录**——`llama serve --models-dir ./models_directory`
3. **预设文件**——`llama serve --models-preset ./my-models.ini`

注意，发送请求时需要指定模型名称。

```sh
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer no-key" \
  -d '{
    "model": "ggml-org/gemma-3-4b-it-qat-GGUF:Q4_0",
    "messages": [
      {"role": "user", "content": "你好！"}
    ]
  }'
```

可以按以下方式列出可用的模型名称。

```sh
(base) ➜  ~ curl -s http://localhost:8080/v1/models | jq '.data[].id'
"LiquidAI/LFM2.5-230M-GGUF:Q4_K_M"
"ggml-org/Qwen3-Reranker-0.6B-Q8_0-GGUF:Q8_0"
"ggml-org/gemma-3-4b-it-qat-GGUF:Q4_0"
```

服务器会自动加载模型以执行推理。

![路由器](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/llama.cpp/router.png)

完整的标志参考请参阅[服务器 README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)。如需了解端点，请继续阅读 [API 文档](api)；如需了解浏览器界面，请参阅[网页界面指南](webui)。
