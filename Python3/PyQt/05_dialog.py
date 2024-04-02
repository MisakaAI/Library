import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        # 创建小部件 输入框
        self.edit = QLineEdit("Write my name here")
        # 创建小部件 按钮
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        # 创建布局
        layout = QVBoxLayout()
        # 添加小部件
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        # 设置布局
        self.setLayout(layout)
        # Add button signal to greetings slot
        # 添加按钮的信号到 greetings 插槽
        self.button.clicked.connect(self.greetings)

    # Greets the user
    # 定义 greetings 插槽
    def greetings(self):
        print(f"Hello {self.edit.text()}")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())