// 导入 System 命名空间
using System

// 输出内容并换行
Console.WriteLine("Hello World!");

// 输出内容但不换行
Console.Write("Hello World!\n");

// 蜂鸣器
Console.Beep();

// 清除控制台缓存和控制台窗口
Console.Clear();

// 返回输入流的下一行字符
string name = Console.ReadLine();

// 读取单个字符输入，并且显示在控制台上
ConsoleKeyInfo keyInfo = Console.ReadKey();

// 读取单个字符输入，并且不显示在控制台上
ConsoleKeyInfo keyInfo = Console.ReadKey(true);

// 输出用户按下的键
Console.WriteLine(keyInfo.KeyChar);

// 检查是否按下了 Enter 键
if (keyInfo.Key == ConsoleKey.Enter) {
    Console.WriteLine("You pressed Enter!");
}

// 睡眠 500s
System.Threading.Thread.Sleep(500);
