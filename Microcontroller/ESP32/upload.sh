#!/bin/bash
# MicroPython ampy 文件上传

AMPY_PORT="/dev/ttyUSB0"    # ESP32 端口
LOCAL_DIR="dist"            # 要上传的本地目录名
REMOTE_ROOT="/"             # 文件上传到板卡上的目标目录

# 检查 ampy 命令是否存在
if ! command -v ampy &> /dev/null
then
    echo "错误：找不到 ampy 命令。请确保 ampy 已安装。"
    exit 1
fi

echo "--- ampy 文件上传开始 ---"
echo "本地目录: ${LOCAL_DIR}"
echo "目标端口: ${AMPY_PORT}"
echo "板卡目标路径: ${REMOTE_ROOT}"
echo "--------------------------"

if [ ! -d "${LOCAL_DIR}" ]; then
    echo "错误：本地目录 '${LOCAL_DIR}' 不存在！"
    exit 1
fi

# 确保目标路径格式正确
if [ "${REMOTE_ROOT}" != "/" ] && [ "${REMOTE_ROOT: -1}" != "/" ]; then
    REMOTE_ROOT="${REMOTE_ROOT}/"
fi

# 遍历 LOCAL_DIR 目录下的所有文件
for local_file in "${LOCAL_DIR}"/*
do
    # 检查是否是文件
    if [ -f "${local_file}" ]; then
        # 获取文件名 (例如：dict/main.py -> main.py)
        filename=$(basename "${local_file}")

        # 完整的目标路径 (例如：/main.py)
        remote_file="${REMOTE_ROOT}${filename}"

        echo "上传文件: ${local_file} -> ${remote_file}"

        # 执行 ampy put 命令上传文件
        ampy -p "${AMPY_PORT}" put "${local_file}" "${remote_file}"

        if [ $? -ne 0 ]; then
            echo "错误：文件上传失败：${local_file}。请检查端口或连接。"
            exit 1
        fi
    fi
done

echo "--- 所有文件上传完成！ ---"