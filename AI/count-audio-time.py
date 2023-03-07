#!/bin/env python3

import os
from pathlib import Path
from pydub import AudioSegment

filedir = Path('H:\so-vits-svc\dataset_raw\zheran')

time_count = 0
wav_num = 0
wav_time_max = 0
wav_time_min = 5

for file in os.listdir(filedir):
    if '.wav' in file:
        wav_num += 1
        sound = AudioSegment.from_file(filedir / file, "wav")
        time = len(sound)
        time_count += time
print("共{}个文件，总时长{}分钟".format(wav_num,time_count/1000/60))
