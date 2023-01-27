# 等待

## 显式等待

显示等待 是Selenium客户可以使用的命令式过程语言。
它们允许您的代码暂停程序执行，或冻结线程，直到满足通过的 条件 。
这个条件会以一定的频率一直被调用，直到等待超时。
这意味着只要条件返回一个假值，它就会一直尝试和等待

```python
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
WebDriverWait(driver, timeout=10).until(lambda x: x.find_element(By.ID, "someId"))
```

### 预期的条件

由于必须同步DOM和指令是相当常见的情况，所以大多数客户端还附带一组预定义的 预期条件。

Python’s [selenium.webdriver.support.expected_conditions](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected) class

```python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# 检查网页上是否至少存在一个元素。
WebDriverWait(driver,timeout=10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'ion-header-bar')))

# 检查给定文本是否存在于指定元素中。
WebDriverWait(driver,timeout=10).until(EC.text_to_be_present_in_element((By.ID, "app"),'hello'))
```

## 隐式等待

通过隐式等待，WebDriver在试图查找任何元素时，在一定时间内轮询DOM。
当网页上的某些元素不是立即可用并且需要一些时间来加载时是很有用的。
默认情况下隐式等待元素出现是禁用的，它需要在单个会话的基础上手动启用。
将显式等待和隐式等待混合在一起会导致意想不到的结果，就是说即使元素可用或条件为真也要等待睡眠的最长时间。

警告: 不要混合使用隐式和显式等待。这样做会导致不可预测的等待时间。
例如，将隐式等待设置为10秒，将显式等待设置为15秒，可能会导致在20秒后发生超时。

隐式等待是告诉WebDriver如果在查找一个或多个不是立即可用的元素时轮询DOM一段时间。
默认设置为0，表示禁用。一旦设置好，隐式等待就被设置为会话的生命周期。

```python3
driver = Firefox()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")
```

## 流畅等待

流畅等待实例定义了等待条件的最大时间量，以及检查条件的频率。
用户可以配置等待来忽略等待时出现的特定类型的异常，例如在页面上搜索元素时出现的NoSuchElementException。

```python
driver = Firefox()
driver.get("http://somedomain/url_that_delays_loading")
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))

# is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).until_not(lambda x: x.find_element(By.ID, "someId").is_displayed())
```

`timeout` 超时前的秒数
`poll_frequency` 调用之间睡眠时间间隔默认情况下为0. 5秒。
`ignored_exceptions` 调用期间忽略的异常类的可迭代结构。默认情况下，它只包含NoSuchElementException。

`until` 调用驱动程序提供的方法作为参数，直到返回值的计算结果为True。
`until_not` 调用驱动程序提供的方法作为参数，直到返回值计算为False。