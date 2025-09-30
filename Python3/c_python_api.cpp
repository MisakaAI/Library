#include <Python.h>
#include <iostream>

int main() {
    // 用于存储 Python API 调用的状态和错误信息
    PyStatus status;

    // 创建并初始化 Python 配置结构体
    PyConfig config;

    // 初始化 Python 配置为默认的配置
    PyConfig_InitPythonConfig(&config);

    // 配置 Python 模块搜索路径
    // 添加当前目录下的 Lib/site-packages 路径
    status = PyWideStringList_Append(&config.module_search_paths, L"./Lib/site-packages");

    // 检查上一步操作是否出现异常
    if (PyStatus_Exception(status)) {
        PyConfig_Clear(&config);
        Py_ExitStatusException(status);
    }

    // 根据配置初始化 Python 解释器
    status = Py_InitializeFromConfig(&config);
    if (PyStatus_Exception(status)) {
        PyConfig_Clear(&config);
        Py_ExitStatusException(status);
    }

    // 清理配置结构体，释放相关资源
    PyConfig_Clear(&config);

    // 检查初始化是否成功
    if (!Py_IsInitialized()) {
        std::cerr << "Failed to initialize Python interpreter" << std::endl;
        return 1;
    }

    // 执行 Python 代码
    PyRun_SimpleString("print('Hello World!')");

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
