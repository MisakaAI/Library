import sys
sys.path.append('.')

# # 导入 Cython 编译后的模块
import my_module
import numpy as np
# 调用模块中的函数

a = np.array([5], dtype=np.int32)
b = np.array([3], dtype=np.int32)
result = my_module.power(a, b)

# 打印返回的模块
print(result)