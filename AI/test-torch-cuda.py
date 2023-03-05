#!/bin/env python3

import torch

# 返回当前设备索引
print(torch.cuda.current_device())

# 返回GPU的数量
print(torch.cuda.device_count())

# 返回gpu名字，设备索引默认从0开始
print(torch.cuda.get_device_name(0))

# cuda是否可用，为true就可用了
print(torch.cuda.is_available())

#查看cudnn版本
print(torch.backends.cudnn.version())

#查看torch版本
print(torch.__version__)