# 命令行与环境

[命令行与环境](https://docs.python.org/zh-cn/3.10/using/cmdline.html)

## 命令行

一些常用的参数。

```bash
# 执行 command 中的 Python 代码。
-c <command>

# 在 sys.path 中搜索指定模块
-m <module-name>

# 输出所有命令行选项的简介
-?
-h
--help

# 输出 Python 版本号并退出
-V
--version

# 执行脚本或命令后，也会进入交互模式。
-i

```

下面这几个是我不怎么用的，但是也许对你有用。

```bash

# 在隔离模式下运行 Python。
-I

# 忽略所有 PYTHON* 环境变量
-E

# 开启解析器调试输出（限专家使用，依赖于编译选项）
-d

# 即使在交互模式下也不显示版权和版本信息。
-q

# 开启哈希随机化。
-R

# 移除 assert 语句以及任何以 __debug__ 的值作为条件的代码
-O

# 在启用 -O 的同时丢弃文档字符串。
-OO

# 不要将 用户 site-packages 目录 添加到 sys.path
-s

# 禁用 site 的导入及其所附带的基于站点对 sys.path 的操作
-S

# 强制 stdout 和 stderr 流不使用缓冲。 此选项对 stdin 流无影响。
-u

# 每次在初始化模块时会打印一条信息，显示被加载的地方（文件名或内置模块名）。
-v

# 警告信息的控制。Python 的警告机制默认将警告信息打印到 sys.stderr。
-W <arg>

<arg>
-Wdefault  # 每次调用时警告一次
-Werror    # 转换为例外情况
-Walways   # 每次都发出警告
-Wmodule   # 对每个调用模块警告一次
-Wonce     # 每个Python进程警告一次
-Wignore   # 绝不警告

# 跳过源中第一行，以允许使用非 Unix 形式的 #!cmd。 这适用于 DOS 专属的破解操作。
-x

# 保留用于各种具体实现专属的选项。
-X

# 保留给 Jython 使用，不应当使用的选项
-J
```

## 环境变量

变量|说明
-|-
PYTHONHOME|更改标准 Python 库的位置。
PYTHONPATH|增加模块文件默认搜索路径。
PYTHONCOERCECLOCALE|如果值设为 0，将导致主 Python 命令行应用跳过将传统的基于 ASCII 的 C 与 POSIX 区域设置强制转换为更强大的基于 UTF-8 的替代方案。
PYTHONUTF8|如果设为 1 ，将会启用 Python UTF-8 模式。<br>若设为 0 ，则会禁用 Python UTF-8 模式 。

其他的看文档吧，用得到的时候再添加。