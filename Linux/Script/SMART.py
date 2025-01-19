#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

# 获取全部硬盘设备名
fdisk = subprocess.run(
    "fdisk -l | grep '^Disk /dev' | awk '{print $2}'",
    shell=True, 
    capture_output=True, 
    text=True)

dev_list = [dev.rstrip(':') for dev in fdisk.stdout.splitlines()]

keywords = {
    "nvme":[
        "overall-health",
        "Data Units Written",
        "Percentage Used",
    ],
    "sata":[
        "overall-health",
        "Reallocated_Sector_Ct",
        "Total_LBAs_Written",
        "Media_Wearout_Indicator",
    ],
    "hdd":[
        "overall-health",
        "Reallocated_Sector_Ct",   # 05
        "Current_Pending_Sector",  # C5
        "Offline_Uncorrectable",   # C6
    ]
}

Translate = {
    "DEVICE": "设备",
    "overall-health self-assessment test result": "整体健康自评测试结果",
    "Data Units Written": "写入的数据单位",
    "Percentage Used": "使用百分比",
    "Reallocated_Sector_Ct": "重新分配扇区计数",
    "Total_LBAs_Written": "写入的总逻辑块地址数",
    "Media_Wearout_Indicator": "介质磨损",
    "Current_Pending_Sector": "待处理的坏道",
    "Offline_Uncorrectable": "无法修复的坏道",
}

result = []

def split(x):
    z = [line for line in rs if any(keyword in line for keyword in keywords[x])]
    result.append(z[0])
    result.append("")
    result.append("ID# | 属性名称 | 标志 | 当前值 | 最差值 | 临界值 | 类型 | 更新状态 | 失败时间| 原始数据")
    result.extend(z[1:])
    result.append("-" * 100)

for i in dev_list:
    r = subprocess.run(['smartctl', '-a', i], capture_output=True, text=True)
    rs = r.stdout.splitlines()
    result.append("DEVICE: " + i)
    if "NVMe" in r.stdout:
        split("nvme")   # NVMe 固态
    elif "Solid" in r.stdout:
        split("sata")   # SATA 固态
    else:
        split("hdd")    # 机械

def replace_keywords_in_list(lst, translation_dict):
    return [replace_keywords(item, translation_dict) for item in lst]

def replace_keywords(x, translation_dict):
    for key, value in translation_dict.items():
        x = x.replace(key, value)  # 使用字典中的映射进行替换
    return x

result_text = ""
for i in replace_keywords_in_list(result, Translate):
    if "写入的总逻辑块地址数" in i:
        l = i.split()
        n = (int(l[-1])*512)/(1024**4)
        i = i.replace(l[-1], l[-1] + f" [{round(n, 2)} TB]")
    result_text = result_text + i + "\n"

print(result_text)
