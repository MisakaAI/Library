# 信号与插槽

`QObject` 需要一种通信的方式。

点击一个按钮时，「点击」是一个信号。
「插槽」插槽可用于接收信号，例如：当按钮被点击时，关闭窗口、保存文档等操作。

可以将任意多个信号连接到单个插槽，一个信号也可以连接到任意数量的插槽。

## 参考文献

- [Signals and Slots](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/signals_and_slots.html)