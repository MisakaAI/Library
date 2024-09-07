# 数字

## 数字解析

`Parse` 方法通常用于将字符串转换为其他数据类型。

```cs
string intString = "450";
int number = int.Parse(numberString);  // 450

string floatString = "12.45";
double number = double.Parse(floatString);  // 结果是 12.45
```

## 数字格式化

在 `.Net` 中，区域信息用 `System.Globalization.CultureInfo` 类来表示。

```cs
using System.Globalization;

int a = 12450;

CultureInfo cInfo_cn = new CultureInfo("zh-CN");
CultureInfo cInfo_en = CultureInfo.CreateSpecificCulture("en-US");

Console.WriteLine(cnInfo);
Console.WriteLine(a.ToString("c", cnInfo)); // ¥12,450.00
Console.WriteLine(enInfo);
Console.WriteLine(a.ToString("c", enInfo)); // $12,450.00
```

## System.Math

`System.Math` 是一个工具类，提供了数学运算的静态方法。

其中包含两个静态 `final double` 字段：`E`和`PI`

- `E` 表示自然对数的底数，它的值接近`2.718`
- `PI` 是圆的周长与直径的比例系数，它的值是`22/7`，约等于`3.1428`

## 常用方法

```cs
// public ststic double Abs(double a)

// 绝对值
Math.Abs(-0.6); // 0.6

// 反余弦，范围在 0.0 到 pi 之间
Math.Acos(0.6); // 0.9272952180016123

// 反正弦，范围在 -pi/2 到 pi/2 之间
Math.Asin(0.6); // 0.6435011087932844

// 反正切，范围在 -pi/2 到 pi/2 之间
Math.Atan(0.6); // 0.5404195002705842

// 余弦
Math.Cos(0.6); // 0.8253356149096783

// 正弦
Math.Sin(0.6); // 0.5646424733950354

// 正切
Math.Tan(0.6); // 0.6841368083416923

// 欧拉数 e 的 double 次幂
Math.Exp(0.6); // 1.8221188003905089

// 自然对数（底数是e）
Math.Log(0.6); // -0.5108256237659907

// 底数为 10 的对数
Math.Log10(0.6); // -0.2218487496163564

// 两个值中较大的一个
Math.Max(0.6, 1.2); // 1.2

// 两个值中较小的一个
Math.Min(0.6, 1.2); // 0.6
```
