# 对象

## 面向对象编程

面向对象编程（Object-Oriented Programming，简称 OOP）是一种程序设计范式，它将程序结构化为一组相互作用的对象。
对象是类的实例，类是定义对象行为和属性的模板。
OOP 通过封装（Encapsulation）、继承（Inheritance）、多态（Polymorphism）和抽象（Abstraction）等特性，使代码更具可维护性、可扩展性和可重用性。

面向对象编程特点：封装、继承、多态
非面向对象编程特点：数据和函数分离、无继承和多态、不易扩展

### 主要概念

- 类（Class）：类是定义对象的蓝图或模板，包含了对象的属性和行为。属性通常对应对象的数据，行为通常对应对象的方法。
- 对象（Object）：对象是类的实例，具有类所定义的属性和行为。每个对象都有自己独立的状态（属性值），但共享类的行为（方法）。
- 封装（Encapsulation）：将数据和操作数据的方法封装在对象内部，控制对数据的访问，避免外部直接修改对象的状态。
- 继承（Inheritance）：子类继承父类的属性和方法，允许代码复用和功能扩展。
- 多态（Polymorphism）：允许不同的对象在调用同一方法时表现出不同的行为。

### 比较

面向对象编程通过类和对象的方式，将数据和操作数据的方法封装在一起，使得程序更具可维护性、可扩展性和可重用性。
面向过程编程则更关注按步骤执行任务，数据和函数分离，适合较小规模的程序，但在处理复杂系统时，可能会导致代码难以维护和扩展。

## System.Object

`System.Object` 类表示了一个C#对象。
所有的类都是从这个类直接或者间接派生的。
