from pathlib import Path
from PIL import Image

"""
1. 获取目录下所有PNG图片的尺寸
2. 将图片扩展为正方形(水平居中，垂直底部对齐)
"""


def get_image_sizes(directory):
    """获取目录下所有PNG图片的尺寸"""
    sizes = []
    png_files = directory.glob("*.png")

    for file_path in png_files:
        try:
            with Image.open(file_path) as img:
                sizes.append(img.size)
                print(f"尺寸统计：{file_path.name} → {img.size}")
        except Exception as e:
            print(f"无法读取 {file_path.name}：{str(e)}")

    return sizes


def expand_to_square(file_path, target_size):
    """将图片扩展为指定大小的正方形"""
    try:
        with Image.open(file_path) as img:
            # 转换为RGBA模式以确保透明背景
            img = img.convert("RGBA")
            width, height = img.size

            # 如果已经是目标尺寸则跳过
            if width == target_size and height == target_size:
                return

            # 创建新画布（透明背景）
            new_img = Image.new("RGBA", (target_size, target_size), (0, 0, 0, 0))

            # 计算粘贴位置（水平居中、垂直底部对齐）
            x_offset = (target_size - width) // 2
            y_offset = target_size - height  # 贴到底部

            new_img.paste(img, (x_offset, y_offset))

            # 覆盖保存原文件
            new_img.save(file_path)
            print(f"已处理：{file_path.name} → {target_size}x{target_size}")

    except Exception as e:
        print(f"处理 {file_path.name} 失败：{str(e)}")


def main():
    # 获取当前目录
    current_dir = Path(".")

    # 第一阶段：收集所有图片尺寸
    print("正在统计图片尺寸...")
    sizes = get_image_sizes(current_dir)

    if not sizes:
        print("没有找到可处理的PNG图片")
        return

    # 计算最大边长
    max_dimension = max(max(w, h) for w, h in sizes)
    print(f"\n最大基准尺寸：{max_dimension}px")

    # 第二阶段：扩展所有图片
    print("\n开始扩展图片...")
    png_files = current_dir.glob("*.png")
    for file_path in png_files:
        expand_to_square(file_path, max_dimension)


if __name__ == "__main__":
    main()
