# NVIDIA Broadcast

NVIDIA Broadcast 可以利用 AI 的强大功能将标准网络摄像头和麦克风升级为高端智能设备，从而将任意空间转变为家庭工作室。
通过麦克风去噪、房间回声消除、虚拟背景、网络摄像头人像跟踪和视频降噪等 AI 功能，提高直播的视频和音频质量。
通过 NVIDIA RTX GPU 上搭载的名为 Tensor Core 的专用 AI 处理器，AI 网络能够实时运行高质量的效果。

## 设置

### 设置 NVIDIA Broadcast

1. 打开 NVIDIA Broadcast 应用。
2. 导航至每个设备并选择顶部的输入设备。
3. 选择您要应用的效果。
    1. 如果您愿意，可以组合使用多种效果。
    2. 我们建议您仅启用所需效果，以避免占用不必要的 GPU 资源。
4. 如果需要，您可以使用下方的滑块调整效果强度或设置。

### 查看 Windows 的“Sound Settings”（声音设置）

1. 前往“Windows Settings”（Windows 设置）> 系统 > 声音，确保已将耳麦或扬声器设置为输出设备。您不应将 NVIDIA Broadcast 扬声器保留为默认设置，因为您需要滤除所有系统声音。
2. 如果您愿意，可以选择 NVIDIA Broadcast 麦克风作为输入设备。这样，您就不需要在每个应用中对其进行配置。在这种情况下，请确保在 NVIDIA Broadcast 应用中选择实际的麦克风。

### 配置直播或视频会议应用

1. 打开要使用的应用
2. 转至“Settings”（设置），然后浏览至“Voice & Video”（语音和视频）部分
3. 选择 NVIDIA Broadcast 设备：
    1. 麦克风 (NVIDIA Broadcast)
    2. 扬声器 (NVIDIA Broadcast)
    3. 摄像头 (NVIDIA Broadcast)

要详细了解如何配置特定应用，请单击此处。

设置完毕！

## 高级设置

关于多效果：在版本 1.2 及更高版本中，您可以为每个设备组合使用多种 AI 效果。运行多种效果会增加应用的 GPU 资源使用率。
要添加辅助效果，只需单击“Add Effect”（添加效果）按钮即可。
要移除效果，请单击效果名称并向下滚动至“x Remove this effect”（x 移除此效果）。
避免第三方过滤器出现问题：应用有时会使用类似 NVIDIA Broadcast 中的效果，如去噪。应用效果两次往往会造成效果无法正确呈现。我们建议在您的应用和驱动中禁用此类效果。
更改分辨率。如果要调整摄像头分辨率，则需要通过 NVIDIA Broadcast 来完成。在直播/视频会议应用中，应保留默认设置，或与 NVIDIA Broadcast 设置相匹配。如果您在 NVIDIA Broadcast 中更改了网络摄像头的分辨率，则需要在应用中重新加载摄像头（也就是将应用关闭后再打开，如果未设置为“Auto”（自动），则需要调整分辨率）。
如果您经常与麦克风/扬声器连接/断开连接：如果您经常切换麦克风和扬声器（即经常插拔），则可以选择（默认设备）作为 NVIDIA Broadcast 的输入。这样系统会自动将 Windows 检测到的任何麦克风/扬声器用作新的默认设备输入，让您不必每次都进行配置。
将 NVIDIA Broadcast 设置为 Windows“Sound settings”（声音设置）中的默认设备：在 Windows 中，您可以将 NVIDIA Broadcast 选作默认麦克风，这样就不必在每个应用中进行更改。如果选择此选项，请确保在 NVIDIA Broadcast 中选择实际的麦克风。请勿对扬声器执行此操作，因为这样一来，您将开始过滤来自设备的所有音频，如视频和音乐。

## 测试方法

NVIDIA Broadcast 应用具有内嵌的测试功能：

要测试您的麦克风，请在具有背景噪音的环境中录制自己的音频。现在，您可以播放文件并打开和关闭效果，或调节强弱，以查看效果给音频带来哪些变化。
为测试您的扬声器，我们提供了一些录音，您可以在打开和关闭效果时听这些录音，比较一下有哪些变化。您还可以调整效果的强弱。
要测试网络摄像头，只需使用预览窗口。

## OBS Studio

1. 前往“Settings”（设置）>“Audio”（音频）。
2. 选择 NVIDIA Broadcast 作为您的设备：
    1. 在“Devices”（设备）>“Mic/Auxiliary Audio”（麦克风/辅助音频）中，选择“Microphone (NVIDIA Broadcast)”（麦克风 (NVIDIA Broadcast)）。
    2. 在“Advanced”（高级）>“Monitoring Device”（监听设备）中，选择“Speakers (NVIDIA Broadcast)”（扬声器 (NVIDIA Broadcast)）。
3. 要选择 NVIDIA Broadcast 摄像头，请在场景中添加视频捕获源，然后选择“Camera (NVIDIA Broadcast)”（摄像头 (NVIDIA Broadcast)）。保留所有设置的默认值。如果要更改摄像头分辨率，则必须通过 NVIDIA Broadcast 来完成。

## 参考文献

- [下载](https://www.nvidia.com/broadcast-app/)
- [NVIDIA Broadcast 应用：设置指南](https://www.nvidia.cn/geforce/guides/broadcast-app-setup-guide/)
