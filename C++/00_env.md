# 环境搭建

## 编译器

### Windows

#### Microsoft Visual C++ (MSVC)

Microsoft Visual C++ (MSVC) 是 Windows Visual Studio 的一部分，指 C++、C 和汇编语言开发工具和库。

- [Visual Studio Code](https://code.visualstudio.com/Download)
- [Visual Studio Community 2022](https://visualstudio.microsoft.com/zh-hans/downloads/)
- [Visual Studio 2022 生成工具](https://aka.ms/vs/17/release/vs_BuildTools.exe)
- [Microsoft Visual C++ Redistributable for Visual Studio 2022](https://aka.ms/vs/17/release/VC_redist.x64.exe)

##### Visual Studio Code

```txt
my_project/
├── .vscode/          # VSCode 特定配置（可选，可由 CMake Tools 自动管理）
│   ├── c_cpp_properties.json   # C/C++ 语言配置
│   ├── launch.json             # 调试配置
│   ├── tasks.json              # 任务配置
│   └── settings.json           # 用户设置
├── build/            # 用于存放构建输出（CMake 默认在此目录构建）
├── src/              # 源代码目录
│   └── main.cpp      # 你的源代码
├── include/          # 头文件目录（可选）
├── CMakeLists.txt    # CMake 的构建定义文件
└── python_script.py  # Python 脚本
```

- [CMakeLists.txt](./my_project/CMakeLists.txt)
- .vscode
  - [c_cpp_properties.json](./my_project/.vscode/c_cpp_properties.json)
  - [launch.json](./my_project/.vscode/launch.json)
  - [tasks.json](./my_project/.vscode/tasks.json)
  - [settings.json](./my_project/.vscode/settings.json)
- [mian.cpp](./my_project/src/main.cpp)

```txt
在 VS Code 中进行 C++ (msvc) 的开发。
C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.44.35207\bin\Hostx86\x86\cl.exe

需要调用 Python 的代码，python 安装路径为：
C:\Users\misaka\AppData\Local\Programs\Python\Python313\python.exe

使用 cmake 生成项目，需要 CMakeLists.txt
C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin\cmake.exe

VS Code 需要配置 c_cpp_properties.json launch.json tasks.json settings.json 这四个文件。

然后写一个 main.cpp 调用 Python 执行 print("hello world")

以上文件均需添加注释。
```

##### 参考文献

- [在 Visual Studio 中安装 C 和C++支持](https://learn.microsoft.com/zh-cn/cpp/build/vscpp-step-0-installation)

#### MinGW-w64

1. 下载 [MSYS2](https://www.msys2.org/)
清华大学开源软件镜像站 [(Windows, x86_64)](https://mirrors.tuna.tsinghua.edu.cn/msys2/distrib/msys2-x86_64-latest.exe)

2. 添加 [Windows Terminal](https://www.msys2.org/docs/terminals/) 配置

```json
{
    "profiles": {
        "defaults": {},
        "list": [
            {
                "guid": "{71160544-14d8-4194-af25-d05feeac7233}",
                "name": "MSYS",
                "hidden": false,
                "colorScheme": "Dark+",
                "commandline": "C:/msys64/msys2_shell.cmd -defterm -here -no-start -mingw64",
                "startingDirectory": "C:/msys64/home/%USERNAME%",
                "icon": "C:/msys64/mingw64.ico",
            }
        ]
    },
}
```

3. 软件仓库

使用清华大学开源软件镜像站

```bash
sed -i "s#https\?://mirror.msys2.org/#https://mirrors.tuna.tsinghua.edu.cn/msys2/#g" /etc/pacman.d/mirrorlist*
```

4. 更新 & 安装

```bash
# 更新基础系统
pacman -Syu

# 安装 mingw-w64 GCC
pacman -S mingw-w64-x86_64-gcc

# Windows计算机上的UCRT仅包含在Windows 10或更高版本中。
# pacman -S mingw-w64-ucrt-x86_64-gcc

# 验证安装
g++ --version
```

5. 环境变量

更新 `PATH` 环境变量，添加 `C:\msys64\mingw64\bin`

6. 编译

```bash
# 编译
g++ -o hello.exe hello.cpp

# 运行
./hello.exe
```

##### VS Code

1. 安装 Visual Studio Code
2. 安装 C/C++ 扩展
3. 安装 MinGW-w64 相关工具

```bash
# 其他版本的Windows，请运行以下不使用UCRT的命令。
pacman -S --needed base-devel mingw-w64-x86_64-toolchain

# Windows计算机上的UCRT仅包含在Windows 10或更高版本中。
# pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain
```

- `base-devel`: 包含基础开发工具，如`make`、`gcc`编译器等
- `mingw-w64-x86_64-toolchain`: 提供 Windows 下的完整工具链

##### Zsh

```bash
pacman -S git
pacman -S zsh
touch ~/.zshrc
# 修改 Windows Terminal 配置
# "commandline": "C:/msys64/msys2_shell.cmd -defterm -here -no-start -mingw64 -shell zsh",

# Oh My Zsh
git clone https://mirrors.tuna.tsinghua.edu.cn/git/ohmyzsh.git
cd ohmyzsh/tools
REMOTE=https://mirrors.tuna.tsinghua.edu.cn/git/ohmyzsh.git sh install.sh
```

### Linux

1. 安装 `g++`

```bash
# 仅安装g++
# sudo apt install g++

## 编译 C/C++ 程序所必需的软件包、GNU 调试器
sudo apt-get install build-essential gdb
```

2. 编译

```bash
# 编译
g++ -o hello hello.cpp

# 运行
./hello
```

### macOS

1. 安装 [Xcode](https://developer.apple.com/xcode/resources/)

```bash
xcode-select --install
```

2. 编译

```bash
# 编译（使用 Clang）
clang++ -o hello hello.cpp

# 运行
./hello
```
