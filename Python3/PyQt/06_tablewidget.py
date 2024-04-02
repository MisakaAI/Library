# 导入QTableWidget、QTableWidgetItem和QColor以显示 背景颜色
import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QTableWidget, QTableWidgetItem)

# 创建一个简单的数据模型，其中包含不同的颜色
colors = [("Red", "#FF0000"),
          ("Green", "#00FF00"),
          ("Blue", "#0000FF"),
          ("Black", "#000000"),
          ("White", "#FFFFFF"),
          ("Electric Green", "#41CD52"),
          ("Dark Blue", "#222840"),
          ("Yellow", "#F9E56d")]

# 定义一个函数将十六进制代码转换为RGB等效值

def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])

# 初始化 QApplication 实例
app = QApplication()

# 将 QTableWidget 配置为具有和 colors 同等的行及列。
table = QTableWidget()
table.setRowCount(len(colors))
table.setColumnCount(len(colors[0]) + 1)

# 设置每列的名称，上面的+1列就是为了显示这个名称。
table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])

# 迭代数据结构，创建 QTableWidgetItems 实例， 使用 x, y 坐标将它们添加到表中。
for i, (name, code) in enumerate(colors):
    item_name = QTableWidgetItem(name)
    item_code = QTableWidgetItem(code)
    item_color = QTableWidgetItem()
    item_color.setBackground(get_rgb_from_hex(code))
    table.setItem(i, 0, item_name)
    table.setItem(i, 1, item_code)
    table.setItem(i, 2, item_color)

# 显示表并执行 QApplication
table.show()
sys.exit(app.exec())
