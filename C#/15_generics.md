# 泛型

泛型（Generics）是允许在类、接口、方法和委托中定义类型参数的功能。
通过泛型，你可以编写类型安全且具有高复用性的代码，而不必在使用不同数据类型时重复编写相同逻辑。泛型允许代码在编译时对类型进行约束，从而提高性能和类型安全性。

```cs
struct Point<T>
{
    T x;
    T y;

    public Point(T x, T y)
    {
        this.x = x;
        this.y = y;
    }

    public T X
    {
        get { return x; }
        set { this.x = value; }
    }

    public T Y
    {
        get { return y; }
        set { this.y = value; }
    }

    public void Print()
    {
        Console.WriteLine("({0},{1})",x,y);
    }
}
class Program
{
    static void Main()
    {

        Point<int> a = new Point<int>();
        Point<double> b = new Point<double>(1.1, 2.2);
        a.Print(); // (0,0)
        b.Print(); // (1.1,2.2)
    }
}
```

## 常见泛型类

### 动态数组

`List<T>` 可以存储任意类型的对象。

```cs
List<int> numbers = new List<int> { 1, 2, 3 };
```

### 键值对集合

`Dictionary<TKey, TValue>` 键值对集合。

```cs
Dictionary<string, int> ages = new Dictionary<string, int>
{
    {"Alice", 25},
    {"Bob", 30}
};
```
