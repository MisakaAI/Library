#!/bin/env python3

# 将音频文件分割为用于训练的小段

import os
from pathlib import Path
from pydub import AudioSegment
from pydub.utils import make_chunks
from pydub.silence import split_on_silence

# 待切割文件存放目录
source_dir = Path('H:\AI干音包')

# 切割后文件存放目录
save_dir = Path('H:\so-vits-svc\dataset_raw\zheran')

# 文件名处理为纯数字格式 a-b.mav
a=1

for f in os.listdir(source_dir):
    # 如果是 wav 格式文件
    if '.wav' in f:
        b=1
        # 读取文件
        sound = AudioSegment.from_file(source_dir / f, "wav")
        # min_silence_len 大于500毫秒的静音段则被认为是静音段
        # silence_thresh 声音多小才被认为是静音段
        # keep_silence 剪切静音段保留多少静音段在有声音的音频段上
        chunks = split_on_silence(sound,min_silence_len=500,silence_thresh=-30,keep_silence=100)
        for i, chunk in enumerate(chunks):
            # 小于15秒 大于2秒
            n = len(chunk)
            if n <= 15000 and n >= 2000:
                chunk.export(save_dir / str(str(a)+'-'+str(b)+'.wav'),format="wav")
                # 显示进度
                print(f+': '+str(a)+'-'+str(b))
            # 大于15秒
            elif n > 15000:
                # 切割的毫秒数 10s=10000
                z = make_chunks(chunk, 10000)
                c = 1
                for x,y in enumerate(z):
                    # 如果大于3秒
                    if len(y) >= 3000:
                        y.export(save_dir / str(str(a)+'-'+str(b)+'-'+str(c)+'.wav'),format="wav")
                        # 显示进度
                        print(f+': '+str(a)+'-'+str(b)+'-'+str(c))
                    c+=1
            b+=1
    a+=1
