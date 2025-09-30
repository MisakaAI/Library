# C/C++ 调用 Python 完全指南

将 Python 解释器嵌入其应用程序中的 C 和 C++ 程序员可用的 API

## Linux

```bash
# C/C++
apt install -y gcc g++ make
apt install build-essential cmake gdb
apt install ninja-build

# Python
apt install python3-dev
python -m venv .venv
source .venv/bin/activate
pip install torch torchvision
pip install -r requirements.txt
python -c "import torch; print(f'PyTorch {torch.__version__}, CUDA available: {torch.cuda.is_available()}')"
```

## Windows

### 开发

1. C++ 开发环境 [MSVC](https://visualstudio.microsoft.com/zh-hans/downloads/)
2. 安装 [Python Debug](https://docs.python.org/zh-cn/3.13/using/windows.html)
    需要选择 **Customize installation**，并启用：
    - [ ] Download Debugging symbols
    - [ ] Download Debug binaries

### 无开发环境下运行

0. 安装 [Microsoft C 运行时](https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist#visual-studio-2015-2017-2019-and-2022)
1. 下载 Python [Windows embeddable package](https://www.python.org/ftp/python/3.13.7/python-3.13.7-embed-amd64.zip)
2. 修改 `python313._pth` 增加 `import site`（或取消注释）
3. 安装 [get-pip-py](https://bootstrap.pypa.io/get-pip.py)
`.\python.exe .\get-pip.py`
4. 安装 PyTorch 等依赖
`.\python.exe -m pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple torch torchvision`
5. 验证安装 `.\python.exe -c "import torch; print(f'PyTorch {torch.__version__}, CUDA available: {torch.cuda.is_available()}')"`

```tree
├── main.exe
├── python313.dll
├── python313.zip           ← 或替换为 Lib/ 文件夹
├── Lib/
│   ├── site-packages/
│   │   └── torch/          ← 你的 PyTorch
│   └── ...                 ← 标准库（如果没用 zip）
└── DLLs/
    ├── _ctypes.pyd
    ├── _socket.pyd
    ├── _ssl.pyd
    └── ...                 ← 其他可能需要的 .pyd
```

## 程序

- [c_python.cpp](./c_python.cpp)

```bash
# python3-config --includes --ldflags
# --embed 嵌入式
g++ -o a.out c_python.cpp $(python3-config --cflags --ldflags --embed) -std=c++17
```

## 参考文献

- [在Windows上使用 Python](https://docs.python.org/zh-cn/3.13/using/windows.html)
