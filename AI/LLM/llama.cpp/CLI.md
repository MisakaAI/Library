# 使用 CLI

`llama cli` 是 llama.cpp 的终端前端：一个用于交互式聊天以及试验模型、采样设置、语法和多模态输入的实验场。

## 基本用法

指定一个模型（可以是本地文件或 Hugging Face 仓库），然后开始聊天：

```sh
# 从 Hugging Face 下载（首次运行后会缓存）
llama cli -hf unsloth/gemma-4-E4B-it-GGUF:Q4_0

# 本地 GGUF 文件
llama cli -m my-model.gguf
```

你将看到可用的命令以及针对模型的输入提示。

![llama cli 输出](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/llama.cpp/llama-cli.png)

一些实用提示：

```sh
# 设置系统提示词
llama cli -m model.gguf -sys "你是一个简洁的助手，请用项目符号回答问题。"

# 提出一个问题，答案完成后退出
llama cli -m model.gguf -st -p "给我一个巴克拉瓦的食谱"
```

## 控制生成

采样参数会影响模型生成文本的方式。llama.cpp 会根据所用模型选择合理的默认值，但你也可以自行尝试并调整这些参数：

```sh
llama cli -hf ggml-org/gemma-4-e4b-it-GGUF:Q4_0 --temp 0.2 --top-k 40 --top-p 0.95
```

| 标志                 | 默认值  | 作用                                           |
| -------------------- | ------- | ---------------------------------------------- |
| `--temp N`           | `0.8`   | 随机性；值越低，结果越确定                     |
| `--top-k N`          | `40`    | 仅从最有可能的 K 个令牌中采样                  |
| `--top-p N`          | `0.95`  | 核采样的概率质量                               |
| `--min-p N`          | `0.05`  | 丢弃相对概率低于此值的令牌                     |
| `-n, --predict N`    | `-1`    | 要生成的最大令牌数（`-1` = 不限）              |
| `--repeat-penalty N` | `1.0`   | 惩罚重复的令牌序列                             |

## 性能和内存

```sh
# 设置上下文窗口（0 = 模型允许的最大上下文大小）
llama cli -m model.gguf -c 16384

# 将 MoE 专家权重保留在 CPU 上；适合在小型 GPU 上运行大型 MoE 模型
llama cli -m model.gguf -cmoe
```

默认情况下，llama.cpp 会调整未设置的选项以适应设备可用内存（`--fit on`），因此启动时很少会出现内存不足错误。使用 `--list-devices` 查看可用 GPU，并使用 `-dev` 选择特定的 GPU。

## 多模态输入

许多 LLM 支持图像或多模态输入。启动 `llama cli` 后，可以使用 `/image` 命令将图像添加到提示词中（先输入媒体文件，再输入引用该图像的文本提示词）：

```
> /image image.png

已从 'image.png' 加载媒体

> 描述这张图片
```

对于一次性的媒体-文本提示词，可以将媒体文件与提示词一起传入。

```sh
llama cli -hf ggml-org/gemma-4-e4b-it-GGUF:Q4_0 --image "image.png" -p "描述这张图片。"
```

同样，你可以在 CLI 中使用 `/audio` 输入音频，或使用 `--audio` 传入一次性的音频-文本组合。通过逗号分隔的路径可以指定多个文件。

```
> /audio /Users/mervenoyan/Downloads/example_audio.mp3

已从 '/Users/mervenoyan/Downloads/example_audio.mp3' 加载媒体

> 转录这段音频
```

## 推理模型

对于支持思考/推理的模型，你可以控制思考行为：

```sh
# 完全禁用思考
llama cli -hf ggml-org/gemma-4-e4b-it-GGUF:Q4_0 -rea off

# 将思考限制为 1024 个令牌
llama cli -m model.gguf --reasoning-budget 1024
```

## 推测解码

使用推测解码辅助模型（或草稿模型）来加快生成速度。模型必须支持此功能，并且需要同时指定主模型和草稿模型：

```bash
llama cli -m big-model.gguf -md small-draft-model.gguf --spec-type draft-simple
```

对于 Hugging Face Hub 上的 GGUF 仓库，可以分别指定大型模型和小型模型的仓库。有些仓库会将它们放在一起；对于其他仓库，则可以分别指定包含主模型和辅助模型的仓库。

```bash
llama cli -hf ggml-org/gemma-4-e4b-it-GGUF:Q4_0 --hf-repo-draft ggml-org/gemma-4-e4b-it-GGUF:Q4_0 --spec-type draft-mtp
```

`--spec-type` 默认为 `none`（不进行草稿推测）。常用选项有 `draft-simple`、`draft-mtp` 或 `draft-eagle3`，具体取决于模型支持的草稿模型类型。

## 获取帮助

`llama cli -h` 会打印所有选项。这里列出的是最常用的标志；[完整参考](https://github.com/ggml-org/llama.cpp/blob/master/tools/cli/README.md)介绍了更多高级设置。
