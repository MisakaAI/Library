# 继承

继承就是通过创建一个新的类来扩展一个类。
新创建的类和原来的类就会形成一种父子关系。

原来的类通常被称为父类（parent class）或基类（base class）
新的类通常被称为子类（child class）或派生类（derived class）

```cs
// 定义一个基类
public class Animal
{
    public float Weight;
    public void Eat() {
        Console.WriteLine("Eat");
    }
}

// 定义一个派生类，继承自 Animal 类
public class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("Barking");
    }
}
```

## 继承关系

`Dog` 是一种 `Animal`，但 `Animal` 不一定是 `Dog`。

子类继承了父类的所有 `public` 的方法和字段。

```cs
Dog dog = new Dog();
Dog.Eat();
Dog.Bark();
```

## 可访问性

子类中，可以访问父类的 `public` 和 `protected` 的成员。
但是不能访问父类的 `private` 成员。

如果子类和父类同一个程序集中，也可以访问超类的 `internal` 成员。

>- `public`：公众的，访问不受限制。
>- `private`：受保护的，只能在类内部访问。
>- `protected`：私有的，可以在类本身及其子类中访问。
>- `internal`：内部的，访问仅限于当前程序集。

## 方法覆盖

子类可以覆盖父类中的方法。
需要加上关键字 `new`。

```cs
public class Dog : Animal
{
    new public void Eat()
    {
        Console.WriteLine("Eat!!!!!");
    }
}
```

## 调用基类的构造函数

当创建子类对象时，基类的构造函数会首先被调用。
可以在子类的构造函数中显式地调用基类的构造函数。
使用 `base` 关键字可以指定要调用的基类构造函数。

```cs
public class Animal
{
    public string Name { get; }

    // 基类的构造函数
    public Animal(string name)
    {
        Name = name;
        Console.WriteLine("Animal constructor called");
    }
}

public class Dog : Animal
{
    public string Breed { get; }

    // 子类的构造函数，通过 base 关键字调用基类的构造函数
    public Dog(string name, string breed) : base(name)
    {
        Breed = breed;
        Console.WriteLine("Dog constructor called");
    }
}
```

```cs
Dog myDog = new Dog("Buddy", "Golden Retriever");
// 输出:
// Animal constructor called
// Dog constructor called
```

- `public`：访问修饰符，表示该属性可以从类外部访问。
- `string`：属性的类型，这里是字符串类型。
- `Name`：属性的名称。
- `{ get; }`：表示这个属性只有一个 `get` 访问器，意味着它是只读的。
没有 `set` 访问器，所以它只能在构造函数或属性初始化器中赋值，一旦对象创建后，该属性的值就不能再更改。

## 调用隐藏基类成员

在C#中，如果子类定义了与基类同名的成员（属性、方法或字段），那么子类的成员会隐藏基类的成员。
这种隐藏是通过 `new` 关键字显式声明的。
仍然可以通过 `base` 关键字调用被隐藏的基类成员。

```cs
using System;
public class Animal
{
    public float Weight;
    public string Eat() {
        return "Eat";
    }
}
public class Dog : Animal
{
    new public string Eat()
    {
        return "Eat!!!!!";
    }

    public void Write()
    {
        Console.WriteLine(base.Eat());
        Console.WriteLine(Eat());
    }
}
class Program
{
    static void Main()
    {

        Dog dog = new Dog();
        dog.Write();
    }
};
```

## 类型转换

可以把一个对象转换成另一种类型。
但是，只能把一个子类的实例转换为它的父类。

```cs
Dog dog = new Dog();
Animal animal = dog;
```

只有父类引用已经指向了一个子类的实例时，才允许向下转换到子类。

```cs
Dog dog2 = (Dog) animal;
```

## 密封类

可以在类的声明中使用关键字 `sealed`，阻止它派生其他的类。

```cs
public sealed class Animal
```

## 关键字 is

使用关键字 `is` 判断一个对象是否为一种特定类型。

```cs
Console.WriteLine(dog is Dog); // True
Console.WriteLine(dog is Animal); // True
```
