# 错误处理

## 捕获异常

`try` 语句通常与 `catch` 和 `finally` 语句一起使用。
`catch` 和 `finally` 是可选的，但是二者至少要选择其中一个。
一个 `try` 语句块，可以有一个或多个 `catch` 语句。
 `finally` 语句在最后执行，通常用于关闭对资源的访问。

```cs
try
{
    int[] numbers = { 1, 2, 3 };
    Console.WriteLine(numbers[10]); // 抛出异常
}
catch (IndexOutOfRangeException e)
{
    Console.WriteLine($"{e.Message}");
}
catch (Exception e)
{
    Console.WriteLine($"{e.Message}");
}
finally
{
    Console.WriteLine("finally");
}
```

### 主动抛出异常

`throw` 关键字可以显式地抛出异常。

```cs
if (value < 0)
{
    throw new ArgumentOutOfRangeException("value", "Value cannot be negative.");
}
```

## 自定义异常

所有的`.NET`异常类，都继承自 `System.Exception` 基类。

```cs
public class MyCustomException : Exception
{
    public MyCustomException(string message) : base(message)
    {
    }
}

try
{
    throw new MyCustomException("This is a custom exception.");
}
catch (MyCustomException ex)
{
    Console.WriteLine(ex.Message);
}
```

## 注意事项

`try` 语句会牺牲一些性能，因此不要过度使用 `try` 语句。
