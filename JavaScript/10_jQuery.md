# jQuery

## jQuery 安装

从官网下载

```html
<script src="jquery.js"></script>
```

### Package

```sh
# npm
npm install jquery

# yarn
yarn add jquery
```

### CDN

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
```

## jQuery 使用

```html
<div id="app">Hello World</div>
```

```js
// 获取 id="app" 元素
var a = $("#app");

// 隐藏元素
a.hide();

// 显示元素
a.show();

// 删除元素
a.remove();

// 隐藏所有 <p> 元素
$("p").hide();
```

### 内容操作

```html
<div></div>
```

```js
// 获取 div
$("div:eq(0)");

// 修改 id 属性
$("div:eq(0)").attr('id','app');

// 获取 id="app" 元素
var a = $("#app");

// 获取 id 属性
a.attr('id');

// 删除属性
a.removeAttr('id');

// 写入文本内容
a.text("Hello World")

// 获取文本内容
a.text()
```

### 获取元素

```html
<ul>
    <li>Apple</li>
    <li>Banana</li>
    <li><span style="color: orange;">Orange</span></li>
</ul>
```

```js
// 获取节点
$("ul").children();

// 查找元素
$("ul").find("span"); // <span style="color: orange;">Orange</span>

// 父元素
$("span").parent(); // <li><span style="color: orange;">Orange</span></li>

// 同级元素
$("span").parent().siblings(); // <li>Apple</li> <li>Banana</li>
```

## jQuery 事件

```js
// 将函数绑定到文档的就绪事件
$(document).ready(function)

// 触发或将函数绑定到被选元素的点击事件
$(selector).click(function)

// 触发或将函数绑定到被选元素的双击事件
$(selector).dblclick(function)

// 触发或将函数绑定到被选元素的获得焦点事件
$(selector).focus(function)

// 触发或将函数绑定到被选元素的鼠标悬停事件
$(selector).mouseover(function)
```
