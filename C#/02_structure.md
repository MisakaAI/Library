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
