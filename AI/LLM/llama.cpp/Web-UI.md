# 网页界面

llama.cpp 在 `llama serve` 中内置了现代化的聊天界面，支持多模态输入、MCP 等功能。

## 开始使用

使用模型启动服务器，然后在浏览器中打开它：

```sh
llama serve -hf ggml-org/gemma-4-e4b-it-GGUF:Q4_0 -c 0
```

然后访问 http://localhost:8080 开始聊天。如果服务器无法绑定 8080 端口，请通过 `--port 8081` 使用其他端口。

一些启动提示：

- `-c 0` 使用模型的完整上下文窗口。
- 用户可以在设置面板中针对每个会话覆盖参数。
- 若要让网络中的其他设备访问 WebUI，请添加 `--host 0.0.0.0`（例如，在笔记本电脑上远程提供模型服务并访问 WebUI）。

## 聊天

聊天界面会实时流式传输响应，并渲染丰富的内容：

- **Markdown：**支持表格、列表和语法高亮的代码块。
- **数学公式：**使用 KaTeX 渲染 LaTeX 表达式。
- **推理：**思考模型会在独立于答案的可折叠区域中显示推理过程。你可以在设置中切换其可见性。
- **HTML/JS 预览：**生成的 Web 代码可以直接在页面中渲染，以便立即查看效果。

![丰富的 HTML 输出](https://huggingface.co/buckets/ggml-org/docs-media/resolve/llama-html.mp4)

## 附件

通过媒体下拉菜单或拖放将文件添加到会话中：

- **图像/PDF：**供视觉语言模型使用（JPEG、PNG、GIF、WebP、SVG、PDF）
- **音频：**供支持音频输入的模型使用，格式为 MP3/WAV

界面了解每个模型的能力，因此会阻止将图像发送给纯文本模型等操作。

![多模态输入](https://huggingface.co/buckets/ggml-org/docs-media/resolve/llama-mm.mp4)

## 管理会话

- **分支：**编辑之前的任意消息或重新生成任意响应，即可从该处创建会话分支；可以自由地在分支之间切换，不会丢失任何内容
- **搜索：**按标题或内容查找会话
- **导入/导出：**将会话备份或分享为 JSON 文件

## 结构化输出

你可以在设置中提供自定义 JSON 模式，以约束模型的响应。这对于发票提取或数据解析等任务很有用，因为这些任务每次都需要机器可读的输出。

在 WebUI 中选择：`Settings → Developer → Custom JSON`，然后填入你的模式：

```json
{
    "json_schema": {
        "type": "object",
        "properties": {
            "sentiment": { "type": "string", "enum": ["positive", "neutral", "negative"] },
            "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
            "summary": { "type": "string", "maxLength": 200 }
        },
        "required": ["sentiment", "confidence", "summary"]
    }
}
```

## 多个模型

当服务器运行在[路由器模式](serve)下（不指定模型启动）时，界面会显示包含已加载模型和可用模型的模型选择器。选择模型后会自动加载它；重新生成响应时，甚至可以在会话中途切换模型。

## 自定义

可以在启动时通过 `--ui-config` 设置默认的界面偏好（下面的配置会将主题设为深色、使用 Markdown 渲染用户消息，并将长消息转换为文件附件）。

```sh
llama serve -hf ggml-org/gemma-4-e4b-it-GGUF:Q4_0 --ui-config '{"theme": "dark", "pasteLongTextToFileLen": 0, "renderUserContentAsMarkdown": true}'
```

![界面选项](https://huggingface.co/buckets/ggml-org/docs-media/resolve/ui_setting.png)

关于该界面的设计背景和更多使用示例，请参阅 GitHub 上的 [WebUI 指南讨论](https://github.com/ggml-org/llama.cpp/discussions/16938)。
