# JavaScript 基础

## 数据

### 直接量

```js
'Hello World !'
```

### 变量

```js
// 定义一个变量
var a;
a = "Hello World";

// 直接对变量赋值
var a = "Hello World";
```

#### 变量类型

- `const` 常量，即不可修改的变量，且必须初始化，否则会报错。
- `var` 变量，如果不初始化会输出 `undefined`，不会报错。
- `let` 只在当前作用域中有效，函数内部使用 `let` 定义后，对函数外部无影响。

#### 声明变量类型

声明新变量时，可以使用关键词 `new` 来声明其类型。

```js
var a = new String;
var b = new Number;
var c = new Boolean;
var d = new Array;
var e = new Object;
```

## 数据类型

### 值类型

又称：原生数据类型 primitive type

- 字符串：`string`
  - 双引号 `"Hello"`
  - 单引号 `'World'`
- 数字：`number`
  - 负数 `-1`
  - 零 `0`
  - 整数 `1`
  - 小数 `3.14`
- 布尔值：`boolean`
  - 真 `true`
  - 假 `false`
- 无：`null`
- 未定义：`undefined`

#### 布尔值

每种数据都有对应的布尔值，为真 `true` 或假 `false`。
空字符串 `''` 为 `false`，非空字符串 `' '` 均为 `true`。
数字 `0` 为 `false`，其余数字 `1` `-1` 均为 `true`。
`null` 和 `undefined` 也代表 `false`

### 引用类型

又称：对象数据类型 object type

- 对象：Object
- 数组：Array
- 函数：Function

#### 对象

```js
// 定义一个对象
var a = {
    key:"value",
    键:"值"
};

// 在对象中增加新的数据
a.apple = "苹果";

// 直接读取对象中的数据
a.key
// 通过变量读取对象中的数据
var b = "key";
a[b]
```

#### 数组

```js
// 定义数组
var a = [];
var a = new Array();

// 数组元素数量
a.length;

// 添加元素到末尾
a.push("apple");

// 删除末尾元素
a.pop();

// 插入、删除或替换元素
var a = [1,2,3,4,5,6,7,8,9];
// 从0开始计数，删除第2位起的1个元素
a.splice(2,1); // a = [1, 2, 4, 5, 6, 7, 8, 9]

// 删除第2位起的3个元素，并插入11,22,33。
a.splice(2,3,11,22,33); // a = [1, 2, 11, 22, 33, 7, 8, 9]

// 数组转化为字符串
// 括号内为分隔元素的符号。
// 如果括号内为空，则默认为逗号。
var b = a.join(',');
```

#### 函数

- [函数](./02_function.md)

#### 复制对象

##### 浅拷贝（shallow copy）

只复制指向某个对象的指针，而不复制对象本身，新旧对象共享一块内存。

```js
var x = { a: 1 };

// 复制对象不能直接赋值
var x1 = x;
x1.a = 0;
x.a; // 0
x1.a; // 0

// 浅拷贝
var obj2 = Object.assign({}, x);
x2.a=0;
x.a; // 1
x2.a; // 0
```

##### 深拷贝（deep copy）

复制并创建一个一模一样的对象，不共享内存，修改新对象，旧对象保持不变。

```js
var x3 = { a: 0, b: { c: 0 } };

// 浅拷贝
var x4 = Object.assign({}, x3);
x4.b.c = 1;
x3.b.c; // 1
x4.b.c; // 1

// 深拷贝
var x5 = JSON.parse(JSON.stringify(x3));
x5.b.c = 2;
x3.b.c; // 1
x5.b.c; // 2
```

#### 查看数据类型

使用 `typeof()` 可以查看数据类型。

```js
var a;
var b = 1;
var c = 3.14;
var d = null;
var e = true;
var f = false;
var g = 'hello world';
var h = {};
var i = [];

typeof(a);
typeof(b);
...
typeof(i);
```

## 运算符

- 赋值：`=`
- 加：`+`
- 减：`-`
- 乘：`*`
- 除：`/`
- 余数：`%`
- 自增：`++`
- 自减：`--`

### 自增运算符

`++` 是自增运算符，为当前变量自增一个单位。
`++i` 表示先增加，再计算结果。
`i++` 表示先计算结果，再增加。

## 条件 if

```js
var a = 1;
var b = 0;
if ( a > b ) {
    console.log(true);
} else if ( a == b ) {
    console.log(null);
} else {
    console.log(false);
}
```

### 表达式与运算符

- [表达式与运算符](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Expressions_and_operators)

#### 相等运算符

```js
// 相等运算符
1 == '1' // true

// 严格相等运算符
1 === '1' // false
```

#### 三元运算符

`表达式?真执行:假执行`



## 循环 for / while

```js
// for循环：括号内为循环开始前执行、循环条件、循环之后执行
for (var i=0; i<10; i++) {
    console.log(i);
}

// while循环：括号内为循环条件。
var i = 0;
while (i<10) {
    console.log(i);
    i++;
}

// ES6 - of
var a = ["A","B","C","D","E","F","G"];
for (var i in a) { console.log(i) }; // 0,1,2,3,4,5,6
for (var i in a) { console.log(a[i]) }; // A,B,C,D,E,F,G
for (var i of a) { console.log(i) }; // A,B,C,D,E,F,G
```

## 常用方法

### 输出

- 输出到控制台:`console.log()`
- 输出到弹窗:`alert()` `confirm()` `prompt()`
- 输出到页面:`document.write()`

```js
console.log('Hello World!');
alert('Hello World!');
document.write("Hello World !");
```

#### 弹出框

在弹出框中换行使用 `\n`

```js
// 警告框
window.alert("Hello World!"); // 可以不带 windows 前缀，下同
alert("Hello World!");

// 确认框
confirm("sometext");

// 输入框
prompt("sometext","defaultText");
```

### 字符串

- 转化为字符串：`toString()`
- 转化为整数：`parseInt()`
`parseInt()` 方法还有基模式，可以把二进制、八进制、十六进制或其他任何进制的字符串转换成整数。
- 转化为浮点数：`parseFloat()`
- 匹配字符串：`indexOf()`
- 分割字符串：`split()`
- 字符串长度：`length`
- 字符串替换：`replace('替换字符','替换字符')`

```js
var a = 123456;
var b = a.toString(); // '123456'
var c = parseInt(b) // 123456
var d = parseInt('0xA',16) // 10

b.indexOf('1'); // 0
b.indexOf('0'); // -1

b.length; // 6

var pi = '3.1415926';
pi.split('.'); // ['3', '1415926']
var e = parseFloat(pi) // 3.1415926
```

## 日期

- 日期 `Date()`

## 参考文献

- 《JavaScript百练成仙》
- [JavaScript 教程](https://www.w3school.com.cn/js/index.asp)
