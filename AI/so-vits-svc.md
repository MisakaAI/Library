# so-vits-svc

歌声音色转换模型

## 部署

```bash
# clone 项目
git clone https://github.com/innnky/so-vits-svc.git -b 4.0

# 切换到 4.0 分支
# git checkout 4.0

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

## 数据预处理

```bash
# 重采样至 44100hz
python resample.py
# 自动划分训练集 验证集 测试集 以及自动生成配置文件
python preprocess_flist_config.py
# 生成hubert与f0
python preprocess_hubert_f0.py
```

## 训练

```bash
python train.py -c configs/config.json -m 44k
```

训练时会自动清除老的模型，只保留最新3个模型，如果想防止过拟合需要自己手动备份模型记录点,或修改配置文件keep_ckpts 0为永不清除。

## 推理

使用 `inference_main.py`

```bash
python inference_main.py -m "logs/44k/G_30400.pth" -c "configs/config.json" -n "君の知らない物語-src.wav" -t 0 -s "nen"
```

必填项部分

-m, --model_path：模型路径。
-c, --config_path：配置文件路径。
-n, --clean_names：wav 文件名列表，放在 raw 文件夹下。
-t, --trans：音高调整，支持正负（半音）。
-s, --spk_list：合成目标说话人名称。

可选项部分：见下一节

-a, --auto_predict_f0：语音转换自动预测音高，转换歌声时不要打开这个会严重跑调。
-cm, --cluster_model_path：聚类模型路径，如果没有训练聚类则随便填。
-cr, --cluster_infer_ratio：聚类方案占比，范围 0-1，若没有训练聚类模型则填 0 即可。

### 可选项

4.0模型训练过程会训练一个f0预测器，对于语音转换可以开启**自动音高预测**，
如果效果不好也可以使用手动的，但转换歌声时请不要启用此功能！！！会严重跑调！！

在 `inference_main` 中设置 `auto_predict_f0` 为 `true` 即可