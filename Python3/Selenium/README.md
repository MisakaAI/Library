# Selenium

Selenium是一个用于Web应用程序测试的工具。

- [Selenium](https://www.selenium.dev/)
- [pypi](https://pypi.org/project/selenium/)
- [api](https://www.selenium.dev/selenium/docs/api/py/api.html)

## 安装

- [Selenium Client Driver](https://www.selenium.dev/selenium/docs/api/py/index.html#installing)

```bash
pip install selenium
```

## 目录

[浏览器驱动](01_driver.md)
[交互](02_interactions.md)
[等待策略](03_waits.md)
[元素对象](04_elements.md)

使用驱动实例开启会话

```python
driver = webdriver.Chrome()
```

在浏览器上执行操作

```python
driver.get("https://www.baidu.com")
```

请求 浏览器信息

```python
title = driver.title
```

建立等待策略

```python
driver.implicitly_wait(0.5)
```

发送命令 查找元素

```python
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
```

操作元素

```python
text_box.send_keys("Selenium")
submit_button.click()
```

获取元素信息

```python
value = message.text
```

结束会话

```python
driver.quit()
```

## 参考资料

- [白月黑羽](https://www.byhy.net/tut/auto/selenium/01/)
