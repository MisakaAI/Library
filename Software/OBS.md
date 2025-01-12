# OBS Studio

- [官网](https://obsproject.com/)

## 设置

### 常规

- [x] 直播时自动录制

### 直播

- [开播设置](https://link.bilibili.com/p/center/index#/my-room/start-live)

### 输出

输出模式 `高级`

#### 音频

音频码率 `320`

#### 视频编码器: x264

- 使用 CPU 编码

码率控制 `CBR`
码率 `6000 Kbps`
关键帧间隔 `0（自动）`
CPU 预设 `faster` / `medium`
配置(Profile) `high`
微调(Tune) `无`

#### 视频编码器: NVIDIA NVENC H.264

- 使用 GPU 编码

速率控制 `CBR`
码率 `6000`
关键帧间隔 `0（自动）`
预设 `P7：最高质量` `P6：高质量`
调节 `高质量`
多次编码 `单次编码`
配置 `high`

- [ ] `前向考虑`
- [x] `心里视觉调整`

GPU `0`
最大B帧 `2`

### 音频

采样率 `48 kHz`

无录歌需求下，麦克风推荐使用 `声丽 SM-008`
配合 `NVIDIA Broadcast` AI降噪。
使用方法参考 [NVIDIA Broadcast](./Broadcast.md)

有录歌需求，则推荐 电容麦克风 + 专业声卡 + Studio One

- [Studio One](https://www.presonus.com/en/studio-one-pricing.html)

### 视频

基础（画布）分辨率 `1920×1080`
输出（缩放）分辨率 `1920×1080`
缩小算法 `[分辨率相符，不需要缩小]`
常用帧率 `60`

### 高级

进程优先级 `高`
渲染器 `Direct3D 11`
色彩格式 `NV12`
色彩空间 `sRGB`
色彩范围 `常规(Limited)` （B站不支持Full，选择Full，颜色会很奇怪。）
SDR 白电平 `300 nits`
HDR 标称峰值电平 `1000 nits`

## 其他

OBS的实时预览功能没有必要的时候建议关闭。

## 弹幕姬

- [拉普拉斯弹幕机](https://play-live.bilibili.com/details/1698160605076?from=1)
- [直播弹幕姬BLC](https://play-live.bilibili.com/details/1675336975685?from=1)
- [BLC弹幕姬](https://github.com/xfgryujk/blivechat)
- [Bilibili Live Chat](https://github.com/Tsuk1ko/bilibili-live-chat)

### 跨域模式

B站 API 无法被跨域调用，若不开启跨域模式，则会使用反代服务（隐私声明）
若在 OBS 使用，则推荐开启跨域模式，方法如下：
任何基于 Chromium 的浏览器（例如 OBS Browser 和 Chrome）都可以通过添加 --disable-web-security 启动参数来禁用网页安全机制，此时可以开启“跨域模式”选项，几乎所有B站 API 将被直接跨域调用（需要 cookie 的除外），这样就不需要依赖反代服务。

#### OBS

直接在启动的快捷方式后追加该参数，然后通过快捷方式启动即可

```sh
--disable-web-security
```

#### Chrome

和 OBS 同理，不过必须额外添加一个 `--user-data-dir` 参数来指定用户目录，随意新建一个空文件夹来指定即可。
该操作看上去十分麻烦，实则是 Chrome 的一个安全措施，因为**禁用网页安全机制是危险行为，日常使用时千万别这么做**

```css
body {
    background-color: rgba(0, 0, 0, 0);
    margin: 0px auto;
    overflow: hidden;
}

.danmaku-content {
    padding-left: 5px;
    padding-bottom:5px;
    height: auto;
}
.danmaku-message,.danmaku-author-name,.danmaku-gift-name,.danmaku-gift-num {
    font-family: "凤凰点阵体 16px";
    font-weight: normal;
    font-size:32px;
    line-height:38px;
}
.danmaku-author-face {
    width: 38px;
    height: 38px;
    border-radius: 38px;
    margin-right: 5px;
}
```

## 参考文献

- [给新人主播一些OBS设置建议，让你的直播间画质提升个数量级。](https://www.bilibili.com/read/cv7482412/)
