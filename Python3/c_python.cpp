#include <Python.h>
#include <iostream>

int main() {
    // 初始化 Python 解释器
    Py_Initialize();

    // 检查初始化是否成功
    if (!Py_IsInitialized()) {
        std::cerr << "Failed to initialize Python interpreter" << std::endl;
        return 1;
    }

    // 执行 Python 代码
    PyRun_SimpleString("print('Hello World!')");

    // 👇 动态添加 site-packages 路径到 sys.path
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./Lib/site-packages')");
    // PyRun_SimpleString("sys.path.append('/home/misaka/Work/FusFlyMag/.venv/lib/python3.12/site-packages/')");
    // PyRun_SimpleString("sys.path.append('C:/Users/qd-hyh-tech/Desktop/python-3.13.7-embed-amd64/Lib/site-packages')");

        const char* pythonCode = R"(
import sys
print(f'Python {sys.version}')          # Python 版本信息
print(f'Executable {sys.executable}')   # Python 可执行文件路径

import numpy as np
print(f'NumPy {np.__version__}')        # NumPy 版本信息

import torch
print(f'PyTorch {torch.__version__}')                   # PyTorch 版本信息
print(f'CUDA available: {torch.cuda.is_available()}')   # CUDA 可用性
)";

    // 执行 Python 代码
    PyRun_SimpleString(pythonCode);

    // 清理 Python 解释器
    Py_Finalize();

    std::cout << "C++ Program Execution Completed" << std::endl;
    return 0;
}
