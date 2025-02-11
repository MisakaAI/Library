import os

# 获取当前目录下的所有文件名
file_list = os.listdir()

# 遍历每个文件
for file_name in file_list:
    # 判断是否为文件，排除目录
    if os.path.isfile(file_name):
        # 获取文件名和文件后缀名
        file_name_without_ext, file_ext = os.path.splitext(file_name)

        # 将文件名和后缀名分别转换为大写和小写
        new_file_name = file_name_without_ext.upper() + file_ext.lower()

        # 构造新的文件路径
        new_file_path = os.path.join(os.path.dirname(file_name), new_file_name)

        # 重命名文件
        os.rename(file_name, new_file_path)

        print(f'Renamed: {file_name} -> {new_file_name}')
