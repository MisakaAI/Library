# JavaScript Cookie

Cookie 是在计算机上存储在小的文本文件中的数据。

## 创建 cookie

```js
/*  */
document.cookie = "username=Bill Gates";

// 可以添加有效日期（UTC 时间）
// 默认情况下，在浏览器关闭时会删除 cookie
document.cookie = "username=Bill Gates; expires=Sun, 31 Dec 2017 12:00:00 UTC";

// 可以告诉浏览器 cookie 属于什么路径
// 默认情况下，cookie 属于当前页
document.cookie = "username=Bill Gates; expires=Sun, 31 Dec 2017 12:00:00 UTC; path=/";

// 设置 cookie 的函数
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
```

## 读取 cookie

```js
var x = document.cookie;

// 获取 cookie 的函数
function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
         }
         if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
         }
     }
    return "";
}
```

## 改变 cookie

```js
document.cookie = "username=Steve Jobs; expires=Sun, 31 Dec 2017 12:00:00 UTC; path=/";
```

## 检测 cookie

```js
// 检测 cookie 的函数
function checkCookie() {
    var username = getCookie("username");
    if (username != "") {
        alert("Welcome again " + username);
    } else {
        username = prompt("Please enter your name:", "");
        if (username != "" && username != null) {
            setCookie("username", username, 365);
        }
    }
}
```

## 删除 cookie

```js
// 直接把 expires 参数设置为过去的日期即可
document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
```
