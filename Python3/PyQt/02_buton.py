#!/usr/bin/python

# 导入模块
import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

# 创建一个python函数
@Slot()
def say_hello():
    print("Button clicked, Hello!")

# 创建一个Python应用
app = QApplication(sys.argv)

# 创建一个按钮，连接并显示
button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()

# 运行
app.exec()
