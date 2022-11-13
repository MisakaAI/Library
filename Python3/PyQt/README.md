# PyQt

Qt在Python中有两个分支。

[PyQt](https://www.riverbankcomputing.com/software/pyqt/) 是由 Riverbank Computing 公司开发，出现的比较早。
采用 `GPLv3` 许可证和商业许可证发布，这表示你如果使用 PyQt6 ，则必须将你的代码进行开源，如果要闭源，则需要购买商业许可。

[PySide](https://doc.qt.io/qtforpython/) 采用 `LGPL` 许可发布，这意味着只要你以调用动态链接库的形式使用 Qt ，你可以以任何形式（商业、非商业、开源、非开源）发布你的程序。

本文使用的Qt的版本为`pyside6`

## 安装

```bash
# PyQt
pip install PyQt6

# PySide
pip install pyside6
```

## 工具

目录：`%LocalAppData%\Programs\Python\Python311\Scripts`

`pyside6-designer.exe` Qt Designer，可轻松画出UI
`pyside6-genpyi.exe` 为所有PySide模块生成.pyi文件
`pyside6-rcc.exe` Qt资源编译工具
`pyside6-uic.exe` 用于将.ui文件转换成.py文件

## 目录

- [Hello World](./00_hello_world.py)
- [Qt的Python模块](./01_Modules.md)
- []()
- []()