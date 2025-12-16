# 安装和环境配置

## 在中国网络环境下使用 Flutter

```sh
export PUB_HOSTED_URL="https://mirrors.tuna.tsinghua.edu.cn/dart-pub"
export FLUTTER_STORAGE_BASE_URL="https://mirrors.tuna.tsinghua.edu.cn/flutter"

echo 'export PUB_HOSTED_URL="https://mirrors.tuna.tsinghua.edu.cn/dart-pub"' >> ~/.zshrc
echo 'export FLUTTER_STORAGE_BASE_URL="https://mirrors.tuna.tsinghua.edu.cn/flutter"' >> ~/.zshrc
```

## 更新软件源 && 安装依赖

```sh
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y curl git unzip xz-utils zip libglu1-mesa
```

## 从镜像站下载 Flutter SDK 安装包

[https://mirrors.tuna.tsinghua.edu.cn/flutter/flutter_infra/releases/stable/](https://mirrors.tuna.tsinghua.edu.cn/flutter/flutter_infra/releases/stable/)

```sh
cd ~/Downloads

# wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.38.5-stable.tar.xz
wget https://mirrors.tuna.tsinghua.edu.cn/flutter/flutter_infra/releases/stable/linux/flutter_linux_3.38.5-stable.tar.xz

mkdir ~/develop/
tar -xf ~/Downloads/flutter_linux_3.29.3-stable.tar.xz -C ~/develop/
```

## Flutter SDK

Flutter SDK 默认从 Github 获取更新，如您访问 Github 速度慢，可以在 Flutter 目录下运行命令：

```sh
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/flutter-sdk.git
```

将上游设置为镜像站。
或者通过下面的命令，直接从 Master 构建渠道检出 Flutter 的 SDK：

```sh
git clone -b master https://mirrors.tuna.tsinghua.edu.cn/git/flutter-sdk.git
./flutter-sdk/bin/flutter --version
```

您也可以替换上述代码中 git clone -b 之后的 master 为 beta 获取 Beta 渠道的构建、替换为 dev 获取 Dev 渠道的构建。

### 添加 Flutter 到系统环境

```sh
echo 'export PATH="<path-to-sdk>/bin:$PATH"' >> ~/.zshenv
```

验证安装

```sh
flutter --version
dart --version
```

## 添加 VS Code 的 Flutter 扩展

通过 VS Code 的快速打开 (Ctrl+P) 执行命令 `ext install Dart-Code.flutter` 添加扩展

- [Flutter]( https://marketplace.visualstudio.com/items?itemName=Dart-Code.flutter)

通过 VS Code 的命令面板 (Ctrl+Shift+P) 执行命令 `Flutter: New Project`

为了确保正确安装Flutter，请在首选终端中运行 `flutter doctor -v` 。

## 参考文献

- [Set up and test drive Flutter](https://docs.flutter.dev/get-started/quick)
- [快速开始](https://docs.flutter.cn/get-started/quick/)
- [Tuna Flutter 软件仓库](https://mirrors.tuna.tsinghua.edu.cn/help/flutter/)
