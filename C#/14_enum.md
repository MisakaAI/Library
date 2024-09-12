# 枚举

枚举（enum）是一种值类型，它允许你为一组相关的常量定义一个命名集合。

## 枚举的用途

- 提高代码的可读性和可维护性：枚举使代码更易读，不必记住一组相关的常量。
- 定义一组固定的常量：比如定义一个状态、方向、星期等。
- 类型安全：与整型或字符串不同，枚举限制了取值范围，有助于防止无效的值被使用。

## 定义枚举

默认情况下，枚举中的每个成员都从0开始递增。

```cs
enum Days
{
    Sunday,    // 默认值为 0
    Monday,    // 默认值为 1
    Tuesday,   // 默认值为 2
    Wednesday, // 默认值为 3
    Thursday,  // 默认值为 4
    Friday,    // 默认值为 5
    Saturday   // 默认值为 6
}

Days D1 = Days.Monday; // Monday
Days D2 = (Days)2; // Tuesday
int D3 = (int)Days.Wednesday; // 3
```

也可以在定义枚举时手动指定枚举成员的值。

```cs
enum Status
{
    Ready = 1,
    Running = 5,
    Completed = 10,
    Failed = -1
}

Status S1 = Status.Running; // Running
Status S2 = (Status)2; // 2
int S3 = (int)Status.Failed; // -1
```

### 类中的枚举

可以将枚举用于类中。

```cs
class Week
{
    public enum Days
    {
        Sunday,
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday,
    }
}

Week.Days D1 = Week.Days.Monday;
```

## Switch 语句中的枚举

```cs
enum Days
{
    Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
}

Days day = Days.Sunday;

switch (day)
{
    case Days.Monday:
    case Days.Tuesday:
    case Days.Wednesday:
    case Days.Thursday:
    case Days.Friday:
        Console.WriteLine("Week day");
        break;
    case Days.Saturday:
    case Days.Sunday:
        Console.WriteLine("Week end");
        break;
}
```

## 枚举的位标志

当枚举用于标识一组可以组合的选项时，你可以使用`Flags`属性。

```cs
[Flags]
enum FileAccess
{
    Read    = 1,
    Write   = 2,
    Execute = 4
}

FileAccess access = FileAccess.Read | FileAccess.Write; // Read, Write
Console.WriteLine((int)access); // 3
```
