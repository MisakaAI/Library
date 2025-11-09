# Emmet

Emmet 使用类似于 CSS 选择器的语法来描述元素的结构与属性。
可以极大的提升 HTML 编写效率。

- [Emmet](https://www.emmet.io/)

## 初始化 HTML 结构

`html:5` 或 `!`

之后会出现

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

可以使用[代码片段](quickSuggestions.md#html)代替此功能，创建及使用自己的模板。

## HTML 常用语法

- 子代（嵌套） `>`

```html
<!-- div>p -->
<div>
    <p></p>
</div>
```

- 同级 `+`

```html
<!-- div+p -->
<div></div>
<p></p>
```

- 回到上级 `^`

```html
<!-- div>p>i^b -->
<div>
    <p><i></i></p>
    <b></b>
</div>
```

- 多个 `*`

```html
<!-- p*3 -->
<p></p>
<p></p>
<p></p>
```

- 样式 `.`

```html
<!-- p.css -->
<p class="css"></p>
```

- ID `#`

```html
<!-- div#app -->
<div id="app"></div>
```

- 属性 `[]`

```html
<!-- img[src="a.jpg"] -->
<img src="a.jpg" alt="">

<!-- a[href="index.html"] -->
<a href="index.html"></a>
```

- 内容 `{}`

```html
<!-- p{test} -->
<p>test</p>
```

- 分组 `()`

```html
((p>span*3)+(a*3>div))*2
<p><span></span><span></span><span></span></p>
<a href=""><div></div></a>
<a href=""><div></div></a>
<a href=""><div></div></a>
<p><span></span><span></span><span></span></p>
<a href=""><div></div></a>
<a href=""><div></div></a>
<a href=""><div></div></a>
```

- 序号 `$`

```html
a[href='$.jpg']{link $}*3
<a href="1.jpg">link 1</a>
<a href="2.jpg">link 2</a>
<a href="3.jpg">link 3</a>
```

- 随机填充 `lorem<number>` （ lorem 是 Lorem ipsum 的简称 ）

```html
<!-- ul>lorem3*4 -->
<ul>
    <li>Lorem, ipsum dolor.</li>
    <li>Impedit, sit pariatur?</li>
    <li>Rem, nemo. Similique.</li>
    <li>Quis, quam qui!</li>
</ul>
<!-- p>lorem2*3 -->
<p><span>Lorem, ipsum.</span><span>Fugiat, esse.</span><span>Cupiditate, quisquam?</span></p>
```

## CSS 常用缩写

```css
.body{
    /* w400+h300+m24+p32 */
    width: 400px;
    height: 300px;
    margin: 24px;
    padding: 32px;

    /* m0-0-24-0 */
    margin: 0 0 24px 0;

    /* fz20 */
    font-size: 20px;

    /* fz1.5 */
    font-size: 1.5em;

    /* fw500 */
    font-weight: 500;

    /* fwb */
    font-weight: bold;

    /* lh48 */
    line-height: 48;

    /* bgc */
    background-color: #fff;

    /* dib */
    display: inline-block;

    /* dif */
    display: inline-flex;

    /* df */
    display: flex;
}
```

## 长标签缩写

```html
<!-- script:src -->
<script src=""></script>

<!-- link:css -->
<link rel="stylesheet" href="style.css">

<!-- link:favicon -->
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">

<!-- a:link -->
<a href="http://"></a>

<!-- inp -->
<input type="text" name="" id="">

<!-- input:password -->
<input type="password" name="" id="">

<!-- btn -->
<button></button>

<!-- btn:s -->
<button type="submit"></button>
```
