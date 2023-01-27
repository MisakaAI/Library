# 浏览器交互

[交互](https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/)

## 获取浏览器信息

[获取浏览器信息](https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/#获取浏览器信息)

```python
# 获取标题
driver.title

# 获取当前 UR
driver.current_url
```

## 浏览器导航

[浏览器导航](https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/navigation/)

```python
# 打开网站
driver.get("https://selenium.dev")

# 后退
driver.back()

# 前进
driver.forward()

# 刷新
driver.refresh()
```

## JavaScript 警告框,提示框和确认框

[JavaScript 警告框,提示框和确认框](https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/alerts/)

```python
## Alerts 警告框
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()

# Wait for the alert to be displayed and store it in a variable
alert = wait.until(expected_conditions.alert_is_present())

# Store the alert text in a variable
text = alert.text

# Press the OK button
alert.accept()

## Confirm 确认框
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample confirm").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = driver.switch_to.alert

# Store the alert text in a variable
text = alert.text

# Press the Cancel button
alert.dismiss()

## Prompt 提示框
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample prompt").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = Alert(driver)

# Type your message
alert.send_keys("Selenium")

# Press the OK button
alert.accept()
```

## Cookies

[同cookies一起工作](https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/cookies/)

```python
## 添加 Cookie
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "key", "value": "value"})

## 获取命名的 Cookie
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "foo", "value": "bar"})

# Get cookie details with named cookie 'foo'
print(driver.get_cookie("foo"))

## 获取全部 Cookies
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Get all available cookies
print(driver.get_cookies())

## 删除 Cookie
from selenium import webdriver
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Delete a cookie with name 'test1'
driver.delete_cookie("test1")

## 删除所有 Cookies
from selenium import webdriver
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

#  Deletes all cookies
driver.delete_all_cookies()
```

## IFrames和frames

[与IFrames和frames一起工作](https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/frames/)

```python
## 使用 WebElement
# 存储网页元素
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")

# 切换到选择的 iframe
driver.switch_to.frame(iframe)

# 单击按钮
driver.find_element(By.TAG_NAME, 'button').click()

## 使用 name 或 id
# 通过 id 切换框架
driver.switch_to.frame('buttonframe')

# 单击按钮
driver.find_element(By.TAG_NAME, 'button').click()

## 使用索引
# 基于索引切换到第 2 个 iframe
iframe = driver.find_elements(By.TAG_NAME,'iframe')[1]

# 切换到选择的 iframe
driver.switch_to.frame(iframe)

## 离开框架
# 切回到默认内容
driver.switch_to.default_content()
```

## 窗口和标签

[同窗口和标签一起工作](https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/windows/)

```python
## 获得当前窗口的窗口句柄
driver.current_window_handle

## 切换窗口或标签页
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 启动驱动程序
with webdriver.Firefox() as driver:
# 打开网址
driver.get("https://seleniumhq.github.io")

# 设置等待
wait = WebDriverWait(driver, 10)

# 存储原始窗口的 ID
original_window = driver.current_window_handle

# 检查一下，我们还没有打开其他的窗口
assert len(driver.window_handles) == 1

# 单击在新窗口中打开的链接
driver.find_element(By.LINK_TEXT, "new window").click()

# 等待新窗口或标签页
wait.until(EC.number_of_windows_to_be(2))

# 循环执行，直到找到一个新的窗口句柄
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# 等待新标签页完成加载内容
wait.until(EC.title_is("SeleniumHQ Browser Automation"))

## 创建新窗口(或)新标签页并且切换
# 打开新标签页并切换到新标签页
driver.switch_to.new_window('tab')

# 打开一个新窗口并切换到新窗口
driver.switch_to.new_window('window')

## 关闭窗口或标签页
#关闭标签页或窗口
driver.close()

#切回到之前的标签页或窗口
driver.switch_to.window(original_window)

## 在会话结束时退出浏览器
driver.quit()
```

### 窗口管理

[窗口管理](https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/windows/#窗口管理)

```python
## 获取窗口大小
# # 分别获取每个尺寸
width = driver.get_window_size().get("width")
height = driver.get_window_size().get("height")

# 或者存储尺寸并在以后查询它们
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")

## 设置窗口大小
driver.set_window_size(1024, 768)

## 得到窗口的位置 （获取浏览器窗口左上角的坐标）
# 分别获取每个尺寸
x = driver.get_window_position().get('x')
y = driver.get_window_position().get('y')

# 或者存储尺寸并在以后查询它们
position = driver.get_window_position()
x1 = position.get('x')
y1 = position.get('y')

## 设置窗口位置
# 将窗口移动到主显示器的左上角
driver.set_window_position(0, 0)

## 最大化窗口
driver.maximize_window()

## 最小化窗口
driver.minimize_window()

## 全屏窗口
driver.fullscreen_window()

## 屏幕截图
from selenium import webdriver
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

# Returns and base64 encoded string into image
driver.save_screenshot('./image.png')

driver.quit()

## 元素屏幕截图
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

ele = driver.find_element(By.CSS_SELECTOR, 'h1')

# Returns and base64 encoded string into image
ele.screenshot('./image.png')

driver.quit()

## 执行脚本
# Stores the header element
header = driver.find_element(By.CSS_SELECTOR, "h1")

# Executing JavaScript to capture innerText of header element
driver.execute_script('return arguments[0].innerText', header)

## 打印页面 （此功能需要无头模式下的Chromium浏览器）
from selenium.webdriver.common.print_page_options import PrintOptions

print_options = PrintOptions()
print_options.page_ranges = ['1-2']

driver.get("printPage.html")

base64code = driver.print_page(print_options)

```

## 虚拟身份验证器

[虚拟身份验证器](https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/virtual_authenticator/)