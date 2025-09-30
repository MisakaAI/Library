# my_module.pyx
import numpy as np
cimport numpy as np

# 指定 NumPy 数组类型
def power(np.ndarray[np.int32_t, ndim=1] a, np.ndarray[np.int32_t, ndim=1] b):
    """
    输入两个 NumPy 整数数组 a 和 b，返回 a ** b
    """
    cdef int n = a.shape[0]
    if b.shape[0] != n:
        raise ValueError("Arrays must have the same length")
    cdef np.ndarray[np.int32_t, ndim=1] result = np.empty(n, dtype=np.int32)
    cdef int i
    for i in range(n):
        result[i] = a[i] ** b[i]
    return result
