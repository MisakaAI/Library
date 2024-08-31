# 字符串

## System.String

`System.String` 表示一个字符串。
也可以使用关键字 `string`
字符串的开始和结束都是用双引号`"`
前缀`@`可以使字符串不进行转义。`@"\\"`
使用`+`可以拼接字符串。

String类的属性 `Length` 和 `Chars`

```cs
// 声明字符串的两种方式
System.String hello = "Hello";
string hello = "Hello";

// Length 返回当前 String 对象的字符数
int len = hello.Length;

// Chars 返回指定索引位置的 Char 对象
char i = hello[0];
```

String类提供了操作String的值的方法。

```cs
// 拼接字符串
string hello = String.Concat("Hello",' ',"World"); // "Hello World"

// 判断字符串内是否包含传入的值
bool s = hello.Contains("Hello"); // True

// 字符串是否以特定后缀结尾
bool s = hello.EndsWith("World"); // True

// 字符串是否以指定的前缀开始
bool s = hello.StartsWith("Hello"); // True

// 返回指定子字符串第一次出现的索引
// 没有发现匹配，则返回-1
int s = hello.IndexOf("o"); // 4

// 返回指定子字符串最后一次出现的索引
// 没有发现匹配，则返回-1
int s = hello.LastIndexOf("o"); // 7

// 返回指定子字符串的索引，从指定索引位置开始
int s = hello.IndexOf("o", 5); // 7
int s = hello.LastIndexOf("o", 5); // 4

// 返回当前字符串的一个子字符串，从指定的索引位置开始
string s = hello.Substring(6); // "World"
string s = hello.Substring(6,3); // "Wor"

// 字符串替换
string s = hello.Replace("o","O"); // "HellO WOrld"

// 按关键字拆分成数组
string[] s = hello.Split(" "); // { "Hello", "World" }
for (int i = 0; i<s.Length;  i++) {
    Console.WriteLine(s[i]);
}

// 拆分成字符数组
char[] s = hello.ToCharArray(); // { 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd' }
for (int i = 0; i<s.Length;  i++) {
    Console.WriteLine(s[i]);
}

// 字符串全部字符转化为小写
string s = hello.ToLower(); // "hello world"

// 字符串全部字符转化为大写
string s = hello.ToUpper(); // "HELLO WORLD"

// 去除开头和结尾的空格，并返回一个新字符串。
string s = " Hello World  ".Trim(); // "Hello World"

// 字符串插值
int age = 18;
string message = $"I am {age} years old."; // "I am 18 years old."
```

## System.Text.StringBuilder

### StringBuilder 构造函数

`String` 对象是不可改变的，如果需要增加或插入字符，就会产生新的对象。
为了避免多余的性能消耗，最好使用 `System.Text.StringBuilder` 类

- `StringBuilder()`
默认容纳 16 个字符
- `StringBuilder(int capacity)`
默认容纳 `capacity` 个字符
- `StringBuilder(int capacity, int maxCapacity)`
默认容纳 `capacity` 个字符，最大容纳 `maxCapacity`
字符超过 `maxCapacity` 个时，会抛出异常。
- `StringBuilder(string value)`
预先存放字符串 `value`
- `StringBuilder(string value, int capacity)`
预先存放字符串 `value`，默认容纳 `capacity` 个字符
- `StringBuilder(string value, int startIndex, int length, int capacity)`
初始字符串 `value`，起始位置 `startIndex` ，截取的长度 `length`，初始容量 `capacity`

```cs
using System.Text;
StringBuilder sb1 = new StringBuilder();
sb1.Append('H');
StringBuilder sb2 = new StringBuilder(2);
sb1.Append('e');
sb1.Append('l');
StringBuilder sb3 = new StringBuilder(1,2);
sb1.Append('l');
sb1.Append('o');
sb1.Append(' ');
StringBuilder sb4 = new StringBuilder("World");
string sb4s = sb4.ToString();
StringBuilder sb5 = new StringBuilder("Wor",3);
StringBuilder sb6 = new StringBuilder(sb4s,3,2,2);
Console.WriteLine(sb1.ToString() + sb2.ToString() + sb3.ToString() + sb5.ToString() + sb6.ToString());
```

### StringBuilder 属性

- `Capacity` 容量
- `Charts` 索引位置
- `Length` 长度
- `MaxCapacity` 最大容量值，默认值 2147483647

```cs
using System.Text;
StringBuilder sb = new StringBuilder();
sb.Append("Hello World");
Console.WriteLine(sb.Capacity);
Console.WriteLine(sb.Length);
sb[5] = '?'; // Charts
Console.WriteLine(sb);
Console.WriteLine(sb.MaxCapacity);
```

### StringBuilder 方法

- `ToString()` 转换为字符串
- `Append(string value)` 在末尾增加字符 `value`
- `Insert(int index, string value)` 在指定位置 `index` 插入字符 `value`
- `Remove(int startindex, int length)` 删除字符串，从 `startindex` 开始删除 `length` 个字符

```cs
using System.Text;
StringBuilder sb = new StringBuilder();
sb.Append("Hello World");
sb.Insert(5, '!');
sb.Remove(5, 2);
Console.WriteLine(sb.ToString());
```
