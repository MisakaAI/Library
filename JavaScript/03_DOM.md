# Document Object Model

当网页被加载时，浏览器会创建页面的**文档对象模型**

```html
<div id="app" class="style" name="name"></div>
```

```js
document.getElementById("app").innerHTML = "Hello World!";
```

## 方法

### 查找 HTML 元素

```js
// 通过元素 id 来查找元素
document.getElementById("app"); // id="app"
```

#### HTMLCollection 对象

HTMLCollection 对象是类数组的 HTML **元素**列表（集合）
可以遍历 HTMLCollection 对象。
但 HTMLCollection 对象不是数组。

```js
// 通过标签名来查找元素
document.getElementsByTagName("div"); // <div></div>

// 通过类名来查找元素
document.getElementsByClassName("style"); // class="style"

// 通过name来查找元素
document.getElementsByName("name"); // name="name"
```

#### NodeList 对象

NodeList 对象是从文档中提取的**节点**列表（集合）。
NodeList 对象与 HTMLCollection 对象几乎相同。

```js
// 通过 CSS 选择器查找 HTML 元素
document.querySelectorAll("div.style"); // <div class="style"></div>
```

### 改变 HTML 元素

```js
var element = document.getElementById("app");

// 改变元素的 inner HTML
element.innerHTML = "Hello World";

// 改变 HTML 元素的属性值
element.className = "s" // class="s"
element.setAttribute("class", "style"); // class="style"

// 改变 HTML 元素的样式
element.style.color = "red"; // style="color: red;"
element.style.visibility = 'hidden'; // style="visibility: hidden;" 隐藏
element.style.visibility = 'visible'; // style="visibility: visible;" 显示
```

### 添加和删除元素

```js
// 创建 HTML 元素
var p = document.createElement('p'); // <p></p>
var b = document.createElement('b'); // <b></b>
var s = document.createElement('s'); // <s></s>

// 创建一个文本节点
var t=document.createTextNode("Hello World"); // Hello World

// 节点添加 HTML 元素
p.appendChild(b); // <p><b></b></p>
b.appendChild(t); // <p><b>Hello World</b></p>

// 删除 HTML 元素
var a = document.getElementById("app");
a.remove();

// 删除 HTML 节点
p.removeChild(b); // <p></p>
b.removeChild(t); // <b></b>

// 替换 HTML 元素
// 用元素 s 来替换掉 b
p.replaceChild(s,b);

// 写入 HTML 输出流
document.write("<h1>Hello World</h1>"); // <h1>Hello World</h1>
```

### 查找 HTML 对象

```js
// 返回文档的 cookie
document.cookie

// 返回 <body> 元素
document.body

// 返回文档的完整 URL
document.URL

// 返回文档的（加载）状态
document.readyState

// 返回文档服务器的域名
document.domain
```

## DOM 事件

- 点击 `onclick`
- 进入页面 `onload`
- 离开页面 `onunload`
- 改变输入内容 `onchange`
- 鼠标移至元素上 `onmouseover`
- 鼠标移出元素后 `onmouseout`
- 点击（按住鼠标） `onmousedown`
- 点击（松开鼠标） `onmouseup`

## 事件监听程序

```js
var element = document.getElementById("app")

// 为指定元素指定事件处理程序
element.addEventListener("click", myFunction);
function myFunction() {
    alert ("Hello World!");
}

// 删除已通过 addEventListener() 方法附加的事件处理程序
element.removeEventListener("mousemove", myFunction);
```
