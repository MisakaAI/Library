# JavaScript 浏览器对象

## Window 对象 `window`

- 浏览器窗口的内高度（以像素计） `window.innerWidth`
- 浏览器窗口的内宽度（以像素计） `window.innerHeight`
- 打开新窗口 `window.open()`
- 关闭当前窗口 `window.close()`
- 移动当前窗口 `window.moveTo()`
- 重新调整当前窗口 `window.resizeTo()`

## 用户屏幕信息 `window.screen`

可不带 window 前缀

- 屏幕宽度`screen.width`
- 屏幕高度 `screen.height`
- 可用宽度 `screen.availWidth` *减去诸如窗口工具条之类的界面特征*
- 可用高度 `screen.availHeight` *减去诸如窗口工具条之类的界面特征*
- 色深 `screen.colorDepth`
- 像素深度 `screen.pixelDepth`

## Window Location `window.location`

可不带 window 前缀

- URL `location.href`
- 主机名 `location.hostname`
- 路径名 `location.pathname`
- 协议 `location.protocol` *http 或 https*
- 端口 `location.port`
- 加载新文档 `location.assign`
- 刷新 `location.reload()`

## 浏览器历史 `window.history`

可不带 window 前缀

- 后退 `history.back()`
- 前进 `history.forward()`

## 有关访问者的信息 `window.navigator`

可不带 window 前缀

- Cookie 启用 `navigator.cookieEnabled`
- 用户代理报头 `navigator.userAgent` *浏览器无法报告发布晚于浏览器的新操作系统*
- 语言 `navigator.language`
