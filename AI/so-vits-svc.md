# so-vits-svc

基于vits与softvc的歌声音色转换模型

- [SoVITS](https://github.com/innnky/so-vits-svc#readme) This repository has been archived
- [SoVits](https://github.com/svc-develop-team/so-vits-svc) svc社区维护仓库

本说明基于 `4.0` 版本

## 部署

```bash
# clone 项目
git clone https://github.com/innnky/so-vits-svc.git -b 4.0

# 切换到 4.0 分支（-b 4.0）
# git checkout 4.0

# 依赖问题

## Python 3.10
# https://www.python.org/downloads/release/python-31010/

## Microsoft C++ 生成工具
# https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/
# .\vs_BuildTools.exe --norestart --passive --downloadThenInstall --includeRecommended --add Microsoft.VisualStudio.Workload.NativeDesktop --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Workload.MSBuildTools

## vc_redist.x64
# https://aka.ms/vs/17/release/vc_redist.x64.exe

## CUDA 11.7
# PyTorch 目前仅支持到 CUDA 11.7
# https://developer.nvidia.com/cuda-toolkit
# https://developer.nvidia.com/cuda-11-7-1-download-archive?target_os=Windows&target_arch=x86_64&target_version=10

# 验证 CUDA
# nvidia-smi
# nvcc -V

## PyTorch
# https://pytorch.org/get-started/previous-versions/
# https://download.pytorch.org/whl/torch_stable.html
# pip install torch==1.13.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117
# pip install torch==1.13.1+cu117 torchvision==0.13.1+cu11 torchaudio==0.14.1 --extra-index-url https://download.pytorch.org/whl/cu117
# 也可以下载后用pip install *.whl 的方式进行离线安装

# 验证 PyTorch 安装
# import torch
# torch.cuda.is_available()

## ffmpeg
# https://ffmpeg.org/download.html
# 添加到环境变量
# （搜索）环境变量 - 系统变量 - Path - 编辑 - 新建

# 验证 ffmpeg
# ffmpeg -version

# pydub
# pip install pydub

# 安装 Python 依赖
pip install -r requirements.txt

# 预先下载的模型文件

# 放在 hubert 目录下
# https://ibm.box.com/s/z1wgl1stco8ffooyatzdwsqn2psd9lrr

# 放在 logs/44k 目录下
# https://huggingface.co/innnky/sovits_pretrained/resolve/main/sovits4/G_0.pth
# https://huggingface.co/innnky/sovits_pretrained/resolve/main/sovits4/D_0.pth
```

## 准备训练数据

```txt
dataset_raw
├───speaker0
│   ├───xxx1-xxx1.wav
│   ├───...
│   └───Lxx-0xx8.wav
└───speaker1
    ├───xx2-0xxx2.wav
    ├───...
    └───xxx7-xxx007.wav
```

此外还需要编辑 `configs/config.json`

```json
// 有几个人
"n_speakers": 10
// 每个人的名字
"spk":{
    "speaker0": 0,
    "speaker1": 1,
}
```

## 数据预处理

- [自动分割干音](automatic-audio-split.py)
- [时长统计](count-audio-time.py)

```bash
# 重采样至 44100hz
python resample.py
# 自动划分训练集 验证集 测试集 以及自动生成配置文件
python preprocess_flist_config.py
# 生成hubert与f0
python preprocess_hubert_f0.py
```

## 修改显存

修改 `configs\config.json` 文件中 `batch_size` 的数值。

推测 `batch_size` 参数和显存有关，需要根据显存的大小调整。

查看显存：任务管理器 - 性能 - GPU - 专用GPU内存

## 训练

```bash
python train.py -c configs/config.json -m 44k
```

训练时会自动清除老的模型，只保留最新3个模型，如果想防止过拟合需要自己手动备份模型记录点。
或修改配置文件 `keep_ckpts 0` 为永不清除。

### 其他说明

global_step = 最多语音说话人的语音数 / batch_size * epoch

global_step 表示总体迭代次数
batch_size 是配置文件中的参数，可能是显存有关
epoch 表示迭代批次，每一批次可以看作一个迭代分组

### 训练次数的查看

日志保存的位置：`.\logs\32k\train.log`
持续查看日志：`tail -f logs/32k/train.log`

## 推理

使用 `inference_main.py`

```bash
python inference_main.py -m "logs/44k/G_30400.pth" -c "configs/config.json" -n "君の知らない物語-src.wav" -t 0 -s "nen"
```

必填项部分

-m, --model_path：模型路径，在 `logs/44k` 目录下。
-c, --config_path：配置文件路径，`configs/config.json`。
-n, --clean_names：wav 文件名列表，放在 `raw` 文件夹下。
-t, --trans：音高调整，支持正负（半音）。
-s, --spk_list：合成目标说话人名称。

可选项部分：见下一节

-a, --auto_predict_f0：语音转换自动预测音高，转换歌声时不要打开这个会严重跑调。
-cm, --cluster_model_path：聚类模型路径，如果没有训练聚类则随便填。
-cr, --cluster_infer_ratio：聚类方案占比，范围 0-1，若没有训练聚类模型则填 0 即可。

```python
# 也可以修改 inference_main.py 文件

# 这里改成训练出来的G模型路径
model_path = "logs/32k/G_10000.pth"
# 配置文件路径
config_path = "configs/config.json"

# 这里修改成你要处理的干声片段的文件名，支持多个文件，放在raw文件夹下
clean_names = ["vocals_01", "vocals_02","vocals_03"]
# 音高调整，支持正负（半音）
trans = [0]
# 这里是说话人的名字，之前准备训练样本的文件夹名字
spk_list = ['Sucial']
# 默认-40，嘈杂的音频可以-30，干声保留呼吸可以-50
slice_db = -40
# 音频输出格式
wav_format = 'wav'
```

### 可选项

4.0模型训练过程会训练一个f0预测器，对于语音转换可以开启**自动音高预测**，
如果效果不好也可以使用手动的，但转换歌声时请不要启用此功能！！！会严重跑调！！

在 `inference_main` 中设置 `auto_predict_f0` 为 `true` 即可。

用于被推理的 wav 文件，需要也是干音，需要这个干音分成若干段不超过40秒的片段。

推荐使用 [Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui) 对歌曲进行人声分离。

使用方法可参考：[最强伴奏与人声分离工具](http://www.staycu.com/1731.html)

### Tips

女翻唱男时，音高不变的情况下很难听出是女声，一般会提高3-7个音高 `-t 3`。
但提高音高后会出现高音嘶哑、破音、唱不出来等情况。

可以试试AU的频谱频率显示器 `Shift+D`
比如有些混音能在低频区发现多一些亮的片段，擦除就能恢复正常。

## 参考文献

- [soVITS3.0炼丹教程](https://www.bilibili.com/read/cv20500632)
- [最强伴奏与人声分离工具](http://www.staycu.com/1731.html)