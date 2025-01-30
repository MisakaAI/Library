import os
from pathlib import Path

# 查找指定目录中最大的图片文件的路径

# 检索目录
directory = r'F:\\'

# 排除目录
exclude_directories = [Path(r'F:\Picture\壁纸\赛博朋克2077')]

# 将文件大小格式化为可读性较高的形式
def get_formatted_size(file_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if file_size < 1024.0:
            break
        file_size /= 1024.0
    return f"{file_size:.2f} {unit}"

# 找最大图片并排除目录
def find_largest_images_exclude_dirs(path, n=10, exclude_dirs=[]):
    path = Path(path)
    image_list = []

    # 递归地获取指定目录下的所有文件和子目录。
    # '**/*'模式表示匹配所有的文件和子目录。
    for file in path.glob('**/*'):
        # is_file() 是否是一个文件（而不是目录）
        # suffix.lower() 小写的文件后缀
        # in () 是否在图片文件格式列表中
        if file.is_file() and file.suffix.lower() in ('.jpg', '.jpeg', '.png', '.gif', '.bmp'):
            # 检查 file 的父目录是否包含在排除目录列表（exclude_dirs）中
            if not any(excluded_dir in file.parents for excluded_dir in exclude_dirs):
                # 作为一个元组添加到 image_list 列表中，以便后续处理和显示。
                image_list.append((file, file.stat().st_size))

    # 按文件大小排序
    image_list.sort(key=lambda x: x[1], reverse=True)

    # 取前n个最大的文件
    largest_images = image_list[:n]

    # 返回结果
    return largest_images

# 结果存储在 largest_images_paths 变量中
largest_images_paths = find_largest_images_exclude_dirs(directory, n=10, exclude_dirs=exclude_directories)

if largest_images_paths:
    print("文件大小前10的图片文件路径：")
    for i, (path, size) in enumerate(largest_images_paths, 1):
        formatted_size = get_formatted_size(size)
        print(f"{i}. {path} | {formatted_size}")
else:
    print("未找到任何图片文件")
