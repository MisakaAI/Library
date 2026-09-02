# llama.cpp

有几种方式可以在你的机器上安装 `llama.cpp`：

- 访问 [https://llama.app](https://llama.app)，并按照页面上的说明进行安装
`curl -LsSf https://llama.app/install.sh | sh`
- 使用 `Docker` 运行 —— 参阅 [Docker 文档](https://github.com/ggml-org/llama.cpp/blob/master/docs/docker.md)
- 从 [Releases 发布页面](https://github.com/ggml-org/llama.cpp/releases) 下载预编译好的二进制文件
- 克隆该仓库并从源码构建 —— 参阅 [构建指南](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)

安装完成后，可以这样使用：

```bash
# 验证安装
llama cli --version

# 直接从 Hugging Face 下载并运行模型
llama cli -hf ggml-org/Qwen3.5-0.8B-GGUF

# 启动兼容 OpenAI API 的服务
llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF

# 运行已经下载完的本地模型 `.gguf` 文件
llama cli -m my-model.gguf
```

## 目录

- [使用 CLI](./CLI.md)
- [运行服务器](./Server.md)
- [网页界面](./Web-UI.md)
- [API 服务器](./API.md)
- [Windows 启动脚本](./start.cmd) `CRLF` `gb2312`

## 与本地编码代理搭配使用

运行 `llama serve`，安装 `pi-llama` 插件并启动 Pi。
它将自动发现您的本地模型。
无需配置，无需 API 密钥。
文件保留在您的机器上，请求绝不会离开它。

```sh
# 1. 运行一个模型
llama serve

# 2. 安装 pi-llama 插件
pi install git:github.com/huggingface/pi-llama

# 3. 运行 Pi，一切就绪
pi
```
