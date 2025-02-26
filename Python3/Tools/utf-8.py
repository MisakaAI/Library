import os
import chardet  # pip install chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def convert_to_utf8(file_path, original_encoding):
    if original_encoding.lower() != 'utf-8':
        # 读取文件内容并解码
        with open(file_path, 'r', encoding=original_encoding, errors='ignore') as file:
            content = file.read()

        # 重新编码并写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Converted {file_path} from {original_encoding} to UTF-8")
    else:
        print(f"{file_path} is already UTF-8 encoded.")
l = []
def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                encoding = detect_encoding(file_path)
                try:
                    convert_to_utf8(file_path, encoding)
                except:
                    l.append(file_path)

# 使用目录路径调用函数
directory_path = ''
process_directory(directory_path)
print("------------------")
for i in l:
    print(i)
