# Android Studio

Android Studio 是基于 IntelliJ IDEA 的 IDE，用于 Android 开发。

1. 下载 [Android Studio](https://developer.android.com/?hl=zh-cn)
    - [国内特供](https://developer.android.google.cn/?hl=zh-cn)
2. 下载 [简体中文语言包](https://github.com/sollyu/AndroidStudioChineseLanguagePack/releases)
3. 设置代理 [阿里云镜像](https://developer.aliyun.com/mirror/android.googlesource.com) `https://mirrors.aliyun.com/android.googlesource.com/`
4. 设置 gradle 国内镜像 `gradle/wrapper/gradle-wrapper.properties`
`distributionUrl=https\://repo.huaweicloud.com/gradle/gradle-8.13-bin.zip`

## [在硬件设备上运行应用](https://developer.android.com/studio/run/device?hl=zh-cn)

- `ChromeOS`：无需其他配置。
- `macOS`：无需其他配置。
- `Windows`：为 adb 安装 USB 驱动程序（如适用）。
如需安装指南和用于获取 OEM 驱动程序的链接，请参阅安装 OEM USB 驱动程序。
- `Ubuntu Linux`：请进行以下设置：

希望使用 adb 的每个用户都需要位于 `plugdev` 群组中。
如果您看到一条错误消息，指出您不在 `plugdev` 群组内，请使用以下命令将自己添加到其中：

```sh
sudo usermod -aG plugdev $LOGNAME
```

群组仅在登录时更新，因此您必须退出才能使此更改生效。
当您重新登录后，可以使用 id 检查自己现在是否已在 `plugdev` 群组中。

需要为系统添加涵盖设备的 `udev` 规则。
`android-sdk-platform-tools-common` 软件包中包含一组适用于 Android 设备并由社区维护的默认 `udev` 规则。
若要安装此软件包，请使用以下命令：

```sh
apt-get install android-sdk-platform-tools-common
```
