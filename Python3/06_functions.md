# 函数

定义 函数使用关键字 def，后跟函数名与括号内的形参列表。
函数语句从下一行开始，并且必须缩进。

``py
# 斐波那契数列函数
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
```