# API 服务器

`llama serve` 在 `http://localhost:8080` 上以多种格式提供 REST API：

- `/v1/...` 下与 **OpenAI 兼容**的端点，可与现有的 OpenAI SDK 和应用配合使用
- 与 **Anthropic 兼容**的 `/v1/messages` 端点
- 具备额外能力的 **llama.cpp 端点**（更底层的选项）

如果服务器使用 `--api-key` 启动，请将其作为 Bearer 令牌传入：`Authorization: Bearer YOUR_KEY`。

## 聊天补全

`POST /v1/chat/completions` 是最常用的端点。它接受标准的 OpenAI 聊天格式，并可通过 `"stream": true` 启用流式输出：

```sh
curl http://localhost:8080/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "messages": [
            {"role": "system", "content": "你是一个乐于助人的助手。"},
            {"role": "user", "content": "写一首关于 Python 异常的打油诗"}
        ]
    }'
```

或者使用 OpenAI Python SDK——只需修改基础 URL：

```python
import openai

client = openai.OpenAI(base_url="http://localhost:8080/v1", api_key="no-key-required")

completion = client.chat.completions.create(
    model="local-model",
    messages=[{"role": "user", "content": "写一首关于 Python 异常的打油诗"}],
)
print(completion.choices[0].message.content)
```

除了 OpenAI 参数外，同一个请求体还接受 llama.cpp 专用的生成参数。

### 结构化输出

可以将响应限制为有效 JSON，或限制为特定的模式：

```json
{
	"messages": [{ "role": "user", "content": "提取姓名和日期：..." }],
	"response_format": {
		"type": "json_schema",
		"schema": {
			"type": "object",
			"properties": {
				"name": { "type": "string" },
				"date": { "type": "string" }
			},
			"required": ["name", "date"]
		}
	}
}
```

对于自由格式的 JSON，请使用 `{"type": "json_object"}`。

### 工具调用

OpenAI 风格的函数调用适用于原生支持工具调用格式的模型；对于其余模型，则使用通用的回退机制。像平常一样传入 `tools` 和 `tool_choice`。支持的模型系列请参阅[函数调用文档](https://github.com/ggml-org/llama.cpp/blob/master/docs/function-calling.md)。

### 多模态输入

视觉和音频模型接受消息中带类型的内容部分：

```json
{
	"messages": [
		{
			"role": "user",
			"content": [
				{ "type": "text", "text": "这张图片里有什么？" },
				{ "type": "image_url", "image_url": { "url": "https://example.com/photo.jpg" } }
			]
		}
	]
}
```

`image_url.url` 可以是远程 URL 或 Base64 数据 URI；对于音频文件，`input_audio` 的用法相同。

### 推理模型

对于思考模型，解析后的推理内容会在 `message.reasoning_content` 中返回，与 `message.content` 中的最终答案分开（可通过 `--reasoning-format` 配置）。

### 时间和用量

响应包含标准的 OpenAI `usage` 对象，以及 llama.cpp 的 `timings` 对象，其中提供每秒生成令牌数统计和从缓存中复用的提示词令牌数量（`cache_n`），便于跟踪性能和上下文用量。

## 其他与 OpenAI 兼容的端点

| 端点                    | 用途                                                                 |
| ---------------------- | -------------------------------------------------------------------- |
| `POST /v1/completions` | 根据原始 `prompt` 进行文本补全                                         |
| `POST /v1/responses`   | OpenAI Responses API（内部转换为聊天补全）                              |
| `POST /v1/embeddings`  | 生成嵌入向量——需要启用池化的模型（参见[服务文档](serve)）                 |
| `POST /v1/rerank`      | 根据查询为文档排序——需要重排序模型                                      |
| `GET /v1/models`       | 模型元数据（ID、上下文大小、参数）                                       |

`/v1/models` 报告的模型 `id` 默认为模型文件路径；可以使用 `--alias` 设置易读的名称。

## 与 Anthropic 兼容的端点

`POST /v1/messages` 接受 Anthropic Messages API 格式，包括 `system`、`stop_sequences`、流式输出和工具使用，因此 Anthropic SDK 及应用也可以指向 llama serve：

```sh
curl http://localhost:8080/v1/messages \
    -H "Content-Type: application/json" \
    -H "x-api-key: your-api-key" \
    -d '{
        "model": "local-model",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": "你好！"}]
        }'
```

`POST /v1/messages/count_tokens` 可以在不生成内容的情况下统计输入令牌数。

## 原生端点

这些端点提供 OpenAI 接口之外的 llama.cpp 功能：

| 端点                                         | 用途                                                                                                                                     |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `GET /health`                                | 存活检查：就绪时返回 `200`，加载期间返回 `503`                                                                                           |
| `POST /completion`                           | 使用完整 llama.cpp 选项集进行原生补全（令牌数组、`n_probs` 对数概率、`id_slot` 固定、每个请求的 LoRA 缩放值等）                         |
| `POST /tokenize` / `POST /detokenize`        | 在文本和令牌之间进行转换                                                                                                                |
| `POST /apply-template`                       | 应用模型的聊天模板，但不运行推理                                                                                                        |
| `POST /infill`                               | 根据 `input_prefix` 和 `input_suffix` 进行中间填充代码补全                                                                                |
| `GET /props`                                 | 服务器和模型属性（上下文大小、聊天模板、多模态类型）                                                                                    |
| `GET /slots`                                 | 每个处理槽的当前状态                                                                                                                     |
| `GET /metrics`                               | Prometheus 指标（需要 `--metrics`）                                                                                                      |
| `GET /lora-adapters` / `POST /lora-adapters` | 在运行时列出并设置 LoRA 适配器的缩放值                                                                                                   |

一个最小的原生补全请求：

```sh
curl http://localhost:8080/completion \
    -H "Content-Type: application/json" \
    -d '{"prompt": "构建网站可以分为 10 个简单步骤：", "n_predict": 128}'
```

## 路由器模式

在[服务多个模型](serve)时，同一个 API 会根据模型名称路由请求——模型名称可以放在 POST 请求体的 `"model"` 字段中，也可以作为 GET 端点的 `?model=` 查询参数。`GET /models` 会列出所有可用模型及其加载状态和多模态类型，`POST /models/load` / `POST /models/unload` 则用于显式管理模型。

## 错误

错误采用 OpenAI 格式：

```json
{
	"error": {
		"code": 401,
		"message": "API 密钥无效",
		"type": "authentication_error"
	}
}
```

关于完整的请求/响应模式以及每个端点的所有选项，请参阅[服务器 README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)。
