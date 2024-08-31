# 数组

数组是一个对象。
数组是从 `System.Array` 派生而来的类的实例。
数组中的所有元素都必须是相同的数据类型。
数组的大小是固定的，带有0个元素的数组叫做空数组。
数组的索引从 0 开始。

## 声明数组

```cs
int[] n; // 声明一个整型数组
string[] hello; // 声明一个字符串数组
```

## 初始化数组

创建数组时，元素通常是 `null` 或 该元素类型的默认值。
例如 `int` 类型的数组，默认值为 `0`。


```cs
// 声明数组的同时指定数组的大小
int[] n = new int[5];

// 在初始化时直接赋值
string[] hello = new string[] { "Hello", " ", "World" };
int[] n = { 1, 2, 3, 4, 5 }; // 更简洁的写法 省略 new
```

## 访问数组元素

```cs
Console.WriteLine(hello[0]);
Console.WriteLine(n[1]);
```

## 遍历数组

```cs
// for 循环遍历数组
for (int i = 0; i < n.Length; i++) {
    Console.WriteLine(n[i]);
}

// foreach 循环遍历数组
foreach (int i in n) {
    Console.WriteLine(i);
}
```

## 常用方法

- `Length` 获取数组的长度（元素数量）
- `Array.Sort` 对数组进行排序
- `Array.Reverse` 元素反转

调用 `Array.Sort` 和 `Array.Reverse` 之后，**数组仍然是同一个对象**。

```cs
int[] n = { 3, 1, 4, 5, 2 };
int length = n.Length; // 5
Array.Sort(n); // { 1, 2, 3, 4, 5 }
Array.Reverse(n); // { 5, 4, 3, 2, 1 }
Array.Resize(ref n, 9); // { 5, 4, 3, 2, 1, 0, 0, 0, 0 }
```

## 改变数组大小

`Array.Resize` 实际上会创建一个新的数组对象，并将原始数组的元素复制到新的数组中。
因此，调用 `Array.Resize` 之后，**数组将不再是同一个对象**。

```cs
int[] n = { 5, 4, 3, 2, 1 };
Array.Resize(ref n, 9); // { 5, 4, 3, 2, 1, 0, 0, 0, 0 }
```

## 多维数组

### 二维数组（矩阵）

多维数组用多个方括号来表示。

```cs
// 声明一个 3x3 的二维数组
int[,] matrix = new int[3, 3];

// 初始化二维数组
int[,] matrix = {
    { 1, 2, 3 },
    { 4, 5, 6 },
    { 7, 8, 9 }
};

// 访问二维数组元素
int element = matrix[0, 1]; // 2

// 修改二维数组元素
matrix[0, 1] = 10; // 将第一个数组的第二个元素修改为 10
```

### 锯齿数组（交错数组）

即数组的数组，每个子数组可以有不同的长度。

```cs
// 声明一个包含 3 个子数组的锯齿数组
int[][] jaggedArray = new int[3][];

// 初始化子数组
jaggedArray[0] = new int[] { 1, 2, 3 };
jaggedArray[1] = new int[] { 4, 5 };
jaggedArray[2] = new int[] { 6, 7, 8, 9 };

// 访问锯齿数组元素
int element = jaggedArray[0][1]; // 2

// 遍历锯齿数组
foreach (int[] array in jaggedArray)
{
    foreach (int number in array)
    {
        Console.WriteLine(number);
    }
}
```
