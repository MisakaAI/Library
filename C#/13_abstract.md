# 抽象类

抽象类（abstract class）是一种无法直接实例化的类，通常作为其他类的基类来使用。
抽象类定义了一些通用的行为或特性，但它本身并不完整，必须通过继承的方式由子类实现具体的功能。
抽象类的主要作用是为子类提供一种通用的接口或模板，让子类可以继承并扩展它。

## 为什么使用抽象类

当多个类有相似的行为或属性时，可以将这些相似性提取到抽象类中，避免代码重复。
抽象类可以作为基础类，定义通用的接口，同时让不同的子类实现特定的细节。

## 抽象类的特点

### 不能实例化

不能直接创建抽象类的对象，必须通过继承由子类实例化。

```cs
// 错误的示例：不能实例化抽象类
AbstractClass obj = new AbstractClass();
```

### 可以包含抽象方法

抽象类中可以包含抽象方法，这些方法没有方法体，必须在继承的子类中实现。

如果基类中的方法使用了 `virtual` (虚方法)，表示该方法可以在派生类中被重写。
如果基类中的方法是 `abstract` （抽象方法）的，那么派生类必须重写这个方法。

当子类重写基类方法时，必须在方法前使用 `override` 关键字。

```cs
abstract class Shape
{
    // 抽象方法，没有方法体
    public abstract void Draw();
}

class Circle : Shape
{
    // 子类中必须实现抽象方法
    public override void Draw()
    {
        Console.WriteLine("Drawing a circle.");
    }
}
```

### 可以包含普通方法

除了抽象方法，抽象类还可以包含普通的非抽象方法，这些方法在抽象类中已经实现，可以在子类中直接使用或重写。

```cs
abstract class Shape
{
    public abstract void Draw(); // 抽象方法

    public void Move() // 普通方法
    {
        Console.WriteLine("Moving the shape.");
    }
}
```

### 可以有属性、字段、构造函数

抽象类可以包含属性、字段和构造函数，与普通类类似。
抽象类的构造函数通常用于被子类调用，以初始化通用的成员。

```cs
abstract class Animal
{
    public string Name { get; set; } // 字段

    public Animal(string name) // 构造函数
    {
        Name = name;
    }

    public abstract void Speak(); // 抽象方法
}
```

### 子类必须实现抽象方法

任何继承抽象类的子类都必须实现抽象类中的所有抽象方法，除非子类本身也是抽象的。

```cs
abstract class Bird
{
    public abstract void Fly(); // 抽象方法
}

class Sparrow : Bird
{
    // 子类中必须实现抽象方法
    public override void Fly()
    {
        Console.WriteLine("Sparrow is flying.");
    }
}
```
