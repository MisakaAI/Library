#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
在 MYSYS2 的 MINGW64 环境下执行！！！！

自动化 Release 构建和部署脚本
使用 pathlib 处理所有文件路径操作

功能：
1. 清理构建目录
2. 使用 CMake 配置和构建 Release 版本
3. 使用 windeployqt 部署 Qt 依赖
4. 使用 ldd 检查并复制缺失的 DLL

使用方法: python auto_release.py [可执行文件路径]
"""

import sys
import re
import subprocess
import shutil
import argparse
from pathlib import Path

# 配置变量 - 根据您的项目修改这些值
BUILD_DIR = Path("build")  # 构建目录
CMAKE_SOURCE_DIR = Path(".")  # CMake 源码目录
EXECUTABLE_NAME = "QtProject.exe"  # 可执行文件名
CMAKE_GENERATOR = "MinGW Makefiles"


# 运行命令并打印输出
def run_command(cmd, cwd=None, check=True):
    print(f"执行命令: {' '.join(cmd)}")
    try:
        result = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, check=check
        )
        if result.stdout:
            print("输出:", result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败: {e}")
        if e.stderr:
            print("错误输出:", e.stderr)
        return None


# 清理构建目录
def clean_build_directory():
    if BUILD_DIR.exists():
        print(f"清理构建目录: {BUILD_DIR}")
        shutil.rmtree(BUILD_DIR)
    else:
        print(f"构建目录不存在: {BUILD_DIR}")


# 运行 CMake 配置
def cmake_configure():
    cmd = [
        "cmake",
        "-B",
        str(BUILD_DIR),
        "-S",
        str(CMAKE_SOURCE_DIR),
        "-DCMAKE_BUILD_TYPE=Release",
    ]

    # 添加生成器
    if CMAKE_GENERATOR:
        cmd.extend(["-G", CMAKE_GENERATOR])

    return run_command(cmd)


# 运行 CMake 构建
def cmake_build():
    cmd = ["cmake", "--build", str(BUILD_DIR), "--config", "Release"]
    return run_command(cmd)


# 查找可执行文件
def find_executable():
    # 首先尝试在构建目录中查找
    exe_path = BUILD_DIR / EXECUTABLE_NAME
    if exe_path.is_file():
        return exe_path

    # 如果不在构建目录根目录，可能在子目录中
    for exe_file in BUILD_DIR.rglob(EXECUTABLE_NAME):
        if exe_file.is_file():
            return exe_file

    # 如果仍未找到，尝试 Release 子目录
    release_exe_path = BUILD_DIR / "Release" / EXECUTABLE_NAME
    if release_exe_path.is_file():
        return release_exe_path

    return None


# 运行 windeployqt 部署 Qt 依赖
def windeployqt():
    exe_path = find_executable()
    if not exe_path:
        print(f"错误: 找不到可执行文件 {EXECUTABLE_NAME}")
        return False

    cmd = [
        "windeployqt6",
        "--release",
        "--no-translations",
        "--no-system-d3d-compiler",
        str(exe_path),
    ]

    result = run_command(cmd)
    if result and result.returncode == 0:
        print("windeployqt 执行成功")
        return True
    return False


# 运行 ldd 检查依赖并复制缺失的 DLL
def run_ldd_and_copy_dlls():
    exe_path = find_executable()
    if not exe_path:
        print(f"错误: 找不到可执行文件 {EXECUTABLE_NAME}")
        return False

    exe_dir = exe_path.parent

    # 运行 ldd 命令
    ldd_result = run_command(["ldd", str(exe_path)], check=False)
    if not ldd_result or ldd_result.returncode != 0:
        print("ldd 命令执行失败，跳过 DLL 复制")
        return False

    # 解析 ldd 输出
    dll_pattern = re.compile(r"\s*(.+?)\s+=>\s+(.+?)\s+\(0x[0-9a-fA-F]+\)")
    dlls_to_copy = []

    for line in ldd_result.stdout.split("\n"):
        match = dll_pattern.match(line)
        if match:
            dll_name = match.group(1)
            dll_path = Path(match.group(2))

            # 跳过系统 DLL 和已存在的 DLL
            if not is_system_dll(dll_path) and not (exe_dir / dll_name).exists():
                dlls_to_copy.append((dll_name, dll_path))

    print("===== dlls_to_copy =====")
    print(dlls_to_copy)
    print("===== end =====")

    # 复制 DLL
    copied_count = 0
    for dll_name, dll_path in dlls_to_copy:
        if dll_path.exists():
            try:
                shutil.copy2(str(dll_path), str(exe_dir / dll_name))
                print(f"已复制: {dll_name}")
                copied_count += 1
            except Exception as e:
                print(f"复制 {dll_name} 失败: {e}")
        else:
            print(f"警告: DLL 文件不存在: {dll_path}")

    print(f"复制了 {copied_count} 个 DLL 文件")
    return True


# 检查是否为系统 DLL（不需要复制）
def is_system_dll(dll_path):
    system_paths = [
        "/c/Windows/",
    ]

    dll_path_str = str(dll_path).lower()
    return any(sys_path in dll_path_str for sys_path in system_paths)


# 主函数
def main():
    parser = argparse.ArgumentParser(description="自动化 Release 构建和部署脚本")
    parser.add_argument("--exe", help="可执行文件路径（可选）")
    args = parser.parse_args()

    # 如果通过参数指定了可执行文件路径
    if args.exe:
        global EXECUTABLE_NAME
        EXECUTABLE_NAME = args.exe

    print("开始自动化 Release 构建和部署流程")

    # 1. 清理构建目录
    print("\n=== 步骤 1: 清理构建目录 ===")
    clean_build_directory()

    # 2. CMake 配置
    print("\n=== 步骤 2: CMake 配置 ===")
    if not cmake_configure():
        print("CMake 配置失败，终止流程")
        return False

    # 3. CMake 构建
    print("\n=== 步骤 3: CMake 构建 ===")
    if not cmake_build():
        print("CMake 构建失败，终止流程")
        return False

    # 4. 查找可执行文件
    exe_path = find_executable()
    if not exe_path:
        print(f"错误: 找不到可执行文件 {EXECUTABLE_NAME}")
        return False

    print(f"找到可执行文件: {exe_path}")

    # 5. 使用 windeployqt 部署 Qt 依赖
    print("\n=== 步骤 4: 使用 windeployqt 部署 Qt 依赖 ===")
    if not windeployqt():
        print("windeployqt 执行失败")
        # 不终止流程，继续尝试复制 DLL

    # 6. 使用 ldd 检查并复制缺失的 DLL
    print("\n=== 步骤 5: 使用 ldd 检查并复制缺失的 DLL ===")
    run_ldd_and_copy_dlls()

    print("\n=== 流程完成 ===")
    print(f"可执行文件位置: {exe_path}")
    print("请在干净环境中测试应用程序以确保所有依赖项都已正确包含")

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
