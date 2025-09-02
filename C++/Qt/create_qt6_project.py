#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import platform

# ==================== 配置区域 ====================

# 项目配置
PROJECT_NAME = "QtProject"

# 指定基础目录
# PROJECT_DIR = Path(r"C:\Users\misaka")
# PROJECT_DIR = Path("/home/misaka")
PROJECT_DIR = Path.home()

# 修改为在指定目录下创建项目目录
PROJECT_DIR = PROJECT_DIR / PROJECT_NAME

# 环境配置 - Linux 版本
if platform.system() == "Linux":
    # Linux 系统路径配置
    GCC_PATH = Path("/usr/bin/gcc")
    GXX_PATH = Path("/usr/bin/g++")
    MAKE_PATH = Path("/usr/bin/make")
    GDB_PATH = Path("/usr/bin/gdb")

    # Qt 配置
    QT_INCLUDE_PATH = Path("/usr/include/x86_64-linux-gnu/qt6")
    QT_BIN_PATH = Path("/usr/lib/qt6/bin")
else:
    # Windows 系统路径配置
    MSYS2_PATH = Path("C:/msys64")
    MINGW64_BIN = MSYS2_PATH / "mingw64" / "bin"
    USR_BIN = MSYS2_PATH / "usr" / "bin"

    GCC_PATH = MINGW64_BIN / "gcc.exe"
    GXX_PATH = MINGW64_BIN / "g++.exe"
    MAKE_PATH = MINGW64_BIN / "mingw32-make.exe"
    GDB_PATH = MINGW64_BIN / "gdb.exe"

    QT_INCLUDE_PATH = MINGW64_BIN.parent / "include" / "qt6"

# ==================== 配置区域结束 ====================


# 创建项目目录结构
def create_directory_structure():
    dirs = [
        ".vscode",
    ]

    for dir_name in dirs:
        dir_path = PROJECT_DIR / dir_name
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"创建目录: {dir_path}")


# 创建 CMakeLists.txt
def create_cmakelists_txt():
    content = f"""cmake_minimum_required(VERSION 3.16)
project({PROJECT_NAME})

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(WIN32)
    set(CMAKE_EXE_LINKER_FLAGS "${{CMAKE_EXE_LINKER_FLAGS}} -mwindows")
endif()

find_package(Qt6 REQUIRED COMPONENTS Core Widgets)

qt6_standard_project_setup()

if(WIN32)
    qt6_add_executable({PROJECT_NAME} WIN32
        main.cpp
        mainwindow.cpp
        mainwindow.h
        widget.ui
    )
else()
    qt6_add_executable({PROJECT_NAME}
        main.cpp
        mainwindow.cpp
        mainwindow.h
        widget.ui
    )
endif()

target_link_libraries({PROJECT_NAME} PRIVATE Qt6::Core Qt6::Widgets)
"""
    file_path = PROJECT_DIR / "CMakeLists.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"创建文件: {file_path}")


# 创建 CMakePresets.json
def create_cmake_presets_json():
    if platform.system() == "Linux":
        # Linux 版本配置
        content = f"""{{
    "version": 3,
    "configurePresets": [
        {{
            "name": "linux-gcc",
            "displayName": "Linux GCC",
            "generator": "Unix Makefiles",
            "toolchainFile": "",
            "cacheVariables": {{
                "CMAKE_C_COMPILER": "{GCC_PATH.as_posix()}",
                "CMAKE_CXX_COMPILER": "{GXX_PATH.as_posix()}",
                "CMAKE_MAKE_PROGRAM": "{MAKE_PATH.as_posix()}"
            }},
            "condition": {{
                "type": "equals",
                "lhs": "${{hostSystemName}}",
                "rhs": "Linux"
            }}
        }}
    ]
}}
"""
    else:
        # Windows 版本配置
        content = f"""{{
    "version": 3,
    "configurePresets": [
        {{
            "name": "mingw64",
            "displayName": "MinGW64",
            "generator": "MinGW Makefiles",
            "toolchainFile": "",
            "cacheVariables": {{
                "CMAKE_C_COMPILER": "{GCC_PATH.as_posix()}",
                "CMAKE_CXX_COMPILER": "{GXX_PATH.as_posix()}",
                "CMAKE_MAKE_PROGRAM": "{MAKE_PATH.as_posix()}"
            }},
            "condition": {{
                "type": "equals",
                "lhs": "${{hostSystemName}}",
                "rhs": "Windows"
            }}
        }}
    ]
}}
"""
    file_path = PROJECT_DIR / "CMakePresets.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"创建文件: {file_path}")


# 创建 .vscode/c_cpp_properties.json
def create_vscode_cpp_properties():
    if platform.system() == "Linux":
        # Linux 版本配置
        content = f"""{{
    "configurations": [
        {{
            "name": "Linux",
            "includePath": [
                "${{workspaceFolder}}/**",
                "/usr/include/**",
                "{QT_INCLUDE_PATH.as_posix()}/**"
            ],
            "defines": [],
            "compilerPath": "{GXX_PATH.as_posix()}",
            "cStandard": "c17",
            "cppStandard": "c++17",
            "intelliSenseMode": "linux-gcc-x64"
        }}
    ],
    "version": 4
}}
"""
    else:
        # Windows 版本配置
        content = f"""{{
    "configurations": [
        {{
            "name": "Win32",
            "includePath": [
                "${{workspaceFolder}}/**",
                "{MINGW64_BIN.parent.as_posix()}/include/**",
                "{QT_INCLUDE_PATH.as_posix()}/**"
            ],
            "defines": [],
            "compilerPath": "{GXX_PATH.as_posix()}",
            "cStandard": "c17",
            "cppStandard": "c++17",
            "intelliSenseMode": "gcc-x64"
        }}
    ],
    "version": 4
}}
"""
    file_path = PROJECT_DIR / ".vscode" / "c_cpp_properties.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"创建文件: {file_path}")


# 创建 .vscode/tasks.json
def create_vscode_tasks():
    if platform.system() == "Linux":
        # Linux 版本配置
        content = """{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "cmake configure",
            "type": "shell",
            "command": "cmake",
            "args": [
                "-B",
                "build",
                "-S",
                ".",
                "-G",
                "Unix Makefiles"
            ],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": "$gcc"
        },
        {
            "label": "cmake build",
            "type": "shell",
            "command": "cmake",
            "args": [
                "--build",
                "build"
            ],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": "$gcc",
            "dependsOn": "cmake configure"
        }
    ]
}
"""
    else:
        # Windows
        content = """{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "cmake configure",
            "type": "shell",
            "command": "cmake",
            "args": [
                "-B",
                "build",
                "-S",
                ".",
                "-G",
                "MinGW Makefiles"
            ],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": "$msCompile"
        },
        {
            "label": "cmake build",
            "type": "shell",
            "command": "cmake",
            "args": [
                "--build",
                "build"
            ],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": "$msCompile",
            "dependsOn": "cmake configure"
        }
    ]
}
"""
    file_path = PROJECT_DIR / ".vscode" / "tasks.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"创建文件: {file_path}")


# 创建 .vscode/launch.json
def create_vscode_launch():
    if platform.system() == "Linux":
        # Linux 版本配置
        content = f"""{{
    "version": "0.2.0",
    "configurations": [
        {{
            "name": "Debug {PROJECT_NAME} (Manual)",
            "type": "cppdbg",
            "request": "launch",
            "program": "${{workspaceFolder}}/build/{PROJECT_NAME}",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${{workspaceFolder}}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "miDebuggerPath": "{GDB_PATH.as_posix()}",
            "setupCommands": [
                {{
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }}
            ],
            "preLaunchTask": "cmake build"
        }}
    ]
}}
"""
    else:
        # Windows 版本配置
        content = f"""{{
    "version": "0.2.0",
    "configurations": [
        {{
            "name": "Debug {PROJECT_NAME} (Manual)",
            "type": "cppdbg",
            "request": "launch",
            "program": "${{workspaceFolder}}/build/{PROJECT_NAME}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${{workspaceFolder}}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "miDebuggerPath": "{GDB_PATH.as_posix()}",
            "setupCommands": [
                {{
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }}
            ],
            "preLaunchTask": "cmake build"
        }}
    ]
}}
"""
    file_path = PROJECT_DIR / ".vscode" / "launch.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"创建文件: {file_path}")


# 创建 main.cpp
def create_main_cpp():
    content = """#include <QApplication>
#include "mainwindow.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    MainWindow window;
    window.show();

    return app.exec();
}
"""
    file_path = PROJECT_DIR / "main.cpp"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"创建文件: {file_path}")


# 创建 mainwindow.h
def create_mainwindow_h():
    content = """#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
"""
    file_path = PROJECT_DIR / "mainwindow.h"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"创建文件: {file_path}")


# 创建 mainwindow.cpp
def create_mainwindow_cpp():
    content = """#include "mainwindow.h"
#include "ui_widget.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}
"""
    file_path = PROJECT_DIR / "mainwindow.cpp"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"创建文件: {file_path}")


# 创建 widget.ui 示例文件
def create_widget_ui():
    content = (
        """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLabel" name="label">
      <property name="text">
       <string>欢迎使用 """
        + PROJECT_NAME
        + """</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
    )
    file_path = PROJECT_DIR / "widget.ui"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"创建文件: {file_path}")


# 创建 README.md
def create_readme():
    if platform.system() == "Linux":
        # Linux 版本说明
        content = f"""# {PROJECT_NAME}

这是一个使用 Qt6 和 VS Code 开发的跨平台应用程序。

## 开发环境配置 (Linux)

1. 安装必要的包：

```bash
sudo apt update
sudo apt install qt6-base-dev qt6-tools-dev qt6-tools-dev-tools
sudo apt install build-essential cmake gdb
```

## VS Code 配置

1. 安装必要的扩展：
   - C/C++ (Microsoft)
   - CMake
   - CMake Tools (Microsoft)
   - Qt Tools

## 构建和运行

1. 在 VS Code 中打开项目
2. 按 `Ctrl+Shift+P`，输入 "CMake: Configure"
3. 按 `Ctrl+Shift+P`，输入 "CMake: Build"
4. 按 F5 开始调试

## 项目结构

- [CMakePresets.json](CMakePresets.json): CMake 预设文件
- [CMakeLists.txt](CMakeLists.txt): 项目构建脚本
- [main.cpp](main.cpp): 程序入口点
- [mainwindow.h](mainwindow.h): 主窗口类
- [widget.ui](widget.ui): 界面设计文件
- `.vscode/`: VS Code 配置文件
  - [cpp_properties.json](.vscode/c_cpp_properties.json): 配置 C/C++ IntelliSense 和代码补全
  - [tasks.json](.vscode/tasks.json): 配置构建任务
  - [launch.json](.vscode/launch.json): 运行配置
"""
    else:
        # Windows 版本说明
        content = f"""# {PROJECT_NAME}

这是一个使用 Qt6 和 VS Code 开发的跨平台应用程序。

## 开发环境配置

1. 确保已安装 MSYS2 并配置好 MinGW64 环境
2. 安装必要的包：

```bash
pacman -S mingw-w64-x86_64-qt6-base mingw-w64-x86_64-qt6-tools
pacman -S mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake mingw-w64-x86_64-make mingw-w64-x86_64-gdb
```

## VS Code 配置

1. 安装必要的扩展：
   - C/C++ (Microsoft)
   - CMake
   - CMake Tools (Microsoft)
   - Qt Tools

## 构建和运行

1. 在 VS Code 中打开项目
2. 按 `Ctrl+Shift+P`，输入 "CMake: Configure"
3. 按 `Ctrl+Shift+P`，输入 "CMake: Build"
4. 按 F5 开始调试

## 项目结构

- [CMakePresets.json](CMakePresets.json): CMake 预设文件
- [CMakeLists.txt](CMakeLists.txt): 项目构建脚本
- [main.cpp](main.cpp): 程序入口点
- [mainwindow.h](mainwindow.h): 主窗口类
- [widget.ui](widget.ui): 界面设计文件
- `.vscode/`: VS Code 配置文件
  - [cpp_properties.json](.vscode/c_cpp_properties.json): 配置 C/C++ IntelliSense 和代码补全
  - [tasks.json](.vscode/tasks.json): 配置构建任务
  - [launch.json](.vscode/launch.json): 运行配置
"""
    file_path = PROJECT_DIR / "README.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"创建文件: {file_path}")


# 主函数
def main():
    print("开始创建 Qt6 VS Code 项目...")
    print(f"检测到系统: {platform.system()}")

    # 创建目录结构
    create_directory_structure()

    # 创建配置文件
    create_cmakelists_txt()
    create_cmake_presets_json()
    create_vscode_cpp_properties()
    create_vscode_tasks()
    create_vscode_launch()

    # 创建源代码文件
    create_main_cpp()
    create_mainwindow_h()
    create_mainwindow_cpp()
    create_widget_ui()

    # 创建说明文件
    create_readme()

    print("\n项目创建完成！")
    print(f"项目名称: {PROJECT_NAME}")
    print(f"项目路径: {PROJECT_DIR.resolve()}")


if __name__ == "__main__":
    main()
