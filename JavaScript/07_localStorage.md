# JavaScript 本地存储

`localStorage` 对象存储没有到期日期的数据，浏览器关闭时数据不会被删除。
`sessionStorage` 对象仅存储一个会话的数据，关闭浏览器选项卡时数据将被删除。

```js
// 保存数据
localStorage.setItem("key", "value");
sessionStorage.setItem("key", "value");

// 读取数据
var lastname = localStorage.getItem("key");
var lastname = sessionStorage.getItem("key");

// 删除数据
localStorage.removeItem("key");
sessionStorage.removeItem("key");

// 删除所有已保存数据
localStorage.clear();
sessionStorage.clear();

// 返回存储中第 n 个键的名称。
localStorage.key(0)
sessionStorage.key(1);
```
