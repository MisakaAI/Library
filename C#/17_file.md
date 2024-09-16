# 输入输出

`System.IO` 命名空间提供了用于文件和流操作的类，可以读取和写入文本或二进制文件。

## 文件和目录

`File` 和 `Directory` 都是静态的，而 `FileInfo` 和 `DirectoryInfo` 都是面向对象的，支持实例化对象后，对对象进行多次操作。

特性|DirectoryInfo/FileInfo|Directory/File
-|-|-
面向对象|是|否
适合场景|多次操作同一文件或目录|简单的一次性操作
资源开销|需要实例化，适合多次使用|静态方法，简单任务时开销小
元数据获取|可以轻松获取文件/目录详细信息|无法直接获取，需要额外逻辑
代码简洁性|对于复杂操作更清晰|简单操作更简洁
性能|次操作更高效|一次性操作更高效

当你需要对同一个文件或目录执行多次操作，或者需要获取文件、目录的元数据时，`DirectoryInfo` 和 `FileInfo` 是更合适的选择。
如果你只需要对目录或文件执行一次性操作，且不需要保存或重复使用路径信息，`Directory` 和 `File` 类的静态方法会更加简洁易用。

- `File` 类用于对文件进行操作。
  - `Create(string path)`
  在指定路径创建一个新的文件，如果文件已经存在，则覆盖它，返回一个 `FileStream` 对象。
  - `Delete(string path)`
  删除指定路径的文件。
  - `Exists(string path)`
  检查指定路径的文件是否存在。
  - `Copy(string sourceFileName, string destFileName, bool overwrite)`
  将文件从一个位置复制到另一个位置，`overwrite` 为 `true` 时，如果目标文件已存在则覆盖。
  - `Move(string sourceFileName, string destFileName)`
  将文件从一个位置移动到另一个位置。
  - `ReadAllText(string path)`
  读取文件的全部内容并返回为字符串。
  - `WriteAllText(string path, string contents)`
  将指定的字符串写入到文件中（覆盖文件的内容）。
  - `ReadAllLines(string path)`
  读取文件的所有行，并返回字符串数组，每一行是数组的一个元素。
  - `WriteAllLines(string path, string[] contents)`
  将字符串数组中的所有行写入文件（覆盖文件的内容）。
  - `OpenRead(string path)`
  以只读方式打开指定文件，返回一个 `FileStream` 对象，用于读取文件内容。
  - `OpenWrite(string path)`
  以写入模式打开指定文件，返回一个 `FileStream`对象，用于写入文件内容。
  - `GetCreationTime(string path)`
  获取指定文件的创建时间。
  - `GetLastWriteTime(string path)`
  获取文件的最后修改时间。
- `Directory` 类用于对目录进行操作。
  - `CreateDirectory(string path)`
  在指定路径创建一个新的目录。如果目录已经存在，则不会抛出异常。
  - `Delete(string path, bool recursive)`
  删除指定路径的目录。`recursive` 参数为 `true` 时，递归删除该目录及其所有子目录和文件。
  - `Exists(string path)`
  检查指定路径的目录是否存在。
  - `GetFiles(string path)`
  获取指定目录下的所有文件的完整路径，返回一个字符串数组。
  - `GetDirectories(string path)`
  获取指定目录下的所有子目录的路径，返回一个字符串数组。
  - `GetCurrentDirectory()`
  获取当前工作目录的路径。
  - `Move(string sourceDirName, string destDirName)`
  将指定目录及其内容移动到新位置。
  - `GetCreationTime(string path)`
  获取指定目录的创建时间。
  - `GetParent(string path)`
  获取指定目录的父目录。
- `FileInfo`：用于管理和操作文件的类。
  - `Create()`
  创建一个文件并返回文件流。
  - `CopyTo(string destFileName)`
  复制文件到指定路径。
  - `MoveTo(string destFileName)`
  将文件移动到新位置。
  - `Delete()`
  删除文件。
  - `Exists`
  检查文件是否存在。
  - `Length`
  获取文件大小（字节）。
  - `Name`
  获取文件的名称。
  - `FullName`
  获取文件的完整路径。
  - `DirectoryName`
  获取文件所在的目录的名称。
  - `Extension`
  获取文件扩展名。
  - `CreationTime`
  获取或设置文件的创建时间。
  - `LastAccessTime`
  获取或设置文件的最后访问时间。
- `DirectoryInfo`：用于管理和操作目录的类。
  - `Create()`
  创建目录。
  - `Delete(bool recursive)`
  删除目录。recursive 参数为 true 时，递归删除目录及其内容。
  - `Exists`
  检查目录是否存在。
  - `GetFiles()`
  获取目录下的所有文件，返回 FileInfo[]。
  - `GetDirectories()`
  获取目录下的所有子目录，返回 DirectoryInfo[]。
  - `MoveTo(string destDirName)`
  移动目录到新位置。
  - `Name`
  获取目录的名称。
  - `FullName`
  获取目录的完整路径。
  - `Parent`
  获取父目录。
  - `CreationTime`
  获取或设置目录的创建时间。
  - `LastAccessTime`
  获取或设置目录的最后访问时间。

### 创建文件

```cs
using System;
using System.IO;
class Program
{
    static void Main()
    {
        string filePath = @"D:\test\test.txt";
        try
        {
            FileStream fs = File.Create(filePath);
        }
        catch (IOException e)
        {
            Console.WriteLine(e.Message);
        }
        finally
        {
        }
    }
}
```

`using` 语句会在代码块执行完毕后自动调用对象的 `Dispose` 方法。
对于文件操作，这意味着文件流会被正确关闭，文件句柄会被释放。
如果在打开或写入文件时发生异常，`using` 会确保文件流仍然被正确关闭。
如果创建失败，会抛出异常，因此建议将 `using` 放在 `try` 语句中。

```cs
using System;
using System.IO;
class Program
{
    static void Main()
    {
        string filePath = @"D:\test\test.txt";
        try
        {
            using (FileStream fs = File.Create(filePath))
            {
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
    }
}
```

### 删除文件

```cs
File.Delete(filePath);
```

### 创建目录

```cs
string directoryPath = @"D:\test";
if (!Directory.Exists(directoryPath))
{
    Directory.CreateDirectory(directoryPath);
    Console.WriteLine("目录已创建: " + directoryPath);
}
else
{
    Console.WriteLine("目录已存在: " + directoryPath);
}
```

### 删除目录

```cs
if (Directory.Exists(directoryPath))
{
    try
    {
    Directory.Delete(directoryPath);  // 只能删除空目录
    Directory.Delete(directoryPath, true);  // true 表示递归删除目录及其中的所有文件和子目录
    Console.WriteLine("目录已删除: " + directoryPath);
    }
    catch (Exception e)
    {
        Console.WriteLine("目录删除失败: " + directoryPath);
        Console.WriteLine(e);
    }
}
else
{
    Console.WriteLine("目录不存在");
}
```

### 文件和目录属性

```cs
string path = @"D:\test\test.txt";
FileInfo fileInfo = new FileInfo(path);
Console.WriteLine(fileInfo.Length); // 字节 0
Console.WriteLine(fileInfo.Extension); // 扩展名 .txt

string dir_path = @"D:\test";
DirectoryInfo dirInfo = new DirectoryInfo(dir_path);
Console.WriteLine(dirInfo.Exists); // 是否存在 True
Console.WriteLine(dirInfo.Name); // 名称 test
Console.WriteLine(dirInfo.FullName); // 完整路径 D:\test
Console.WriteLine(dirInfo.Parent); // 父目录 D:\
```

### 列出目录下文件

```cs
// 目录下文件
FileInfo[] files = dirInfo.GetFiles();
Console.WriteLine("目录中的文件:");
foreach (var file in files)
{
    Console.WriteLine(file.Name);
}
// 目录下子目录
DirectoryInfo[] dirs = dirInfo.GetDirectories();
Console.WriteLine("目录中的子目录:");
foreach (var dir in dirs)
{
    Console.WriteLine(dir.Name);
}
```

### 复制和移动文件

```cs
/* 复制文件 */
string sourceFile = @"C:\SourceDirectory\example.txt";
string destinationFile = @"C:\DestinationDirectory\example_copy.txt";
// File
File.Copy(sourceFile, destinationFile, true);
// FileInfo
FileInfo fileInfo = new FileInfo(sourceFile);
fileInfo.CopyTo(destinationFile, true); // true 允许覆盖

/* 移动文件 */
// File
File.Move(sourceFile, destinationFile);
// FileInfo
fileInfo.MoveTo(destinationFile, true); // true 允许覆盖
// DirectoryInfo
string sourceDir = @"C:\SourceDirectory";
string destinationDir = @"C:\DestinationDirectory\SourceDirectory";
DirectoryInfo dirInfo = new DirectoryInfo(sourceDir);
dirInfo.MoveTo(destinationDir);
```

## 输入输出流

- `FileStream` 用于从文件中读取或向文件写入字节流
- `StreamReader` `StreamWriter` 用于处理文本的流输入输出，支持字符级别的读取和写入。
- `BinaryReader` `BinaryWriter` 用于读取和写入二进制文件数据。
- `MemoryStream` 用于将数据存储在内存中的流。

同时也示范使用 `File` 类读写文本/二进制数据。

### 读取文本

- `StreamReader`
逐行读取，流式读取内容。内存占用较低，适合处理大文件。
- `File.ReadAllText` 与 `File.ReadAllLines`
一次性将文件的所有行读取到一个字符串或数组。内存占用较高，因为它一次性加载整个文件。

```cs
string path = @"D:\test\output.txt";
// 使用 StreamReader 逐行读取文件
using (StreamReader reader = new StreamReader(path))
{
    string line;
    while ((line = reader.ReadLine()) != null)
    {
        Console.WriteLine(line);
    }
}
// 使用 File.ReadAllText 读取文件
string text = File.ReadAllText(path); // 读取整个文件为一个字符串
Console.WriteLine(text);
// 使用 File.ReadAllLines 读取文件
string[] lines = File.ReadAllLines(path); // 逐行读取文件内容
foreach (var line in lines)
{
    Console.WriteLine(line);
}
```

### 写入文本

- `StreamWriter`
- `File.WriteAllText` `File.WriteAllLines`

```cs
string path = @"D:\test\output.txt";
string text = "Hello World.";
// 使用 StreamWriter 逐行写入文件
using (StreamWriter writer = new StreamWriter(path))
{
    writer.WriteLine(text);
}
// 使用 File.WriteAllText 写入文件
File.WriteAllText(path, text);
// 使用 `File.WriteAllLines` 写入文件
string[] lines = { "Hello", "World" };
File.WriteAllLines(path, lines);
```

### 读取二进制

- `File.ReadAllBytes`
- `BinaryReader`
- `FileStream`

```cs
string path = @"D:\test\binary.bin";
FileInfo fileInfo = new FileInfo(path);
long fileSize = fileInfo.Length; // fileInfo.Length 返回的类型是 long
int fize = (int)fileSize; // 5
// 使用 File.ReadAllBytes 读取整个文件为字节数组
byte[] bytes = File.ReadAllBytes(path);
foreach (byte b in bytes)
{
    Console.Write(b + " ");
}
// 使用 BinaryReader 读取二进制文件
using (BinaryReader reader = new BinaryReader(File.Open(path, FileMode.Open)))
{
    byte[] readData = reader.ReadBytes(fize); // BinaryReader.ReadBytes() 的参数必须是 int

    foreach (byte b in readData)
    {
        Console.Write(b + " ");
    }
}
// 使用 FileStream 读取文件 FileStream.Read()
// FileStream 提供了更细粒度的控制，可以读取或写入任意位置的文件。
byte[] buffer = new byte[fileSize];  // 定义缓冲区，用于存储读取到的数据

using (FileStream fs = new FileStream(path, FileMode.Open, FileAccess.Read))
{
    int bytesRead = fs.Read(buffer, 0, buffer.Length);  // 从文件中读取字节
    Console.WriteLine($"Read {bytesRead} bytes from file.");
}

foreach (byte b in buffer)
{
    Console.Write(b + " ");
}
```

### 写入二进制

- `File.WriteAllBytes`
- `BinaryWriter`
- `FileStream`

```cs
string path = @"D:\test\binary.bin";
byte[] data = { 1, 2, 3, 4, 5 };

// 使用 File.WriteAllBytes 可以将字节数组写入文件
File.WriteAllBytes(path, data);

// 使用 BinaryWriter 写入二进制文件
using (BinaryWriter writer = new BinaryWriter(File.Open(path, FileMode.Create)))
{
    writer.Write(data);
}

// 或使用 FileStream 写入文件 FileStream.Write()
// FileStream 提供了更细粒度的控制，可以读取或写入任意位置的文件。
using (FileStream fs = new FileStream(path, FileMode.OpenOrCreate))
{
    fs.Write(data, 0, data.Length);
    // 要写入文件的数据 data, 表示从 data 数组的哪个索引开始写入, 要写入的字节数量。
}
```

### MemoryStream

`MemoryStream` 用于在内存中操作数据而不写入物理文件，适合临时数据处理。

```cs
byte[] buffer;

// 写入 MemoryStream
using (MemoryStream ms = new MemoryStream())
{
    ms.Write(new byte[] { 1, 2, 3, 4 }, 0, 4);
    buffer = ms.ToArray();
}

// 从 MemoryStream 读取
using (MemoryStream ms = new MemoryStream(buffer))
{
    int b;
    while ((b = ms.ReadByte()) != -1)
    {
        Console.Write(b + " ");
    }
}
```
