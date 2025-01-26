# Scrcpy

安卓手机投屏电脑

- [Scrcpy](https://github.com/Genymobile/scrcpy)
- [README zh‐CN](https://github.com/Genymobile/scrcpy/wiki/README.zh‐CN)
- [FAQ](https://github.com/Genymobile/scrcpy/wiki/FAQ.zh‐CN)

## 快捷键

功能|快捷键
-|-
全屏|Alt+F
将窗口大小重置为1:1 (匹配像素)|Alt+G
点按 主屏幕|Alt+H/中键
点按 返回|Alt+B/右键
点按 切换应用|Alt+S
点按 电源键|Alt+P
打开屏幕|鼠标右键
复制到剪贴板|Alt+C
剪切到剪贴板|Alt+X
同步剪贴板并粘贴|Alt+V

## 其他功能

### 屏幕录制

```bash
scrcpy --record=file.mp4
scrcpy -r file.mkv
```

### 无线连接

[Windows7 安卓驱动 下载](https://www.thecustomdroid.com/google-android-usb-drivers/)
[ADB](https://developer.android.google.cn/tools/releases/platform-tools?hl=zh-cn)

``` bash
# 查看设备
adb devices -l
# 发出 shell 命令
adb shell
# 查看设备分辨率
wm size
# 查看设备dpi
wm density

# 查看IP
adb shell ip route
# 启用设备的网络 adb 功能
adb tcpip 5555
# 连接到您的设备
adb connect DEVICE_IP:5555
# 打开scrcpy
scrcpy --tcpip=DEVICE_IP
```

### 保持常亮

```bash
scrcpy --stay-awake
scrcpy -w
```

### 关闭设备屏幕

```bash
scrcpy --turn-screen-off
scrcpy -S
```

### 查看设备UA

[UA检测](https://useragent.buyaocha.com/)
