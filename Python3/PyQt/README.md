# PyQt

Qt在Python中有两个分支。

[PyQt](https://www.riverbankcomputing.com/software/pyqt/) 是由 Riverbank Computing 公司开发，出现的比较早。

采用 `GPLv3` 许可证和商业许可证发布，这表示你如果使用 PyQt6 ，则必须将你的代码进行开源，如果要闭源，则需要购买商业许可。

[PySide](https://doc.qt.io/qtforpython/) Qt for Python

PySide 遵循与 Qt 相同的许可协议，这意味着有两个发行版，社区版 `(LGPLv3/GPLv3)` 和商业版。
详细信息请查看[Qt许可](https://www.qt.io/licensing)。

简单的来说，LGPL 允许商业软件通过类库引用 (link) 方式使用 LGPL 类库而不需要开源商业软件的代码。

关于议的具体说明，可以参考[《编程与调试 C++ -- Qt 的 LGPL 协议》](https://blog.hawkhai.com/blog/2022/08/10/qt-lgpl)一文。

因此，本文使用的 Qt 的版本为`pyside6`

## 安装

```bash
# PyQt
# pip install PyQt6

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
- [Qt模块](./01_Modules.md)
- [显示窗口](./02_show.py)
- [创建按钮](./03_buton.py)
- [信号与插槽](./04_signals_and_slots.md)
- [创建对话框](./05_dialog.py)
- [使用表格小部件检查数据](./06_tablewidget.py)
- [使用树小部件搜索数据](./07_treewidget.py)
- [.ui 文件(pyside6-designer)](./08_uifiles.md)
- [.qrc 文件(pyside6-rcc)](./09_qrcfiles.md)
- [翻译应用程序](./10_translations.md)
- [应用程序样式](./11_widgetstyling.md)

## 参考文献

- [Documentation](https://doc.qt.io/qtforpython-6/index.html)
- [PySide6-Code-Tutorial](https://github.com/muziing/PySide6-Code-Tutorial)