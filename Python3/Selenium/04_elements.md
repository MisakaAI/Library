# 元素

## 查询网络元素

[查询网络元素](https://www.selenium.dev/zh-cn/documentation/webdriver/elements/finders/)

根据提供的定位值定位元素

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# 匹配第一个符合条件的元素
driver.find_element(By.CLASS_NAME, "tomatoes")

# 匹配所有符合条件的元素
driver.find_elements(By.TAG_NAME, "li")
```

## 定位策略

[定位策略](https://www.selenium.dev/zh-cn/documentation/webdriver/elements/locators/)
[By](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.by.html#module-selenium.webdriver.common.by)

在 WebDriver 中有 8 种不同的内置元素定位策略：

```python
CLASS_NAME = 'class name'
CSS_SELECTOR = 'css selector'
ID = 'id'
LINK_TEXT = 'link text'
NAME = 'name'
PARTIAL_LINK_TEXT = 'partial link text'
TAG_NAME = 'tag name'
XPATH = 'xpath'
```

定位器 Locator|描述
-|-
class name | 定位class属性与搜索值匹配的元素（不允许使用复合类名）
css selector | 定位 CSS 选择器匹配的元素
id | 定位 id 属性与搜索值匹配的元素
name | 定位 name 属性与搜索值匹配的元素
link text | 定位link text可视文本与搜索值完全匹配的锚元素
partial link text | 定位link text可视文本部分与搜索值部分匹配的锚点元素。如果匹配多个元素，则只选择第一个元素。
tag name | 定位标签名称与搜索值匹配的元素
xpath | 定位与 XPath 表达式匹配的元素

### 相对定位

```python
from selenium.webdriver.support.relative_locator import locate_with

# above 上
locate_with(By.TAG_NAME, "input").above({By.ID: "password"})

# below 下
locate_with(By.TAG_NAME, "input").below({By.ID: "email"})

# to_left_of 左
locate_with(By.TAG_NAME, "button").to_left_of({By.ID: "submit"})

# to_right_of 右
locate_with(By.TAG_NAME, "button").to_right_of({By.ID: "cancel"})

# near 近
locate_with(By.TAG_NAME, "input").near({By.ID: "lbl-email"})

# 组合相对定位
locate_with(By.TAG_NAME, "button").below({By.ID: "email"}).to_right_of({By.ID: "cancel"})
```

## 元素交互

[Web元素交互](https://www.selenium.dev/zh-cn/documentation/webdriver/elements/interactions/)

用于操纵表单的高级指令集

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 点击 (适用于任何元素)
driver.find_element(By.NAME, "q").click()

# 发送键位 (仅适用于文本字段和内容可编辑元素)
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

# 清除 (仅适用于文本字段和内容可编辑元素)
driver.find_element(By.NAME, "q").clear()

# 提交 (仅适用于表单元素)
# 在 Selenium 4 中不推荐使用此方式，检验使用表单中的 button 进行提交。

# 选择 (参见 选择列表元素)
# https://www.selenium.dev/documentation/webdriver/support_features/select_lists/
```

### 选择列表元素

[使用选择列表元素](https://www.selenium.dev/zh-cn/documentation/webdriver/support_features/select_lists/)

```python
## 构建
# 首先定位一个 <select> 元素, 然后借助其初始化一个Select 对象
select_element = driver.find_element(By.NAME, 'selectomatic')
select = Select(select_element)

## 选择
# 根据其可见文本选择选项
select.select_by_visible_text('Four')
# 根据其值属性选择选项
select.select_by_value('two')
# 根据其在列表中的位置选择选项
select.select_by_index(3)

## 禁用的选项
# 具有 disabled 属性的选项可能无法被选择

## 取消选择选项
# 只有复选类型的选择列表才能取消选择选项. 您可以对要选择的每个元素重复使用这些方法.
select.deselect_by_value('eggs')
```

### 发送键位 Keys

[Keys](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#module-selenium.webdriver.common.keys)

#### 常见的键盘操作

```python
# 删除键
sent_keys(Keys.BACK_SPACE)    
# 空格键
sent_keys(Keys.SPACE)
# Tab 键
sent_keys(Keys.TAB)
# Delete 键
sent_keys(Keys.DELETE)
# + 键
sent_keys(Keys.ADD)
# Enter 键
sent_keys(Keys.ENTER)
# Shift 键
sent_keys(Keys.SHIFT)
# ctrl+A：全选
sent_keys(Keys.CONTROL, 'a')
# ctrl+C：复制
sent_keys(Keys.CONTROL, 'c')
# ctrl+V：粘贴
sent_keys(Keys.CONTROL, 'v')
# ctrl+X：剪切
sent_keys(Keys.CONTROL, 'x')
# F1 键
sent_keys(Keys.F1)
# 数字 9 键
sent_keys(Keys.NUMPAD9)
```

## 信息

[关于网络元素的信息](https://www.selenium.dev/zh-cn/documentation/webdriver/elements/information/)

查询有关特定元素的许多详细信息

```python
# 是否显示
driver.find_element(By.NAME, "email_input").is_displayed()

# 是否启用
driver.find_element(By.NAME, 'btnK').is_enabled()

# 是否被选定
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type").is_selected()

# 获取元素标签名
driver.find_element(By.CSS_SELECTOR, "h1").tag_name

# 位置和大小
driver.find_element(By.CSS_SELECTOR, "h1").rect

# 获取元素CSS值
driver.find_element(By.LINK_TEXT, "More information...").value_of_css_property('color')

# 文本内容
driver.find_element(By.CSS_SELECTOR, "h1").text

# 获取特性或属性
driver.find_element(By.NAME, "email_input").get_attribute("value")

# 获取坐标
driver.find_element(By.CSS_SELECTOR, 'h1').location
```

## 文件上传

[文件上传](https://www.selenium.dev/zh-cn/documentation/webdriver/elements/file_upload/)

当input元素为文件类型时, 文件上传对话框可以使用Selenium处理

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/upload");
driver.find_element(By.ID,"file-upload").send_keys("selenium-snapshot.jpg")
driver.find_element(By.ID,"file-submit").submit()
if(driver.page_source.find("File Uploaded!")):
    print("file upload success")
else:
    print("file upload not successful")
driver.quit()
```

## 颜色

[同颜色一起工作](https://www.selenium.dev/zh-cn/documentation/webdriver/support_features/colors/)

```python
from selenium.webdriver.support.color import Color

# HEX
HEX_COLOUR = Color.from_string('#2F7ED8')
# RGBA
RGB_COLOUR = Color.from_string('rgb(255, 255, 255, 1)')
# 透明
TRANSPARENT = Color.from_string('transparent')
# 颜色名
BLACK = Color.from_string('black')
HOTPINK = Color.from_string('hotpink')

# 查询元素以获取其颜色
Color.from_string(driver.find_element(By.ID,'login').value_of_css_property('color'))
# 查询元素以获取其背景颜色
Color.from_string(driver.find_element(By.ID,'login').value_of_css_property('background-color'))

# 对比颜色
assert login_button_background_colour == HOTPINK

# 将颜色转换为以下格式之一并执行静态验证
assert login_button_background_colour.hex == '#ff69b4'
assert login_button_background_colour.rgb == 'rgb(255, 105, 180)'
assert login_button_background_colour.rgba == 'rgba(255, 105, 180, 1)'
```

## 鼠标

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 创建浏览器实例对象
driver = webdriver.Chrome()
# 创建鼠标实例化对象
chains = ActionChains(driver)

# 先通过 xpath 定位登录按钮
login = driver.find_element_by_xpath("//button[text()='登录']")
# 鼠标左键单击登录按钮
chains.click(login).perform()

## 常用鼠标操作
# 单击鼠标左键
click(ele)
# 单击鼠标右键
context_click(ele)
# 双击鼠标左键
double_click(ele)
# 拖动某个元素后松开
drag_and_drop(source, target)
# 鼠标悬停在一个元素上
move_to_element(ele)
# 在某个元素上单击鼠标左键，不松开
click_and_hold(ele)
# 在某个元素上松开鼠标左键
release()
# 执行上速鼠标操作
perform()
```
