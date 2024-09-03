# 结构

结构和类一样拥有字段或方法这样的成员。
但结构是值类型，不能继承。

C#的所有基本类型，都是 `System` 命名空间中多定义的结构的别名。

```cs
int a = 1;
System.Int32 b = 1;

Console.WriteLine(a.GetType()); // System.Int32
```

## 编写一个结构

编写一个结构，包括两个字段和两个方法。

```cs
struct Point
{
    public int X;
    public int Y;

    public void Move(int x, int y)
    {
        X+=x;
        Y+=y;
    }

    public void Print()
    {
        System.Console.WriteLine("(" + X + "," + Y + ")");
    }

}
class Program
{
    static void Main()
    {
        Point p1 = new Point();
        p1.Print();
        p1.X = 10;
        p1.Y = 20;
        p1.Move(4,5);
        p1.Print();
    }
}
```

## 可为空的类型

通常，引用类型如 `string` 可以为`null`，而值类型不能。
通过使用`nullable`，你可以让值类型也能表示`null`。
通过在值类型后面加上`?`来定义一个`nullable`类型。
使用`HasValue`属性来检查`nullable`变量是否有值。
`null-coalescing`运算符允许你在`nullable`类型为`null`时提供一个默认值。
可以使用`??=`运算符将`nullable`类型赋值为某个默认值（如果它为`null`）。

```cs
int? number = null;

if (number.HasValue)
{
    Console.WriteLine($"Number: {number.Value}");
}
else
{
    Console.WriteLine("Number is null");
}

int result = number ?? 0; // 如果 number 为 null，则 result 为 0
number ??= 10; // 如果 number 为 null，则赋值为 10
```
