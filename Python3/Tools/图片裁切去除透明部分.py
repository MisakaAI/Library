from pathlib import Path
from PIL import Image

"""
1. 四周各裁切50px
2. 去掉透明区域
"""


def crop_transparent_areas(image):
    """裁切掉图片周围的完全透明区域"""
    if "A" in image.getbands():
        alpha = image.getchannel("A")
        bbox = alpha.getbbox()
    else:
        bbox = (0, 0, image.width, image.height)

    return image.crop(bbox) if bbox else image


def process_image(file_path):
    try:
        with Image.open(file_path) as img:
            # 第一次裁切：四周各裁切50px
            first_crop = (
                50,  # left
                50,  # top
                img.width - 50,  # right
                img.height - 50,  # bottom
            )

            if first_crop[0] >= first_crop[2] or first_crop[1] >= first_crop[3]:
                print(f"跳过 {file_path.name}：首次裁切后尺寸无效")
                return

            img_cropped = img.crop(first_crop)

            # 第二次裁切：去掉透明区域
            img_final = crop_transparent_areas(img_cropped)

            # 保存结果（覆盖原文件）
            img_final.save(file_path)
            print(f"已处理：{file_path.name}")

    except Exception as e:
        print(f"处理 {file_path.name} 时出错：{str(e)}")


def main():
    png_files = Path(".").glob("*.png")
    for file_path in png_files:
        process_image(file_path)


if __name__ == "__main__":
    main()
