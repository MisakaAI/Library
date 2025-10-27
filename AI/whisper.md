# Whisper 离线语音识别

- [github](https://github.com/openai/whisper)
- [openai](https://openai.com/zh-Hans/index/whisper/)

## 安装

```sh
# 安装
pip install -U openai-whisper

# 最新的提交
# pip install git+https://github.com/openai/whisper.git

# 更新到最新版本
# pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
```

### 依赖

```sh
sudo apt update && sudo apt install ffmpeg
```

### 使用

```sh
# 指定模型
whisper audio.mp3 --model medium

# 指定语言
whisper japanese.wav --language Japanese

# --device
# 指定设备，如 cuda 或 cpu
# 在 macOS 上可以使用 mps (Metal Performance Shaders)
python -c "import torch; print(torch.backends.mps.is_available())"
whisper output.aac --model medium --language Chinese --device mps

# 指定缓存目录
whisper output.aac --model large --language Chinese --model_dir ~/.cache/whisper
```

模型本地缓存目录： `~/.cache/whisper`

## 参数说明

| 参数      | 说明                    |
| ------- | --------------------- |
| `audio` | 要转录的音频文件，可以是单个文件或多个文件 |


| 参数                                                                      | 说明                                                                                     | 默认值                  |                        |     |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------- | ---------------------- | --- |
| `-h, --help`                                                            | 显示帮助信息并退出                                                                              | -                    |                        |     |
| `--model MODEL`                                                         | 使用的 Whisper 模型名称                                                                       | turbo                |                        |     |
| `--model_dir MODEL_DIR`                                                 | 模型文件保存路径，默认 `~/.cache/whisper`                                                         | None                 |                        |     |
| `--device DEVICE`                                                       | PyTorch 推理设备（cpu / mps / cuda）                                                         | cpu                  |                        |     |
| `--output_dir, -o OUTPUT_DIR`                                           | 输出文件保存目录                                                                               | 当前目录 `.`             |                        |     |
| `--output_format, -f {txt,vtt,srt,tsv,json,all}`                        | 输出文件格式                                                                                 | all（全部可用格式）          |                        |     |
| `--verbose VERBOSE`                                                     | 是否打印进度和调试信息                                                                            | True                 |                        |     |
| `--task {transcribe,translate}`                                         | 执行任务类型：<br>- `transcribe`：语音识别（X->X）<br>- `translate`：翻译成英语                            | transcribe           |                        |     |
| `--language {...}`                                                      | 音频语言，指定 None 则自动检测                                                                     | None                 |                        |     |
| `--temperature TEMPERATURE`                                             | 采样温度，用于生成多候选                                                                           | 0                    |                        |     |
| `--best_of BEST_OF`                                                     | 采样候选数量（温度非零时使用）                                                                        | 5                    |                        |     |
| `--beam_size BEAM_SIZE`                                                 | Beam search 数量，仅温度为零时生效                                                                | 5                    |                        |     |
| `--patience PATIENCE`                                                   | Beam 解码耐心值，参考论文 [https://arxiv.org/abs/2204.05424](https://arxiv.org/abs/2204.05424)   | 1.0（默认 beam search）  |                        |     |
| `--length_penalty LENGTH_PENALTY`                                       | 令牌长度惩罚系数 alpha，参考 [https://arxiv.org/abs/1609.08144](https://arxiv.org/abs/1609.08144) | None                 |                        |     |
| `--suppress_tokens SUPPRESS_TOKENS`                                     | 生成时抑制的 token ID 列表，`-1` 表示抑制大部分特殊字符，保留常用标点                                             | -1                   |                        |     |
| `--initial_prompt INITIAL_PROMPT`                                       | 初始提示文本，提供给第一段音频                                                                        | None                 |                        |     |
| `--carry_initial_prompt CARRY_INITIAL_PROMPT`                           | 如果 True，将初始提示追加到每次 decode 调用中，可降低 condition_on_previous_text 的效果                       | False                |                        |     |
| `--condition_on_previous_text CONDITION_ON_PREVIOUS_TEXT`               | 如果 True，使用前一段输出作为下一段的提示，可增加一致性，但模型更容易卡住                                                | True                 |                        |     |
| `--fp16 FP16`                                                           | 是否使用 FP16 进行推理                                                                         | True                 |                        |     |
| `--temperature_increment_on_fallback TEMPERATURE_INCREMENT_ON_FALLBACK` | 当解码失败时，增加的温度值                                                                          | 0.2                  |                        |     |
| `--compression_ratio_threshold COMPRESSION_RATIO_THRESHOLD`             | 如果 gzip 压缩比高于此值，认为解码失败                                                                 | 2.4                  |                        |     |
| `--logprob_threshold LOGPROB_THRESHOLD`                                 | 平均 log 概率低于此值，认为解码失败                                                                   | -1.0                 |                        |     |
| `--no_speech_threshold NO_SPEECH_THRESHOLD`                             | `<                                                                                     | nospeech             | >` 概率高于此值且解码失败，认为段落是静音 | 0.6 |
| `--word_timestamps WORD_TIMESTAMPS`                                     | 提取每个词的时间戳，并根据时间戳优化结果（实验性）                                                              | False                |                        |     |
| `--prepend_punctuations PREPEND_PUNCTUATIONS`                           | word_timestamps 为 True 时，将这些标点合并到下一个词                                                  | `'“¿([{-`            |                        |     |
| `--append_punctuations APPEND_PUNCTUATIONS`                             | word_timestamps 为 True 时，将这些标点合并到前一个词                                                  | `'" .。,，!！?？:：”)]}、` |                        |     |
| `--highlight_words HIGHLIGHT_WORDS`                                     | 需要 `--word_timestamps True`，在 srt/vtt 中下划线标注每个词                                        | False                |                        |     |
| `--max_line_width MAX_LINE_WIDTH`                                       | word_timestamps 为 True 时，每行最大字符数                                                       | None                 |                        |     |
| `--max_line_count MAX_LINE_COUNT`                                       | word_timestamps 为 True 时，每段最大行数                                                        | None                 |                        |     |
| `--max_words_per_line MAX_WORDS_PER_LINE`                               | word_timestamps 为 True 时，每行最大单词数（与 max_line_width 互斥）                                  | None                 |                        |     |
| `--threads THREADS`                                                     | CPU 推理线程数，会覆盖 MKL_NUM_THREADS/OMP_NUM_THREADS                                          | 0                    |                        |     |
| `--clip_timestamps CLIP_TIMESTAMPS`                                     | 逗号分隔的剪辑时间戳（秒），可处理音频片段                                                                  | 0（默认整个文件）            |                        |     |
| `--hallucination_silence_threshold HALLUCINATION_SILENCE_THRESHOLD`     | 需要 `--word_timestamps True`，检测到可能的幻觉时，跳过静音段（秒）                                         | None                 |                        |     |
