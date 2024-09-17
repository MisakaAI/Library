# Windows Presentation Foundation

- [WPF](https://learn.microsoft.com/zh-cn/dotnet/desktop/wpf/overview/?view=netdesktop-8.0)

## VS Code

创建 WPF 项目

```powershell
dotnet new wpf -n HelloWorldWPF
```

编译并运行程序 `dotnet run`

### WPF 控件

按钮： `Button` 和 `RepeatButton`。
数据显示：`DataGrid`、`ListView` 和 `TreeView`。
日期显示和选项： `Calendar` 和 `DatePicker`。
对话框： `OpenFileDialog`、 `PrintDialog`和 `SaveFileDialog`。
数字墨迹： `InkCanvas` 和 `InkPresenter`。
文档： `DocumentViewer`、 `FlowDocumentPageViewer`、 `FlowDocumentReader`、 `FlowDocumentScrollViewer`和 `StickyNoteControl`。
输入： `TextBox`、 `RichTextBox`和 `PasswordBox`。
布局： `Border`、 `BulletDecorator`、 `Canvas`、 `DockPanel`、 `Expander`、 `Grid`、 `GridView`、 `GridSplitter`、 `GroupBox`、 `Panel`、 `ResizeGrip`、 `Separator`、 `ScrollBar`、 `ScrollViewer`、 `StackPanel`、 `Thumb`、 `Viewbox`、 `VirtualizingStackPanel`、 `Window` 和 `WrapPanel`。
媒体： `Image`、 `MediaElement`和 `SoundPlayerAction`。
菜单： `ContextMenu`、 `Menu`和 `ToolBar`。
导航： `Frame`、 `Hyperlink`、 `Page`、 `NavigationWindow`和 `TabControl`。
选项： `CheckBox`、 `ComboBox`、 `ListBox`、 `RadioButton`和 `Slider`。
用户信息： `AccessText`、 `Label`、 `Popup`、 `ProgressBar`、 `StatusBar`、 `TextBlock`和 `ToolTip`。

### 布局

- `Canvas`：子控件提供其自己的布局。
- `DockPanel`：子控件与面板的边缘对齐。
- `Grid`：子控件由行和列定位。
- `StackPanel`：子控件垂直或水平堆叠。
- `VirtualizingStackPanel`：子控件在水平或垂直的行上虚拟化并排列。
- `WrapPanel`：子控件按从左到右的顺序放置，在当前行上的空间不足时换行到下一行。

## 纯代码

在项目中，打开 `App.xaml.cs` 文件，删除 `App.xaml` 相关的代码，
并修改启动窗口的代码，使其从纯 C# 创建的窗口开始。

```cs
using System;
using System.Windows;

namespace HelloWorldWPF
{
    public partial class App : Application
    {
        [STAThread]
        public static void Main()
        {
            var app = new Application();
            var mainWindow = new MainWindow();
            app.Run(mainWindow);
        }
    }
}
```

删除 `MainWindow.xaml` 文件，这样我们可以完全通过 C# 代码来控制界面。
然后修改 `MainWindow.xaml.cs` 文件中的代码，手动创建和配置窗口及控件。

```cs
using System.Windows;
using System.Windows.Controls;

namespace HelloWorldWPF
{
    public class MainWindow : Window
    {
        public MainWindow()
        {
            // 设置窗口标题和大小
            this.Title = "Hello World";
            this.Width = 300;
            this.Height = 200;

            // 创建一个 TextBlock 控件，并设置文本内容
            TextBlock textBlock = new TextBlock();
            textBlock.Text = "Hello World";
            textBlock.FontSize = 24;
            textBlock.HorizontalAlignment = HorizontalAlignment.Center;
            textBlock.VerticalAlignment = VerticalAlignment.Center;

            // 将 TextBlock 添加到窗口的内容中
            this.Content = textBlock;
        }
    }
}
```

## XAML

XAML 是一种声明性标记语言。
应用于 .NET 编程模型时，XAML 可简化为 .NET 应用创建 UI 的过程。

以文本表示时，XAML 文件是通常具有 `.xaml` 扩展名的 XML 文件。
可通过任何 XML 编码对文件进行编码，但通常以 UTF-8 编码。

```xml
<Window x:Class="HelloWorldWPF.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:HelloWorldWPF"
        mc:Ignorable="d"
        Title="MainWindow"
        Height="450"
        Width="800">
    <Grid>
        <TextBlock Text="Hello World"
                   HorizontalAlignment="Center"
                   VerticalAlignment="Center"
                   FontSize="24"/>
    </Grid>
</Window>
```

## 其他

### 嵌入字体

1. 将字体文件（例如 `975MaruSC-Bold.ttf`）放入项目目录中的一个文件夹（例如 `Fonts` 文件夹）

2. 打开项目的 `.csproj` 文件，在 `ItemGroup` 中添加如下代码，将字体文件设置为嵌入式资源：

```cs
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
  ...
  </PropertyGroup>
  <ItemGroup>
    <Resource Include="Fonts\975MaruSC-Bold.ttf" />
  </ItemGroup>
</Project>
```

3. 动态加载嵌入的字体

```cs
// 纯代码
inputTextBox.FontFamily = new FontFamily(new Uri("pack://application:,,,/"), "./Fonts/#975MaruSC-Bold");
inputTextBox.FontSize = 16;

pack://application:,,,/./Fonts/#975MaruSC-Bold
```

```xml
<!-- XAML -->
<Grid>
    <TextBlock Text="Hello World"
               HorizontalAlignment="Center"
               VerticalAlignment="Center"
               FontFamily="./Fonts/#975Maru SC Bold"
               FontSize="64"/>
</Grid>
```

## 打包发布

```cs
dotnet publish -c Release -r win-x64 --self-contained
```

- `-c Release`：指定发布为 `Release` 版本（优化后的编译版本）。
- `-r win-x64`：指定目标平台为 Windows 64 位（可以根据需要使用 `win-x86` 生成 32 位应用程序）。
- `--self-contained`：生成独立的 `.exe` 文件，该文件包含所有依赖项（包括 .NET 运行时），用户不需要安装 .NET 来运行应用程序。

### 发布的 .exe 文件

路径 `<项目目录>/bin/Release/net8.0-windows/win-x64/publish/`
