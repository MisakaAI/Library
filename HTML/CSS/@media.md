# 利用 @media screen 实现网页布局的自适应

优点:无需插件和手机主题,对移动设备友好,能够适应各种窗口大小。
只需在CSS中添加 `@media screen` 属性,根据浏览器宽度判断并输出不同的长宽值。

## 准备工作

### 1：设置 Meta 标签

使用 Media 的时候需要先设置下面这段代码，来兼容移动设备的展示效果：

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
```

这段代码的几个参数解释：

- `width = device-width`：宽度等于当前设备的宽度
- `height = device-height`：高度等于当前设备的高度
- `initial-scale`：初始的缩放比例（默认设置为1.0）
- `minimum-scale`：允许用户缩放到的最小比例（默认设置为1.0）
- `maximum-scale`：允许用户缩放到的最大比例（默认设置为1.0）
- `user-scalable`：用户是否可以手动缩放（默认设置为no，因为我们不希望用户放大缩小页面）

### 2：加载兼容文件JS

因为 IE8 既不支持 HTML5 也不支持 CSS3 Media，所以我们需要加载两个 JS 文件，来保证我们的代码实现兼容效果：

```html
<!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
  <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
<![endif]-->
```

**如果不是政府机构的网站，或者目标客户电脑都比较老的，那不考虑 IE 的兼容性也是没问题的。**

### 3：设置IE渲染方式默认为最高

**这部分可以选择添加也可以不添加。**

~~现在有很多人的IE浏览器都升级到IE9以上了，所以这个时候就有又很多诡异的事情发生了，例如现在是IE9的浏览器，但是浏览器的文档模式却是IE8:~~
~~为了防止这种情况，需要加入`<meta http-equiv="X-UA-Compatible" content="IE=edge">`这段代码来让IE的文档模式永远都是最新的。~~
~~如果想使用固定的IE版本，可写成：`<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9">`~~

```html
<meta http-equiv="X-UA-Compatible" content="IE=Edge，chrome=1">
```

这段代码后面加了一个`chrome=1`，这个 Google Chrome Frame（谷歌内嵌浏览器框架GCF）
如果有的用户电脑里面装了这个 chrome 的插件，就可以让电脑里面的IE不管是哪个版本的都可以使用 `Webkit引擎` 及 `V8引擎` 进行排版及运算
不过如果用户没装这个插件，那这段代码就会让IE以最高的文档模式展现效果。

## CSS3 Media 写法

我们先来看下下面这段代码，估计很多人在响应式的网站CSS很经常看到类似下面的这段代码：

```css
@media screen and (max-width: 960px){
    body{
        background: #000;
    }
}
```

这个应该算是一个media的一个标准写法，上面这段CSS代码意思是：
当页面小于 960px 的时候执行它下面的 CSS。

应该有人会发现上面这段代码里面有个`screen`，他的意思是在告知设备在打印页面时使用衬线字体，在屏幕上显示时用无衬线字体。
但是很多网站都会直接省略`screen`,因为你的网站可能不需要考虑用户去打印时，可以直接这样写：

```css
@media (max-width: 960px){
    body{
        background: #000;
    }
}
```

在第一段代码上面我用的是小于960px的尺寸的写法，那现在我们来实现等于 960px 尺寸的代码：

```css
@media screen and (max-device-width:960px){
    body{
        background:red;
    }
}
```

然后就是当浏览器尺寸大于960px时候的代码了：

```css
@media screen and (min-width:960px){
    body{
        background:orange;
    }
}
```

我们还可以混合使用上面的用法：的这段代码的意思是当页面宽度大于960px小于1200px的时候执行下面的CSS。

```css
@media screen and (min-width:960px) and (max-width:1200px){
    body{
        background:yellow;
    }
}
```

### CSS2 Media 用法

其实并不是只有 CSS3 才支持 Media 的用法，早在CSS2开始就已经支持 Media。
具体用法，就是在 HTML 页面的 head 标签中插入`<link rel="stylesheet" type="text/css" media="screen" href="style.css">`这段代码。
上面其实是 CSS2 实现的衬线用法，那 CSS2 的 media 难道就只能支持上面这一个功能吗？答案当然不是，他还有很多用法。
例如我们想知道现在的移动设备是不是纵向放置的显示屏，可以这样写：
`<link rel="stylesheet" type="text/css" media="screen and (orientation:portrait)" href="style.css">`
我们把第一段的代码也用 CSS2 来实现，让它一样可以让页面宽度小于 960px 的执行指定的样式文件：
`<link rel="stylesheet" type="text/css" media="screen and (max-width:960px)" href="style.css">`

```html
<link rel="stylesheet" type="text/css" media="screen and (min-width:801px)" href="css/pc.css">
<link rel="stylesheet" type="text/css" media="screen and (max-width:800px)" href="css/mobile.css">
```

既然CSS2可以实现CSS的这个效果为什么不用这个方法呢？
因为上面这个方法，最大的弊端是他会增加页面http的请求次数，增加了页面负担。
我们用 CSS3 把样式都写在一个文件里面才是最佳的方法。

### Media 所有参数汇总

以上就是我们最常需要用到的媒体查询器的三个特性，大于，等于，小于的写法。
媒体查询器的全部功能肯定不止这三个功能，下面是我总结的它的一些参数用法解释：

- `width`: 浏览器可视宽度。
- `height`: 浏览器可视高度。
- `device-width`: 设备屏幕的宽度。
- `device-height`: 设备屏幕的高度。
- `orientation`: 检测设备目前处于横向还是纵向状态。
- `aspect-ratio`: 检测浏览器可视宽度和高度的比例。(例如：`aspect-ratio:16/9`)
- `device-aspect-ratio`: 检测设备的宽度和高度的比例。
- `color`: 检测颜色的位数。（例如：`min-color:32`就会检测设备是否拥有32位颜色）
- `color-index`: 检查设备颜色索引表中的颜色，他的值不能是负数。
- `monochrome`: 检测单色楨缓冲区域中的每个像素的位数。（这个太高级，估计咱很少会用的到）
- `resolution`: 检测屏幕或打印机的分辨率。(例如：`min-resolution:300dpi`或`min-resolution:118dpcm`)。
- `grid`: 检测输出的设备是网格的还是位图设备。

需要注意顺序，如果你把 `@media (min-width: 768px)` 写在了下面那么很悲剧

```css
@media (min-width: 1200px){/* >= 1200 的设备 */}
@media (min-width: 992px){ /* >= 992 的设备 */ }
@media (min-width: 768px){ /* >= 768 的设备 */ }
```

如果是`1440px`,由于 1440>768 那么 `1200px` 就会失效。

所以用 `min-width` 时，小的放上面，大的在下面。
如果用 `max-width` 时，大的在上面，小的在下面。

```css
@media (max-width: 1199px){/* <= 1199 的设备 */}
@media (max-width: 991px){ /* <= 991 的设备 */ }
@media (max-width: 767px){ /* <= 768 的设备 */ }
```

#### 参考

```css
/* 1280分辨率以上（大于1200px）*/
@media screen and (min-width: 1200px) {}

/* 1100分辨率（大于960px，小于1199px）*/
@media screen and (min-width: 960px) and (max-width: 1199px) {}

/* 880分辨率（大于768px，小于959px）*/
@media screen and (min-width: 768px) and (max-width: 959px) {}

/* 720分辨率（大于480px，小于767px）*/
@media only screen and (min-width: 480px) and (max-width: 767px) {}

/* 440分辨率以下（小于479px）*/
@media only screen and (max-width: 479px) {}

/* 竖屏 */
@media screen and (orientation: portrait) and (max-width: 720px) {}

/* 横屏 */
@media screen and (orientation: landscape) {}
```

## 参考资料

- [利用@media screen实现网页布局的自适应](https://blog.csdn.net/inuyasha1121/article/details/50777116)