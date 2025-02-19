# yt-dlp

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## 一般选项

-U, --update 将此程序更新到最新版本

## 网络代理

--proxy socks5://127.0.0.1:7890

## 视频选择

默认情况下，yt-dlp会尝试下载最好的可用质量，如果你不通过任何选项。

## Cookie

--cookies-from-browser BROWSER[+KEYRING][:PROFILE][::CONTAINER]
    从浏览器加载 cookies
    目前支持的浏览器有：brave, chrome, chromium, edge, firefox, opera, safari, vivaldi, whale

```sh
yt-dlp --proxy socks5://127.0.0.1:7890 --cookies-from-browser firefox https://www.youtube.com/watch\?v\=AhP9LurfNws
```

## 仅下载音频

```sh
yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0
```
