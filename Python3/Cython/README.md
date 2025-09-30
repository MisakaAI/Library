# Cython

Cython 是一种编程语言，它使得为 Python 编写 C 扩展变得既简单又高效。
它可以被看作是：

1. Python 的超集
2. 带有 C 数据类型的 Python

`cython` 是一个编译器，它会将你的 Cython 代码转换成使用 Python/C API 的、高度复杂的 C 代码。

## 安装

```bash
pip install Cython
```

## 工作流程

1. 编写 `.pyx` 文件 [my_module.pyx](./my_module.pyx.py)
2. `setup.py` 文件 [setup.py](./setup.py)
3. 编译成 C 代码 & 共享库
`python setup.py build_ext --inplace`
4. 在 Python 中导入 [main.py](./main.py)
`python main.py`
5. 在 C++ 中调用 [main.cpp](./main.cpp)
`g++ main.cpp $(python3-config --cflags --ldflags --embed) -I$(python -c "import numpy; print(numpy.get_include())") -std=c++17 -o a.out && ./a.out`
