# 环境搭建

## 安装 .NET SDK

下载 [.NET](https://dotnet.microsoft.com/zh-cn/download)

## Visual Studio Code

下载 [Visual Studio Code](https://code.visualstudio.com/Download)

### 适用于 Visual Studio Code 的 C# 扩展

[C#](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)
[C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)

## 创建 C# 项目

1. VS Code 中 `Ctrl + Shift + P` 打开命令面板（Command Palette）
选择 `.NET：New Project`

2. 或者直接在命令行中运行 `dotnet new console -n HelloWorldApp`
-n 后面接项目名称。

## 编译程序

`dotnet build`

运行这个命令后，.NET CLI 会编译项目并生成输出文件，但不会执行程序。

## 编译并运行程序

`dotnet run`

这个命令会先检查项目是否已经编译。
如果没有，它会先编译项目，然后立即运行生成的可执行文件。

## 入口文件

C#程序的入口文件默认为 `Program.cs`
