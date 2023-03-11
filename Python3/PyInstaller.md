# PyInstaller

- [PyInstaller](https://pyinstaller.org/)
- [Using PyInstaller](https://pyinstaller.org/en/v5.8.0/usage.html)

## Installation

```bash
pip install pyinstaller
```

## Usage

```bash
pyinstaller.exe -F -i favicon.ico test.py
```

--distpath DIR
Where to put the bundled app (default: ./dist)
生成应用程序放置的位置（默认：./dist）

--workpath WORKPATH
Where to put all the temporary work files, .log, .pyz and etc. (default: ./build)
在哪里放置所有临时工作文件，.log，.pyz 等（默认值：./build）

-y, --noconfirm
Replace output directory (default: SPECPATH/dist/SPECNAME) without asking for confirmation
替换输出目录（默认： SPECPATH/dist/SPECNAME），而不要求 确认

-a, --ascii
Do not include unicode encoding support (default: included if available)
不包括unicode编码支持（默认值： 包括在内，如果有）

--clean
Clean PyInstaller cache and remove temporary files before building.
清理PyInstaller缓存并删除临时文件 在建造之前。

-D, --onedir
Create a one-folder bundle containing an executable (default)
创建包含可执行文件的单文件夹捆绑包（默认值）

-F, --onefile
Create a one-file bundled executable.
创建一个可执行文件。

--specpath DIR
Folder to store the generated spec file (default: current directory)
用于存储生成的等级库文件的文件夹（默认值： 当前目录）

-n NAME, --name NAME
Name to assign to the bundled app and spec file (default: first script’s basename)
要分配给生成的应用程序和文件的名称 （默认：第一个脚本的名称）

-c, --console, --nowindowed
Open a console window for standard i/o (default). On Windows this option has no effect if the first script is a ‘.pyw’ file.
打开标准I/O的控制台窗口（默认）。在Windows上，此选项 如果第一个脚本是.“pyw”文件，则无效。

-w, --windowed, --noconsole
Windows and Mac OS X: do not provide a console window for standard i/o.
On Mac OS this also triggers building a Mac OS .app bundle.
On Windows this option is automatically set if the first script is a ‘.pyw’ file.
This option is ignored on *NIX systems.
不提供标准I/O的控制台窗口。
开启 Mac OS这也会触发构建Mac OS .app包。
在Windows上，此 如果第一个脚本是.“pyw”文件，则会自动设置选项。
这个选项在 \*NIX系统上被忽略。

-i <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">, --icon <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">
FILE.ico: apply the icon to a Windows executable.
FILE.exe,ID: extract the icon with ID from an exe.
FILE.icns: apply the icon to the .app bundle on Mac OS.
If an image file is entered that isn’t in the platform format (ico on Windows, icns on Mac),
PyInstaller tries to use Pillow to translate the icon into the correct format (if Pillow is installed).
Use “NONE” to not apply any icon, thereby making the OS show some default (default: apply PyInstaller’s icon).
This option can be used multiple times.
将图标应用于Windows可执行文件。
文件.exe，ID：提取 带有exe ID的图标。
FILE.icns：将图标应用于上的.app包
如果输入的图像文件不是平台格式（ico Windows上的icns，Mac上的icns），PyInstaller尝试使用Pillow来翻译图标转换为正确的格式（如果安装了Pillow）。
使用“NONE”表示不 应用任何图标，从而使操作系统显示某些默认值（默认值：应用 PyInstaller的图标）。
此选项可以多次使用。
