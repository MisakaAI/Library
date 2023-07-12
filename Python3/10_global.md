# 全局变量

Python 中定义函数时，若想在函数内部对函数外的变量进行操作，就需要在函数内部声明其为 `global`

## 解释

### 例子1

```python
x = 1
def func():
    x = 2
func()
print(x)
```

输出：1
在 `func` 函数中，并未在 `x` 前面加 `global` ，所以 `func` 函数无法将 `x` 赋为2，无法改变 `x` 的值。

### 例子2

```python
x = 1
def func():
    global x
    x = 2

func()
print(x)
```

输出：2
加了 `global` ，则可以在函数内部对函数外的对象进行操作了，也可以改变它的值了。

### 例子3

```python
global x
x = 1
def func():
    x = 2
func()
print(x)
```

输出：1
`global` 需要在函数内部声明，若在函数外声明，则函数依然无法操作 `x`。

## 参考文献

- [Python的global语句使用](https://blog.csdn.net/xtingjie/article/details/71210182)