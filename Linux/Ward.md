# Ward

Ward 是一款简约的高颜值的服务器监控工具，拥有很漂亮的仪表盘，同时支持神色主题。

```bash
# 克隆
git clone https://github.com/AntonyLeons/Ward

# 进入项目目录
cd Ward

# 构建
docker build . --tag ward

# 运行
docker run --restart unless-stopped -it -d --name ward  -p 5689:5689 -e WARD_PORT=5689 -e WARD_THEME=light --privileged ward
```

1. 处理器名称
1. 处理器利用率百分比
1. 处理器内核数（逻辑和物理内核）
1. 处理器的当前频率
1. 处理器是否支持 64 位指令

1. 操作系统类型及其版本
1. RAM 利用率百分比
1. 已安装 RAM 总量
1. 已安装 RAM 的生成（如果您有 dmidecode）
1. 当前进程计数

1. 存储名称
1. 存储利用率百分比
1. 当前安装的总存储空间（包括外部驱动器）
1. 已安装磁盘数
1. 虚拟内存总量（Linux 中的交换）

1. 此块包含正常运行时间和图表部分。
1. 正常运行时间表示自上次在 Linux 上启动以来的时间，以及在 Windows 上硬重置之间的时间。
1. 它还具有分页器，可用于获取作者联系人。
1. 图表部分显示最后 15 秒的服务器利用率。
（处理器、内存、存储）您可以通过单击图表部分右上角的矩形来隐藏分离的数据集。
