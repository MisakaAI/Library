# 类 Class

在C#中，类定义必须保存成一个带.cs后缀的文件。
文件名不一定非要和类名相同。

```cs
class 类名称
{
    类内容
}
```

## 字段 Field

字段通常在类或结构体的内部定义，并可以使用访问修饰符（如 `public`、`private`）来控制它们的访问级别。

1. 访问级别：字段可以有不同的访问修饰符来控制它们的可见性和访问权限。

2. 静态字段（Static Field）：
使用 `static` 关键字定义的字段属于类本身，而不是某个实例。
静态字段在所有实例之间共享。

3. 只读字段（Read-Only Field）：
使用 `readonly` 关键字定义的字段只能在定义时或构造函数中赋值，之后不能修改。
这种字段通常用于常量数据或初始化后不应改变的值。

4. 常量字段（Constant Field）：
使用 `const` 关键字定义的字段在编译时必须赋值，并且之后不能再更改。
常量字段是隐式 `static` 的。

## 方法

方法定义了一个类的对象（或实例）能做的动作。

声明语法：`返回类型 方法名称 (参数)`

```cs
class Employee // 雇员
{
    int Age; // 年龄
    double Salary; // 薪水

    int Add(int a, int b) // 方法
}
```

## Main 方法

Mian() 作为程序的入口

```cs
class Program
{
    static void Main() {
        Console.WriteLine("Hello World!");
    }
}
```

## 构造函数

每个类必须至少有一个构造函数，否则这个类就不能创建对象。
构造函数和方法一样，但是没有返回值。
构造函数的名称与类名相同。

```cs
class Employee
{
    public static int numberOfEmployees; // 静态变量，用于跟踪员工总数
    public string Name;
    public int Age;

    // 构造函数
    public Employee(string name, int age)
    {
        Name = name;
        Age = age;
        numberOfEmployees+=1
    }
}
```

## 创建对象

使用关键字 `new`

```cs
new Employee();
Employee employee = new Employee();
```

## null 关键字

一个引用变量引用一个变对象。
如果引用变量没有值，则引用变量有一个 `null` 值。

## 命名空间

命名空间允许为自己的类型创建独立的名称，避免和其他类型产生冲突。

```cs
namespace MyNamescape
{
    class MyClass
    {

    }
}
```

如果没有将类声明在一个命名空间中，C#编译器会加上一个默认的命名空间 `globe`

> `.NET Framework` 也用命名空间输出它的类库。
>
>```cs
>using System;
>Console.WriteLine("Hello World!");
>```
>
>等于
>
>```cs
>System.Console.WriteLine("Hello World!");
>```

## 封装和类的访问控制

C#使用访问修饰符来控制类的可见性和访问权限。

- `public`：公众的，访问不受限制。
- `private`：受保护的，只能在类内部访问。
- `protected`：私有的，可以在类本身及其子类中访问。
- `internal`：内部的，访问仅限于当前程序集。

默认情况下类是 `internal` 的，除非明确的声明为`public`。

## 关键字 this

可以在任意方法和构造函数中使用关键字 `this` 表示当前对象。

```cs
this.Age
```

## 使用其他类

使用同一个命名空间中的类作为当前类是允许的。
但是，要使用另一个命名空间的类，必须先使用关键字 `using` 来导入命名空间。

```cs
using System;
Console.WriteLine("Hello World!");
```

等于

```cs
System.Console.WriteLine("Hello World!");
```

## 静态成员

静态成员不需要先实例化就可以调用类成员。

```cs
public static int NumberOfPages;
static public int NumberOfPages;
```

## 方法重载

C# 允许多个方法具有相同的名称。
只要每个方法所接受的参数类型组合不同就可以。

```cs
public void PrintString(String string);
public void PrintString(String string, int offset);
```

## 示例

```cs
class Person
{
    // 字段声明
    public string name;      // 公有字段
    private int age;         // 私有字段
    public static int count; // 静态字段

    // 构造函数
    public Person(string name, int age)
    {
        this.name = name;
        this.age = age;
        count++;  // 每次创建新对象时，count 加 1
    }

    // 方法：返回 Person 的描述
    public string GetDescription()
    {
        return $"Name: {name}, Age: {age}";
    }
}

class Program
{
    static void Main()
    {
        Person p1 = new Person("Alice", 30);
        Person p2 = new Person("Bob", 25);

        Console.WriteLine(p1.GetDescription());  // 输出 "Name: Alice, Age: 30"
        Console.WriteLine(p2.GetDescription());  // 输出 "Name: Bob, Age: 25"
        Console.WriteLine(Person.count);         // 输出 "2"
    }
}
```
