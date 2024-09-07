# 语句

## if 语句

```cs
int a = 0;

if (a==0) {
    int b = 0;
} else if (a==1) {
    int b = 1;
} else {
    int b = -1;
}
```

## while 语句

```cs
int i = 0;

while (i<10) {
    Console.WriteLine(i);
    i++;
}

while (true) {
    Console.WriteLine(i);
    i++;
    if (i>9) {
        break;
    }
}
```

## do-while 语句

```cs
int i = 0;
do {
    Console.WriteLine(i);
    i++;
} while (i<10);
```

## for 语句

初始值;布尔表达式;更新语句

```cs
for (int i=0; i<10; i++) {
    Console.WriteLine(i);
}
```

## break 语句

用于从封闭的 `do` `while` `for` 或 `switch` 语句中。
终止整个循环，跳出循环体。

## continue 语句

跳过当前迭代的剩余部分，进入下一次循环。

## switch 语句

控制结构，根据一个变量的值执行不同的代码块。

```cs
int i=0;
switch (i) {
    case 1:
        Console.WriteLine("一");
        goto label;
    case 2:
        Console.WriteLine("二");
        return;
    case 3:
        Console.WriteLine("三");
        break;
    default:
        Console.WriteLine("Default");
        break;
}

label:
    Console.WriteLine("Label");
```

## return 语句

退出终止一个方法的执行，并返回控制权给调用该方法的地方。

```cs
// 用于返回 void 类型的方法
return;
// 用于返回特定类型值的方法
return value;
```

## => 表达式体成员

```cs
// 完整写法
public string Name
{
    get
    {
        return _name;
    }
}

// 简写形式（表达式体成员）
public string Name
{
    get => _name;
}
```

## Lambda 表达式

Lambda 表达式的基本语法为 `(parameters) => expression`

- **左边**：包含参数列表（可以省略参数类型，如果参数是单一的也可以省略括号）。
- **右边**：包含表达式或代码块，该部分是 Lambda 表达式的主体。

```cs
// 没有参数
Action sayHello = () => Console.WriteLine("Hello!");
sayHello();  // 输出 "Hello!"

// 单个参数
Func<int, int> increment = x => x + 1;
Console.WriteLine(increment(1));  // 输出 2

// 多个参数
Func<int, int, int> add = (x, y) => x + y;
Console.WriteLine(add(3, 4));  // 输出 7

// 块体 Lambda 表达式
/* 如果 Lambda 表达式中有多行代码
可以使用大括号 {} 包含整个代码块
并且需要显式使用 return 返回值 */
Func<int, int, int> multiply = (x, y) =>
{
    int result = x * y;
    return result;
};
Console.WriteLine(multiply(3, 4));  // 输出 12
```

```cs
// 不使用 Lambda 表达式
// Func<int, int, int> add = (x, y) => x + y;
public static int Add(int x, int y)
{
    return x + y;
}

Func<int, int, int> add = Add;
Console.WriteLine(add(3, 4));  // 输出 7
```

## Func

`Func` 是一个泛型委托，用于表示有返回值的函数。

```cs
// 接受 两个 int 参数 并且返回 int 类型的结果。
Func<int, int, int>
```
