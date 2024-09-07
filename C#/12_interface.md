# 接口

C# 中的接口是一个定义了一组方法、属性、事件或索引器的契约，它只声明这些成员的签名而不提供实现。
接口是一种抽象类型，用于定义类或结构必须遵循的规范，但不涉及具体的实现细节。

接口属性通常没有主体。
访问器指示属性是读写、只读还是只写。
与在类和结构中不同，在没有主体的情况下声明访问器不会声明自动实现的属性。
接口可为成员（包括属性）定义默认实现。
在接口中为属性定义默认实现的情况非常少，因为接口无法定义实例数据字段。

## 声明接口

使用 `interface` 关键词来声明接口。
接口的成员默认都是 `public`，不能包含访问修饰符。
按照惯例，接口的名称使用大写字母 `I` 作为前缀。

```cs
interface IEmployee
{
    string Name
    {
        get; // 读
        set; // 写
    }

    int Counter { get; } // 只读
}
```

## 实现接口的类

其他人实现的 `IEmployee` 接口，一定能用的只有 `Name` 和 `Counter`
但是 `numberOfEmployees`，不在 `IEmployee` 接口定义规范内，就不一定能用了。

```cs
public class Employee : IEmployee
{
    public static int numberOfEmployees; // 静态变量，用于跟踪员工总数

    private string _name;
    public string Name  // 实现接口的可读写属性
    {
        get => _name; // 返回私有字段 _name 的值
        set => _name = value; // 设置私有字段 _name 的值
    }

    private int _counter;
    public int Counter  // 实现接口的只读属性
    {
        get => _counter; // 返回私有字段 _counter 的值
    }

    // 构造函数
    public Employee() => _counter = ++numberOfEmployees;
}
```

## 完整示例

```cs
using System;
interface IEmployee
{
    string Name { get; set; }
    int Counter { get; }
}

public class Employee : IEmployee
{
    public static int numberOfEmployees;

    private string _name;
    public string Name  // read-write instance property
    {
        get => _name;
        set => _name = value;
    }

    // _name 是一个字段（field），它的作用是存储 Name 属性的实际值。
    // 字段通常用于在类内部保存数据。
    // 当调用 Name 时，返回 _name
    // 当为 Name 赋值时，将 value 赋值给 _name

    private int _counter;
    public int Counter  // read-only instance property
    {
        get => _counter;
    }

    // constructor
    public Employee() => _counter = ++numberOfEmployees;
}

class Program
{
    static void Main()
    {
        System.Console.Write("Enter number of employees: ");
        Employee.numberOfEmployees = int.Parse(System.Console.ReadLine());

        Employee e1 = new Employee();
        System.Console.Write("Enter the name of the new employee: ");
        e1.Name = System.Console.ReadLine();

        System.Console.WriteLine("The employee information:");
        System.Console.WriteLine("Employee number: {0}", e1.Counter);
        System.Console.WriteLine("Employee name: {0}", e1.Name);
    }
}
```
