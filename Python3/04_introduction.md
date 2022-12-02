# 简介

[Python 速览](https://docs.python.org/zh-cn/3.10/tutorial/introduction.html)

交互模式下，上次输出的表达式会赋给变量 `_`。

## 数字

整数：`int` [Int](https://docs.python.org/zh-cn/3.10/library/functions.html#int)
浮点数：`float` [Float](https://docs.python.org/zh-cn/3.10/library/functions.html#float)
混合类型运算数的运算，会把整数转换为浮点数

四则运算：`+` `-` `*` `/`
分组：`()`
乘方：`**`
余数：`%`

分数： `fractions` [Fraction](https://docs.python.org/zh-cn/3.10/library/fractions.html#fractions.Fraction)
十进制定点和浮点运算：`decimal` [Decimal](https://docs.python.org/zh-cn/3.10/library/decimal.html#decimal.Decimal)

## 字符串

[字符串](https://docs.python.org/zh-cn/3.10/library/stdtypes.html#textseq)

单引号 `允许包含有 "双" 引号`
双引号 `允许嵌入 '单' 引号`

三重引号 三重引号可以换行，所以某些时候可以作为注释使用。
```python
'''
使用三重引号的字符串可以跨越多行
'''

"""
其中所有的空白字符都将包含在该字符串字面值中
"""
```

### 转义

`\`，字符串前面加一个 `r` 不转义

```python
print(r'C:\some\name')
```

### 合并

```python
>>> 'A' + 'B'
'AB'
>>> 'A' 'B'
'AB'
>>> 'A' * 3
'AAA'
>>> 3 * 'B'
'BBB'
```

### 索引&切片

```python
# 因为 0 等于 -0 ，所以负数索引从 -1 开始。
# 省略开始索引时，默认值为 0，省略结束索引时，默认为到字符串的结尾。
>>> 'Python'[0]
'P'
>>> 'Python'[-1]
'n'
>>> 'Python'[2:4]
'th'
>>> 'Python'[:3]
'Pyt'
>>> 'Python'[-3:]
'hon'
>>> 'Python'[-3:-1]
'ho'
>>> 'Python'[-3:-2]
'h'
>>> 'Python'[:3] + 'Python'[-3:]
'Python'
```

### 字符串长度

```python
>>> len('Python')
6
```
