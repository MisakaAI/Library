#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>
#include <iostream>

int main() {
    // 用于存储 Python API 调用的状态和错误信息
    PyStatus status;

    // 创建并初始化 Python 配置结构体
    PyConfig config;

    // 初始化 Python 配置为默认的配置
    PyConfig_InitPythonConfig(&config);

    // 设置优化等级
    config.optimization_level = 2;

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

    // 确保当前目录和 site-packages 在 sys.path 中
    PyObject* sys_path = PySys_GetObject("path");
    PyList_Append(sys_path, PyUnicode_FromString("."));
    PyList_Append(sys_path, PyUnicode_FromString("./Lib/site-packages"));

    // 初始化 NumPy C API
    if (_import_array() < 0) {
        PyErr_Print();
        return 1;
    }

    // 执行 Python 代码
    PyRun_SimpleString("");

    const char* pythonCode = R"(
import sys
print(f'Python {sys.version}')          # Python 版本信息
print(f'Python {sys.path}')          # Python 版本信息
print(f'Executable {sys.executable}')   # Python 可执行文件路径

import numpy as np
print(f'NumPy {np.__version__}')        # NumPy 版本信息
)";

    // 执行 Python 代码
    PyRun_SimpleString(pythonCode);

    // 加载当前目录下的 my_module 模块
    PyObject* my_module = PyImport_ImportModule("my_module");
    if (!my_module) {
        PyErr_Print();
        std::cerr << "Failed to import my_module" << std::endl;
        return 1;
    }

    // 从 my_module 模块中获取名为 "power" 的函数
    PyObject* power_func = PyObject_GetAttrString(my_module, "power");
    if (!power_func || !PyCallable_Check(power_func)) {
        PyErr_Print();
        std::cerr << "Failed to get power function" << std::endl;
        Py_XDECREF(power_func);
        Py_DECREF(my_module);
        return 1;
    }

    // 创建 NumPy 数组
    // a_array = np.array([5], dtype=np.int32)
    // b_array = np.array([3], dtype=np.int32)
    npy_intp dims[1] = {1};
    PyObject* a_array = PyArray_SimpleNew(1, dims, NPY_INT32);
    PyObject* b_array = PyArray_SimpleNew(1, dims, NPY_INT32);
    *(int*)PyArray_GETPTR1((PyArrayObject*)a_array, 0) = 5;
    *(int*)PyArray_GETPTR1((PyArrayObject*)b_array, 0) = 3;

    // 构造参数元组
    PyObject* args = PyTuple_Pack(2, a_array, b_array);

    // 接受返回值
    PyObject* result = PyObject_CallObject(power_func, args);
    if (!result) {
        PyErr_Print();
        std::cerr << "Failed to call power" << std::endl;
    } else {
        // 取返回值
        int res = *(int*)PyArray_GETPTR1((PyArrayObject*)result, 0);
        std::cout << "my_module.power([5],[3]) = " << res << std::endl;
        Py_DECREF(result);
    }

    // 释放引用
    Py_DECREF(args);
    Py_DECREF(a_array);
    Py_DECREF(b_array);
    Py_DECREF(power_func);
    Py_DECREF(my_module);

    // 清理 Python 解释器
    Py_Finalize();

    std::cout << "C++ Program Execution Completed" << std::endl;
    return 0;
}
