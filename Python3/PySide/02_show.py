from PySide6.QtWidgets import QApplication, QLabel

# 创建一个 QApplication 实例
app = QApplication([])

# QLabel 是一个可以显示文本的小部件
label = QLabel("Hello World!")

# 这种 HTML 方法也有效
# label = QLabel("<font color=red size=40>Hello World!</font>")

# 创建标签后，在上面调用 show()
label.show()

# 调用 app.exec() 进入Qt主循环并启动 执行Qt代码
app.exec()