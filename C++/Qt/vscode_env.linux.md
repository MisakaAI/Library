# Qt 6 开发环境（Linux）

- [自动创建Qt项目](create_qt6_project.linux.py)

## 安装 Qt6 开发包

```sh
# 官方安装器
./qt-online-installer-linux-x64-online.run --mirror https://mirrors.tuna.tsinghua.edu.cn/qt
```

```sh
# 更新包列表
sudo apt update

# 安装 Qt6 开发包
sudo apt install qt6-base-dev qt6-tools-dev qt6-tools-dev-tools

# 安装编译工具链和其他必要工具
sudo apt install build-essential cmake gdb qtcreator
```

## 必要的 VS Code 扩展

- `C/C++ (Microsoft)` 提供 C++ 智能感知和调试支持
- `CMake` CMake 语法高亮
- `CMake Tools (Microsoft)` CMake 项目管理
- `Qt C++ Extension Pack` 推荐用于Qt C++开发的扩展程序
- `Qt Tools` Qt 相关工具支持

## 环境变量

- 系统环境变量 `/usr/bin:/usr/local/bin`
- vscode `~/.config/Code/User/settings.json`

```json
{
    "terminal.integrated.env.linux": {
        "PATH": "/usr/bin:/usr/local/bin:${env:PATH}"
    }
}
```

## 配置 CMake 构建预设

`CMakePresets.json`

```json
{
    "version": 3,
    "configurePresets": [
        {
            "name": "linux-gcc",
            "displayName": "Linux GCC",
            "generator": "Unix Makefiles",
            "toolchainFile": "",
            "cacheVariables": {
                "CMAKE_C_COMPILER": "/usr/bin/gcc",
                "CMAKE_CXX_COMPILER": "/usr/bin/g++",
                "CMAKE_MAKE_PROGRAM": "/usr/bin/make"
            },
            "condition": {
                "type": "equals",
                "lhs": "${hostSystemName}",
                "rhs": "Linux"
            }
        }
    ]
}
```

## 配置 C/C++ IntelliSense 和代码补全

`.vscode/c_cpp_properties.json`

```json
{
    "configurations": [
        {
            "name": "Linux",
            "includePath": [
                "${workspaceFolder}/**",
                "/usr/include/**",
                "/usr/include/x86_64-linux-gnu/qt6/**"
            ],
            "defines": [],
            "compilerPath": "/usr/bin/g++",
            "cStandard": "c17",
            "cppStandard": "c++17",
            "intelliSenseMode": "linux-gcc-x64"
        }
    ],
    "version": 4
}
```

## 配置构建任务

`.vscode/tasks.json`

```json
{
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
```

## 配置调试器

`.vscode/launch.json`

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug Qt Application",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/build/your_program",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "miDebuggerPath": "/usr/bin/gdb",
            "setupCommands": [
                {
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "preLaunchTask": "cmake build"
        }
    ]
}
```

## 项目构建脚本

`CMakeLists.txt`

```txt
cmake_minimum_required(VERSION 3.16)

project(MyQtApp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Core Widgets)

qt6_standard_project_setup()

qt6_add_executable(myapp
    main.cpp
    mainwindow.cpp
    mainwindow.h
)

qt6_add_resources(myapp "resources"
    PREFIX "/"
    FILES
        resources.qrc
)

target_link_libraries(myapp Qt6::Core Qt6::Widgets)
```

## 部署

```sh
# 配置 Release 构建
cmake -B build -S . -DCMAKE_BUILD_TYPE=Release
# 执行构建
cmake --build build --config Release
# 部署依赖库
windeployqt6 --release --no-translations --no-system-d3d-compiler build/QtProject.exe
```
