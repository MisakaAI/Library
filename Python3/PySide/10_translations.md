# 翻译应用程序

`Qt Linguist` 和其相关工具可用于为应用程序提供翻译。

翻译的工作原理是通过查找翻译的函数调用，传递消息字符串。
每个 `QObject` 实例都为此提供一个 `tr()` 函数。
还有 `QCoreApplication.translate()`，用于将翻译后的文本添加到非 `QObject` 类中。

## 参考文献

- [Qt Linguist](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/translations.html)
