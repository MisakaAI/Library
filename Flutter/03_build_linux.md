# Linux 开发

配置您的开发环境以运行、构建和部署用于 Linux 桌面的 Flutter 应用。

## 配置

```sh
# 安装依赖
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y clang cmake ninja-build pkg-config libgtk-3-dev libstdc++-12-dev

# 检查工具链问题
flutter doctor -v

# 检查Linux设备
flutter devices
```

## 构建

可执行的二进制文件可以在您的项目中的 `build/linux/x64/<build mode>/bundle/` 下找到。除了在bundle目录中的可执行二进制文件，您可以找到两个目录：

- `lib` 包含所需的.so库文件
- `data` 包含应用程序的数据资产，如字体或图像

除了这些文件之外，应用程序还依赖于各种操作系统库，它是根据这些库编译的。
要查看库的完整列表，请在应用程序的目录上使用 `ldd` 命令。

```sh
# 假设有一个名为 linux_desktop_test 的 Flutter 桌面应用程序
flutter build linux --release
ldd build/linux/x64/release/bundle/linux_desktop_test
```

要打包此应用程序以供分发，请将所有内容包含在bundle目录中，并验证目标Linux系统是否具有所有必需的系统库。

```sh
sudo apt-get install libgtk-3-0 libblkid1 liblzma5
```

## 参考文献

- [使用Flutter构建Linux应用程序](https://docs.flutter.dev/platform-integration/linux/building)
- [构建并将Linux应用程序发布到Snap Store](https://docs.flutter.dev/deployment/linux)
- [Linux打包指南](https://medium.com/@fluttergems/packaging-and-distributing-flutter-desktop-apps-the-missing-guide-part-3-linux-24ef8d30a5b4)
