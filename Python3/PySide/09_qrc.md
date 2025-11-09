# 使用 .qrc 文件

[Qt资源系统](https://doc.qt.io/qt-5/resources.html)是一种在一个应用程序中存储二进制文件的机制。

这些文件将通过QFile类以及QIcon和QPixmap的构造函数，嵌入到应用程序中。
使用以:/开头的特殊文件名来获取。

最常见的用途是自定义图像、图标、字体等。

## 创建 .qrc 文件

在运行任何命令之前，将有关资源的信息添加到 .qrc 文件。
在下面的示例中，请注意 icons.qrc 中列出的资源。

```xml
</ui>
<!DOCTYPE RCC><RCC version="1.0">
<qresource>
    <file>icons/play.png</file>
    <file>icons/pause.png</file>
    <file>icons/stop.png</file>
    <file>icons/previous.png</file>
    <file>icons/forward.png</file>
</qresource>
</RCC>
```

## 生成 Python 文件

```sh
pyside6-rcc icons.qrc -o rc_icons.py
```

## 使用

```py
import rc_icons

# 现有示例
# from PySide6.QtGui import QIcon, QKeySequence
# playIcon = self.style().standardIcon(QStyle.SP_MediaPlay)
# previousIcon = self.style().standardIcon(QStyle.SP_MediaSkipBackward)
# pauseIcon = self.style().standardIcon(QStyle.SP_MediaPause)
# nextIcon = self.style().standardIcon(QStyle.SP_MediaSkipForward)
# stopIcon = self.style().standardIcon(QStyle.SP_MediaStop)

# 修改为下面的
from PySide6.QtGui import QIcon, QKeySequence, QPixmap
playIcon = QIcon(QPixmap(":/icons/play.png"))
previousIcon = QIcon(QPixmap(":/icons/previous.png"))
pauseIcon = QIcon(QPixmap(":/icons/pause.png"))
nextIcon = QIcon(QPixmap(":/icons/forward.png"))
stopIcon = QIcon(QPixmap(":/icons/stop.png"))
```
