# 环境搭建

## 编译器

### Windows

#### Microsoft Visual C++

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
