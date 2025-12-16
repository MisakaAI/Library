# 创建 Flutter 项目

## Terminal

1. 配置项目创建 `flutter create --empty my_app`
2. 等待项目初始化

## VS Code

1. 打开命令选项板 `Ctrl`+`Shift`+`P`
2. 运行新建项目命令 `Flutter: New Project`
3. 选择一个模板
4. 选择项目位置
5. 输入项目名称
6. 等待项目初始化

## CLI

使用 `flutter` 工具创建、分析、测试和运行应用程序：

```sh
# 创建新项目
flutter create <DIRECTORY>

# 显示有关已安装工具的信息
flutter doctor

# 分析项目的 Dart 源代码
flutter analyze

# 在这个包里测试
flutter test [<DIRECTORYDART_FILE>]

# 为 Flutter 项目生成本地化
flutter gen-l10n <DIRECTORY>

# 运行
flutter run <DART_FILE>

# 列出，启动和创建模拟器
flutter emulators

# 列出所有连接的设备
flutter devices -d <DEVICE_ID>

# 构建
flutter build <DIRECTORY>

# 在连接的设备上安装 Flutter 应用程序
flutter install -d <DEVICE_ID>

# 从连接的设备上截取 Flutter 应用的屏幕截图
flutter screenshot

# 升级 Flutter
flutter upgrade

# 使用 pub 工具运行 Flutter 命令
flutter pub get
flutter pub outdated
flutter pub upgrade

# 获取帮助
flutter --help --verbose

# 获取 Flutter SDK 的当前版本，包括其框架、引擎和工具
flutter --version
```
