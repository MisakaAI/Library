# Android 开发

## Android Studio

需要先安装 [Android Studio](../Android/01_Install.md)

### 清华大学镜像站

在编译 Android 项目时，Flutter 还会从 `https://storage.googleapis.com/download.flutter.io` 下载 Java 程序库。
在 Android 项目目录下的 `build.gradle` 中添加下面一行下载源，从而使用镜像源。

```build.gradle
allprojects {
    repositories {
        google()
        jcenter()
        maven { url 'https://mirrors.tuna.tsinghua.edu.cn/flutter/download.flutter.io' }
    }
}
```

### 安装需要的 SDK

通过 Android Studio 的 SDK 管理器安装。

1. 菜单栏 `Tools`
2. 选择 `SDK Manager`
3. 标签页 `SDK Tools`
4. 选择
    - `Android SDK Build-Tools`
    - `Android SDK Command-line Tools (latest)`
    - `Android Emulator`
    - `Android SDK Platform-Tools`
5. 确认 `Apply` / `OK`

### 同意 Android 许可证

```sh
flutter doctor --android-licenses
```

一路输入 `y` 并按回车键，直到所有许可证都接受完毕。

### 验证 Flutter 是否识别连接的设备

```sh
# Android 模拟器
flutter emulators

# 物理 Android 设备
flutter devices
```

## 编译

```sh
export ANDROID_SDK_MANAGER_OPTS="-Dhttp.proxyHost=mirrors.aliyun.com"
flutter build apk --split-per-abi
```

会生成三个文件

- `app-armeabi-v7a-release.apk` ARM 32 位
- `app-arm64-v8a-release.apk` ARM 64 位
- `app-x86_64-release.apk` X86_64 位

## 参考文献

- [设置Android开发](https://docs.flutter.dev/platform-integration/android/setup)
