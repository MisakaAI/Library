# FFmpeg

[FFmpeg](https://ffmpeg.org)

FFmpeg 是一款开源的多媒体处理工具，用于处理视频、音频和图像等多种多媒体格式。
它提供了丰富的功能，包括视频和音频的编码、解码、转码、剪辑、过滤、流媒体处理等，被广泛用于视频处理、音频处理、媒体转换、多媒体应用开发等领域。

本部分内容需要对[视频编码](VideoEncode.md)有一定的了解。

## 下载&安装

[Downlaod](https://ffmpeg.org/download.html)

### 编译安装

```sh
# libmp3lame
# libopus
# libfdk_aac
# x264
# x265
# svt-av1
# libass
```

## 常用参数

- `-c` 指定编码器，是`-codec`的缩写
- `-c copy` 直接复制，不经过重新编码
- `-c:v` 指定视频编码器，v表示video，视频编码器
- `-c:a` 指定音频编码器，a表示audio，音频编码器
- `-i` 指定输入文件
- `-an` 去除音频流
- `-vn：` 去除视频流
- `-sn：` 去除字幕
- `-dn：` 去除数据流
- `-preset` 指定输出的视频质量，会影响文件的生成速度，有以下几个可用的值 `ultrafast` `superfast` `veryfast` `faster` `fast` `medium` `slow` `slower` `veryslow`
- `-y` 不经过确认，输出时直接覆盖同名文件

## 使用

## 查看支持的编码器

```sh
ffmpeg -codecs
```

### 播放视频

```sh
ffplay input.mp4
```

### 查看信息

```sh
# 版本
ffmpeg -version

# 支持的编码格式：编码器（encode）/解码器（decode）
ffmpeg -encoders

# 查看支持的容器
ffmpeg -formats

# 支持的硬件加速器
ffmpeg -hwaccels

# 支持的通信协议
ffmpeg -protocols

# 查看视频文件的元信息
ffmpeg -i input.mp4
```

### 转换容器/格式

```sh
# 将输入文件的视频流和音频流直接复制到输出文件，而不进行重新编码。
ffmpeg -i input.mkv -c:v copy -c:a copy output.mp4
ffmpeg -i input.mkv -c copy output.mp4

# 将视频流通过h.264、音频流通过aac重新编码。
ffmpeg -i input.wmv -c:v libx264 -c:a aac output.mp4
# 将视频流通过h.265重新编码。
ffmpeg -i input.mkv -c:v libx265 output.mp4
```

### 视频转码/压制

#### CRF 恒定率系数

- `-crf` 恒定率系数
为一个 0~51 的数值，常用范围是 17~28
`libx264` 默认 23，`libx265` 默认 28。
数值越小，压缩率也越低，0为无损。
- `-preset` 预案
按压制后质量从低到高分为 `ultrafast` `superfast` `veryfast` `faster` `fast` `medium` `slow` `slower` `veryslow` 9种。
预案越慢，压缩效果越好。

```sh
ffmpeg -i video.mp4 -c:v libx264 -preset slow -crf 20 -c:a copy out.mp4
```

##### H.264 编码配置文件

在 FFmpeg 中，`-profile` 参数用于设置输出视频文件的 H.264 编码配置文件。

- `baseline` 基本配置文件，适用于低复杂度的应用场景，如移动设备视频。
- `main` 主要配置文件，适用于中等复杂度的应用场景，如一般的视频播放。
- `high` 高级配置文件，适用于高质量视频的应用场景，如专业视频编辑和广播。

##### 音频采样率

在 FFmpeg 中，可以使用 `-ar` 选项来设置音频采样率。

```sh
# 设置音频采样率为 44100 Hz
ffmpeg -i input.mp3 -ar 44100 output.mp3
# 设置音频采样率为 48000 Hz
ffmpeg -i input.mp3 -ar 48000 output.mp3
```

#### 2Pass 二压

```sh
# 对于 H.264 二压，使用 -pass 参数。请注意首行行尾的续行。
ffmpeg -y -i video.mp4 -c:v libx264 -b:v 2600k -pass 1 -an -f null NUL && `
ffmpeg -i video.mp4 -c:v libx264 -b:v 2600k -pass 2 -c:a aac -b:a 128k out.mp4

# 对于 H.265 二压，则应使用 -x265-params 参数。同样，请注意首行行尾的续行。
ffmpeg -y -i video.mp4 -c:v libx265 -b:v 2600k -x265-params pass=1 -an -f null NUL && `
ffmpeg -i video.mp4 -c:v libx265 -b:v 2600k -pass 2 -c:a aac -b:a 128k out.mp4
```

#### 定限码率

- `-b:v` b表示bitrate（比特率）
目标平均码率，也即希望得到的输出文件的平均码率（单位 bit/s），该参数也在二压中被使用。
值得说明的是，输出视频的码率总是大于指定的平均码率的。
这是由于容器本身还需要记录元数据等内容（可能占用数百 KB），因此我们总是需要对传入码率参数进行调低。
这个码率超出问题在压制短时长视频压制时比较明显，请特别注意。
- `-maxrate` 最大码率，需要与 `-bufsize` 参数同时使用。
- `-minrate` 最小码率。这个较少使用。
- `-bufsize` 设置视频编码缓冲区大小。

```sh
# 只给定平均码率，输出文件的码率总是略高于指定值。
ffmpeg -i input.mp4 -c:v libx264 -b:v 8M output.mp4
# 利用最大码率参数与缓冲区参数可以更严格地控制码率上限。
ffmpeg -i input.mp4 -c:v libx264 -b:v 8M -maxrate 8M -bufsize 8M output.mp4
```

#### 分辨率缩放

分辨率缩放总是会编码视频

```sh
# 使用默认的  bicubic 算法缩放到高720并保持原宽高比，并用默认编码格式（H.264）编码
ffmpeg -i video.mp4 -vf scale=-1:720 out.mp4

# 指定使用 Lanczos 算法缩放到原视频的宽高的各一半，并用 H.265 格式以默认质量编码
ffmpeg -i video.mp4 -vf scale=iw/2:ih/2:flags=lanczos -c:v libx265 -c:a copy out.mp4

# Bicubic算法是一种基于样条曲线的插值算法，它使用了周围16个像素的灰度值进行插值计算。
# Lanczos 算法是一种基于Sinc函数的插值算法，它通过在图像中使用Sinc函数来进行插值计算。

# 输出到1280x720的例子
## 直接指定宽1280、高720。选择以下任意一种写法即可
scale=w=1280:h=720
scale=1280:720
scale=1280x720
## 可以用-1表示按原视频宽高比自动计算
scale=1280:-1
scale=-1:720
## 也可以使用倍率的写法，用iw、ih代表输入视频的宽和高
scale=iw/2:ih/2

# 输出到方形720x720的例子。
## 可以用ow、oh代表变换后输出视频的宽和高
scale=iw/2:ow
```

### 音频转码

#### 编码器

- `libopus` 语音 / 低延迟
- `aac` 常用
  - `libfdk_aac` Fraunhofer FDK AAC，需要手动编译，这是目前ffmpeg提供的最高质量的AAC编码器，要求ffmpeg配置为 `--enable-libfdk-aac`
- `ac3` 杜比 / Dolby Digital
- `flac` 无损

#### 码率

- 128kbps：
- 192kbps：高频可能发闷（如镲片、吉他泛音衰减），大动态段落（如交响乐）可能浑浊。
- 256kbps：
- 320kbps：乐器分离度更高，人声通透，背景细节清晰。

### 视频分割/裁剪

```sh
# 按照时间进行分割
# 这里的 -ss 参数指定了起始时间，格式为 HH:MM:SS，表示从输入文件的 10 秒处开始分割。
# -to 参数用于指定输出文件的结束时间，格式为 HH:MM:SS，表示从输入文件的 20 秒处结束分割。
# 也可以使用 -t 参数指定持续时间，格式同样为 HH:MM:SS，-t 00:00:20表示分割出的片段时长为 20 秒。
ffmpeg -i input.mp4 -ss 00:00:10 -to 00:00:20 output.mp4

# 按照帧数进行分割
# 这里使用了 -vf 参数来应用视频滤镜，其中的 select 滤镜用于选择特定的帧。
# between(n,100,200) 表示选择从帧数 100 到 200 之间的帧。
ffmpeg -i input.mp4 -vf "select='between(n,100,200)'" output.mp4

# 按照文件大小进行分割
# 这里使用了 -segment_time 参数指定了分割的时长，格式为 HH:MM:SS，表示每个片段的时长为 20 秒。
# -f segment 参数表示输出为分段的格式。
# output_%03d.mp4 则是输出文件的文件名模板，%03d 表示使用三位数字作为片段序号。
ffmpeg -i input.mp4 -c copy -segment_time 00:00:20 -f segment output_%03d.mp4
```

### 分离音频、视频和字幕

```sh
# 提取音频
ffmpeg -i input.mp4 -vn -acodec copy output.mp3
ffmpeg -i input.mp4 -vn -c:a copy output.aac

# 提取视频
ffmpeg -i input.mp4 -an -c:v copy output.mp4

# 提取字幕
ffmpeg -i input.mkv -c copy output.srt
ffmpeg -i input.mp4 -c:s mov_text output.srt
ffmpeg -i input.avi -scodec mov_text output.srt
```

### 视频合并/拼接

```sh
ffmpeg -f concat -i mylist.txt -c copy output.mp4
```

`concat.txt` 文件范例

```txt
file '01.mp4'
file '02.mp4'
...
```

### 图片转视频

```sh
# 图片的文件名为"in000000.jpg"，从0开始依次递增。
ffmpeg -f image2 -i 'in%6d.jpg' -vcodec libx264 -r 25 -b 200k output.mp4
# -r 25 表示每秒播放25帧
# -b 200k 指定码率为200k
```

#### 一图流！为音频添加封面

```sh
# 将一张静态图片（cover.jpg）和一个音频文件（input.mp3）合成为一个 MP4 视频文件（output.mp4）
ffmpeg -loop 1 -i cover.jpg -i input.mp3 -c:v libx264 -c:a aac -b:a 192k -shortest output.mp4
```

1. `-loop 1` 设置循环选项，使输入的图片循环播放。1 表示循环一次，这样图片会一直保持在输出视频中，直到音频文件的时长结束。
2. `-i cover.jpg` 指定输入图片的文件路径和文件名。
3. `-i input.mp3` 指定输入音频文件的文件路径和文件名。
4. `-c:v libx264` 设置视频编码器为 `libx264`，使用 H.264 编码格式进行视频压缩。
5. `-c:a aac` 设置音频编码器为 `aac` ，使用 AAC 编码格式进行音频压缩。
6. `-b:a 192k` 设置音频比特率为 192k，即音频的压缩质量。
7. `-shortest` 设置输出视频的时长为输入文件中时长最短的文件，即以音频文件的时长为准。这样可以保证合成后的视频时长与音频文件一致。
8. `output.mp4` 指定输出视频文件的文件路径和文件名。

### 添加音轨

添加音轨（muxing）指的是，将外部音频加入视频，比如添加背景音乐或旁白。

```sh
ffmpeg -i input.aac -i input.mp4 output.mp4
```

### 添加字幕

```sh
# 内挂字幕
ffmpeg -i input.mp4 -i input.srt -c:v copy -c:a copy -c:s ass output.mkv
# 内嵌字幕
ffmpeg -i input.mp4 -vf subtitles=input.srt output.mp4
```

### 截图

- `-vframes 1` 指定只截取一帧
- `-q:v 2` 表示输出的图片质量，一般是1到5之间（1 为质量最高）。

```sh
# 连续对1秒钟的视频进行截图
ffmpeg -y -i input.mp4 -ss 00:01:24 -t 00:00:01 output_%3d.jpg
# 只截取一帧
ffmpeg  -ss 01:23:45 -i input.mp4 -vframes 1 -q:v 2 output.jpg
```

## 显卡硬件加速*

当前的显卡支持哪些编码格式的硬件加速，可以参考 Nvidia 给出表格：[Video Encode and Decode GPU Support Matrix](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new)

显卡加速使用特殊的编码器（而不是 CPU 编码时的标准编码器），它们通常以 nvenc （或者 cuvid ）结尾。
户可以使用 -codec 来查找当前安装的 FFmpeg 是否在编译时添加了这些编码器的支持。

```sh
# 查看显卡支持的显卡加速器
ffmpeg -hide_banner -codecs | grep nvenc

# Windows PowerShell
# ffmpeg -codecs | select-string nvenc
```

- `-hide_banner` 选项会隐藏 FFmpeg 输出中的配置信息，只显示命令执行的结果和其他有用的信息。

### 硬件加速命令

硬件加速有混合模式（CPU 与 GPU 共同工作）与独占模式（完全 GPU 工作）两种。

```sh
# CPU+GPU 混合模式
ffmpeg -i video.mp4 -c:v h264_nvenc -c:a copy out.mp4

# GPU 独占模式
ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i video.mp4 -c:v h264_nvenc -c:a copy out.mp4
```

上述命令会自动以 2000 kbps（即 2Mbps）左右的总文件比特率来压制视频。
（视频、音频多轨综合，因此单独看视频码率可能会略高于 2M ）

- 编码器 `h264_nvenc` 使用与常规编码器 `libx264` 不同的 `-preset` 参数选项，可以通过如 `ffmpeg -h encoder=h264_nvenc` 的命令查看。
- 编码器 `h264_nvenc` 不支持 CRF 参数控制压制质量，用户需要使用其他的参数，比如粗糙的 `-qp` 参数，或者 `-rc` 参数来指定码率控制模式并配合其他参数（例如 `-b:v` 参数）。
- 关于该编码器的详细帮助，可以参考 `ffmpeg -h encoder=h264_nvenc` 命令给出的参数列表。

`h264_nvenc` 编码器不支持 CRF 参数，可以通过 `-rc` 参数来设置 `vbr_hq` 可变码率模式，并手动指定 `-b:v` 视频码率的数值。
例如下述命令使用可变码率模式，并将视频设置在 2Mbps 附近：

```sh
ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i video.mp4 -c:v h264_nvenc -rc vbr_hq -b:v 2M -c:a copy out.mp4
```

在此基础上，用户还可以配合 `-maxrate` 来限制最大码率、用 `-bufsize` 来调整缓冲区大小（缓冲区越小，码率波动越小）、用 `rc_lookahead` 来设定前览帧数等。

#### HEVC (x265) 硬件加速

```sh
ffmpeg -hwaccel cuda -i input.mp4 \
    -c:v hevc_nvenc \
    -preset p7 \
    -tune hq \
    -rc vbr_hq \
    -cq 23 \
    -b_ref_mode 1 \
    -pix_fmt yuv420p \
    -c:a aac -b:a 192k \
    output_hevc.mkv
```

#### AV1 硬件加速

```sh
ffmpeg -hwaccel cuda -i input.mp4 \
-c:v av1_nvenc \
-preset p7 \
-rc vbr_hq \
-cq 30 \
-pix_fmt yuv420p \
-c:a aac -b:a 192k \
output_av1.mkv
```

## 参考文献

- [ChatGPT](https://chat.openai.com/?model=text-davinci-002-render-sha)
- [FFmpeg 教程](https://wklchris.github.io/blog/FFmpeg/Intro.html#codec-format)
- [阮一峰的网络日志](https://www.ruanyifeng.com/blog/2020/01/ffmpeg.html)