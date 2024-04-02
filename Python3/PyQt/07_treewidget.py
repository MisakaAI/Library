# 使用 QTreeWidget 显示以树形式排列的数据
# 为该应用程序导入 QTreeWidget 和 QTreeWidgetItem
import sys
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

# 定义一个包含项目结构的字典，以将信息显示为 树
data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
        "Project B": ["file_b.csv", "photo.jpg"],
        "Project C": []}

# 初始化 QApplication 实例
app = QApplication()

# 将 QTreeWidget 配置为具有两列。
# 一列用于项目名称， 另一个用于项目中文件的项类型信息的目录
tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Name", "Type"])

# 迭代数据结构，创建 QTreeWidgetItem 元素
items = []
for key, values in data.items():
    item = QTreeWidgetItem([key])
    for value in values:
        ext = value.split(".")[-1].upper()
        child = QTreeWidgetItem([value, ext])
        item.addChild(child)
    items.append(item)

tree.insertTopLevelItems(0, items)

# 显示树并执行 QApplication
tree.show()
sys.exit(app.exec())