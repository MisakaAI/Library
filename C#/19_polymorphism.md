# 多态

- [多态性](https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/object-oriented/polymorphism)

多态（Polymorphism）是一种面向对象编程的特性，允许对象以不同的形式呈现。它有助于实现代码的灵活性和可扩展性。
多态主要通过**继承**和**接口**来实现。

基类可以定义并实现虚方法，派生类可以重写这些方法，即派生类提供自己的定义和实现。
在运行时，客户端代码调用该方法，CLR 查找对象的运行时类型，并调用虚方法的重写方法。

> CLR（Common Language Runtime，通用语言运行时）
> 是.NET框架的一部分，负责执行和管理由不同编程语言（如C#、VB.NET等）编写的代码。

## 编译时多态性

静态多态性，也称为方法重载（Method Overloading）和运算符重载（Operator Overloading）。
在编译时，方法的调用是根据方法的参数个数或类型来确定的。

```cs
class Example
{
    public void Print(int a)
    {
        Console.Write("int: ");
        Console.WriteLine(a);
    }

    public void Print(string a)
    {
        Console.Write("string: ");
        Console.WriteLine(a);
    }
}

var obj = new Example();
obj.Print(5);    // int: 5
obj.Print("Hello");  // string: Hello
```

## 运行时多态性

动态多态性，通过方法重写（Method Overriding）和接口实现（Interface Implementation）来实现。
运行时多态性允许一个子类提供对其父类或接口中的方法不同的实现。它依赖于继承和虚方法（virtual）、抽象方法（abstract）或接口方法的实现。

```cs
class Animal
{
    public virtual void Speak()
    {
        Console.WriteLine("Animal speaks");
    }
}

class Dog : Animal
{
    public override void Speak()
    {
        Console.WriteLine("Dog barks");
    }
}

Animal myAnimal = new Dog();
myAnimal.Speak();  // Dog barks
```

虽然变量`myAnimal`的类型是`Animal`，但因为它实际引用了`Dog`对象。
CLR 会在运行时调用`Dog`类的`Speak`方法。
这就是多态性与 CLR 在运行时的工作方式。
