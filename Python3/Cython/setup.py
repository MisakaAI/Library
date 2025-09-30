from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

numpy_include = np.get_include()
include_dirs = [numpy_include]

extensions = [
    Extension(
        "my_module",
        ["my_module.pyx"],
        include_dirs=include_dirs,
        define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        language="c++"
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        language_level=3,   # 设置 Python 3
        compiler_directives={
            'boundscheck': False,   # 不检查在访问数组/列表时检查下标是否越界
            'wraparound': False     # 不允许负索引
        }
    )
)