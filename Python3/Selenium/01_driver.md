# 浏览器和驱动

Selenium不能直接操作浏览器，通过驱动，可以使Selenium对浏览器进行一些操作。

## 驱动

- [Chrome](https://chromedriver.chromium.org/downloads)
- [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- [FireFox](https://github.com/mozilla/geckodriver/releases)
- [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

## 打开浏览器

每个浏览器都有定制和特有的功能。
这里使用Chrome浏览器。

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome()
service = Service(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=service)
```

## 选项

```python
options = ChromeOptions()

# 直接设置手机型号
mobileEmulation = {'deviceName': 'Pixel 5'}

# 单独设置手机信息
# 宽度
WIDTH = 480
# 高度
HEIGHT = 800
# 像素比
PIXEL_RATIO = 1
UA = "Mozilla/5.0 (Linux; Android 9; DT40) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
options.add_experimental_option('mobileEmulation', mobileEmulation)

# 开发者模式
options.add_argument("--auto-open-devtools-for-tabs")

# 驱动中设置以上选项
driver = webdriver.Chrome(options=options)

# 最大化
driver.maximize_window()

# 最小化
driver.minimize_window()

## 全屏窗口
driver.fullscreen_window()

# 打开网页
driver.get("https://www.baidu.com")

# 退出
driver.quit()
```
