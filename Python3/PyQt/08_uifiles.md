# 使用 .ui 文件

`Qt Designer` 是一个图形化的UI设计工具，是一个独立的二进制文件（pyside6-designer）。
也被嵌入到了 `Qt Creator IDE` 中。

设计存储在.ui文件中，这是一种基于XML的格式。
在项目构建时为它填充小部件实例，使用 `pyside6-uic` 工具可以将它转换为 Python 或 C++ 代码。

## 生成 Python 类

与 UI 文件交互的标准方法是生成一个 Python 类。
需要在控制台上运行以下命令：

```sh
pyside6-uic mainwindow.ui -o ui_mainwindow.py
```

命令的所有输出重定向到一个名为 `ui_mainwindow.py` 的文件。

使用时，，使用 `from ui_mainwindow import Ui_MainWindow` 在程序中直接导入该文件。

```py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
```

## 直接加载

也可以直接加载UI文件。

```py
from PySide6.QtUiTools import QUiLoader

ui_file = QFile("mainwindow.ui")
ui_file.open(QFile.ReadOnly)

loader = QUiLoader()
window = loader.load(ui_file)
window.show()
```
