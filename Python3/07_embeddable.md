# 嵌入式 Python

- [可嵌入的包](https://docs.python.org/zh-cn/3/using/windows.html#the-embeddable-package)
- [下载](https://www.python.org/downloads/)

嵌入式发行版不包括 [Microsoft C Runtime](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022) ，应用程序安装程序负责提供此功能。

## 在嵌入式 Python 中使用 pip 的包

0. [VC_redist](https://aka.ms/vs/17/release/VC_redist.x64.exe)
1. 下载 [python-3.13.7-embed-amd64.zip](https://www.python.org/ftp/python/3.13.7/python-3.13.7-embed-amd64.zip)
2. 修改 `python313._pth` 增加 `import site`（或取消注释）
3. 下载 [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
`.\python.exe .\get-pip.py`
4. 安装 [PyTorch](https://pytorch.org/get-started/locally/)
`.\python.exe -m pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple torch torchvision`
5. 验证安装 `.\python.exe -c "import torch; print(f'PyTorch {torch.__version__}, CUDA available: {torch.cuda.is_available()}')"`
