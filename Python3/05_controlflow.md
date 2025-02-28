# 流程控制

`breakpoint()` 添加断点

`if` 有条件的执行

```py
x=1
if x = 0:
    pass
elif x = 1:
    pass
else:
    pass
```

`for` 对序列（例如字符串、元组或列表）或其他可迭代对象中的元素进行迭代

```py
for i in range(10):
    print(i)
```

`while` 在表达式保持为真的情况下重复地执行

```py
while True:
    pass
```

`range()` range函数可以生成算术级数

```py
>>> list(range(5))
[0, 1, 2, 3, 4]

>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]

```

`break` 跳出最近的 for 或 while 循环
`continue` 跳过本次循环的后续内容，继续执行循环的下一次迭代
`else` 循环的 else 子句在未运行 break 时执行

```py
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
```

`pass` 不执行任何操作,语法上需要一个语句，但程序不实际执行任何动作时，使用该语句。

```py
def f():
    pass
```

`match` 将一个目标值与一个或多个字面值进行比较

```py
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"
```

`_` 作为 通配符 并必定会匹配成功
没有 case 语句匹配成功，则不会执行任何分支。
使用 `|` （“ or ”）在一个模式中可以组合多个字面值。

更详细的说明看官网[match](https://docs.python.org/zh-cn/3.11/tutorial/controlflow.html#match-statements)

