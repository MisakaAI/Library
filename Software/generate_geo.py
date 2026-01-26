#!/usr/bin/env python3
"""
从 DJI MRK 文件生成 ODM geo.txt 坐标文件
"""

import os
import glob
import re

# 工作目录
work_dir = os.path.dirname(os.path.abspath(__file__))
mrk_file = os.path.join(work_dir, "DJI_202601131429_008_新建面状航线40_Timestamp.MRK")
geo_file = os.path.join(work_dir, "geo.txt")

# 获取所有JPG文件并排序
jpg_files = sorted(glob.glob(os.path.join(work_dir, "DJI_*.JPG")))
jpg_names = [os.path.basename(f) for f in jpg_files]

print(f"找到 {len(jpg_names)} 张照片")

# 解析MRK文件
coords = []
with open(mrk_file, "r") as f:
    for line in f:
        # 格式: 编号 时间 [标记] 偏移 纬度,Lat 经度,Lon 高程,Ellh 精度 Q值
        parts = line.strip().split("\t")
        if len(parts) < 2:
            continue

        # 提取坐标
        lat_match = re.search(r"([\d.]+),Lat", line)
        lon_match = re.search(r"([\d.]+),Lon", line)
        alt_match = re.search(r"([\d.]+),Ellh", line)

        # 提取精度 (格式: 0.002845, 0.003021, 0.007645)
        acc_match = re.search(r"(\d+\.\d+),\s*(\d+\.\d+),\s*(\d+\.\d+)\s+\d+,Q", line)

        if lat_match and lon_match and alt_match:
            lat = float(lat_match.group(1))
            lon = float(lon_match.group(1))
            alt = float(alt_match.group(1))

            if acc_match:
                h_acc = max(float(acc_match.group(1)), float(acc_match.group(2)))
                v_acc = float(acc_match.group(3))
            else:
                h_acc = 0.01
                v_acc = 0.02

            coords.append((lon, lat, alt, h_acc, v_acc))

print(f"解析到 {len(coords)} 条坐标记录")

# 生成geo.txt
with open(geo_file, "w") as f:
    f.write("EPSG:4326\n")
    for i, (jpg_name, coord) in enumerate(zip(jpg_names, coords)):
        lon, lat, alt, h_acc, v_acc = coord
        f.write(f"{jpg_name} {lon:.8f} {lat:.8f} {alt:.3f} {h_acc:.4f} {h_acc:.4f} {v_acc:.4f}\n")

print(f"已生成 {geo_file}")
print("\n前5行内容:")
with open(geo_file, "r") as f:
    for i, line in enumerate(f):
        if i < 6:
            print(line.rstrip())
