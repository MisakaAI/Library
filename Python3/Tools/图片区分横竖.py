from pathlib import Path
from PIL import Image
# import pillow_heif

# 注册 HEIF 插件，用于识别 HEIF 格式的图像
# pillow_heif.register_heif_opener()

# 输入目录和目标目录
input_directory = Path(r'F:')
output_directory_a = Path(r'F:\横屏')
output_directory_b = Path(r'F:\竖屏')
output_directory_c = Path(r'F:\正方形')

# 创建目标目录
output_directory_a.mkdir(parents=True, exist_ok=True)
output_directory_b.mkdir(parents=True, exist_ok=True)
output_directory_c.mkdir(parents=True, exist_ok=True)

# 遍历输入目录中的所有文件
for file_path in input_directory.iterdir():
    if file_path.suffix.lower() in ('.jpg', '.png'):  # 检查文件扩展名
        print(file_path)
        with Image.open(file_path) as img:
            width, height = img.size
            aspect_ratio = width / height
        if 0.9 < aspect_ratio < 1.1:
            # 长宽比在0.9和1.0之间，移动到目录C
            output_path = output_directory_c / file_path.name
        elif aspect_ratio > 1.0:
            # 移动到目录A
            output_path = output_directory_a / file_path.name
        elif aspect_ratio < 1.0:
            # 移动到目录B
            output_path = output_directory_b / file_path.name

        file_path.rename(output_path)
