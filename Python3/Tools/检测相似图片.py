import os
from PIL import Image
import imagehash  # pip install imagehash

# 基于图像内容（适用于内容相同但格式/压缩不同的图片）
# 如果图片被修改过（如格式转换、压缩、调整大小等），需通过图像内容识别重复：
# 感知哈希（Perceptual Hash, pHash）
# pHash 算法生成图片的“指纹”，即使图片被压缩或调整大小，哈希值仍相似。

def find_similar_images(directory, hash_size=8, threshold=5):
    # 获取目录下的所有图片文件
    images = [
        f
        for f in os.listdir(directory)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif"))
    ]
    image_hashes = {}

    for image_file in images:
        image_path = os.path.join(directory, image_file)
        try:
            # 打开图片并计算哈希值
            img = Image.open(image_path)
            img_hash = imagehash.phash(img, hash_size=hash_size)

            # 存储图片哈希值
            if img_hash not in image_hashes:
                image_hashes[img_hash] = []
            image_hashes[img_hash].append(image_path)
        except Exception as e:
            print(f"无法处理图片 {image_file}: {e}")

    # 查找相似图片
    similar_images = []
    for hash_value, paths in image_hashes.items():
        if len(paths) > 1:
            # 如果有多个图片拥有相同的哈希值，说明它们是相似的
            similar_images.append(paths)

    return similar_images


def main():
    directory = input("请输入要扫描的文件夹路径: ")
    threshold = int(input("请输入哈希值相似度阈值 (默认5): ") or 5)
    hash_size = int(input("请输入哈希值大小 (默认8): ") or 8)

    similar_images = find_similar_images(directory, hash_size, threshold)

    if similar_images:
        print("\n发现以下相似图片：")
        for group in similar_images:
            print("\n".join(group))
    else:
        print("未发现相似图片。")


if __name__ == "__main__":
    main()
