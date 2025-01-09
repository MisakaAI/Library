# Chrome

## 开机启动

```sh
# 窗口
"C:\Program Files\Google\Chrome\Application\chrome.exe" --chrome --window-size=1936,1120 --disable-notifications --disable-popup-blocking --incognito --disable-pinch --no-user-gesture-required --overscroll-history-navigation=0 --app="%~dp0\index.html"

## 全屏
"C:\Program Files\Google\Chrome\Application\chrome.exe" --kiosk "%~dp0\index.html"

## 全屏2
"C:\Program Files\Google\Chrome\Application\chrome.exe" --chrome --kiosk --disable-notifications --disable-popup-blocking --incognito --disable-pinch --no-user-gesture-required --overscroll-history-navigation=0 "%~dp0\index.html"
```
