# JavaScript 定时事件

`setTimeout()` 和 `setInterval()` 都属于 HTML DOM Window 对象的方法。

- 在等待指定的毫秒数后执行函数 `setTimeout(function, milliseconds)`
- 等同于 setTimeout()，但持续重复执行该函数 `setInterval(function, milliseconds)`

```js
// 5000毫秒（5秒）后刷新页面
setTimeout(function() {
    location.reload();
}, 5000);
```

## 停止执行

使用 `clearTimeout()` 和 `clearInterval()`
通常绑定在 `<button>` 上使用。

```js
var r = function() {
    location.reload();
}
var t = setTimeout(r,5000);
clearTimeout(t);
```
