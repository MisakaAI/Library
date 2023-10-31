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

## 数据类型

### 原生数据类型 primitive type

- 字符串（单引号，双引号）：`'Hello'` `"World"`
- 整数：`-1` `0` `1`
- 小数：`3.14`
- 布尔值：`true` `false`
- 无：`null`
- 未定义：`undefined`

### 对象数据类型 object type

```js
// 定义一个对象
var a = {
    key:"value",
    键:"值"
};

// 在对象中增加新的数据
a.apple = "苹果";

// 直接读取对象中的数据
console.log(a.key);
// 通过变量读取对象中的数据
var b = "key";
console.log(a[b]);
```

#### 复制对象

##### 浅拷贝（shallow copy）

只复制指向某个对象的指针，而不复制对象本身，新旧对象共享一块内存。

```js
var x = { a: 1 };

// 复制对象不能直接赋值
var x1 = x
x1.a = 0
console.log(x.a) // 0
console.log(x1.a) // 0

// 浅拷贝
var obj2 = Object.assign({}, x);
x2.a=0
console.log(x.a) // 1
console.log(x2.a) // 0
```

##### 深拷贝（deep copy）

复制并创建一个一模一样的对象，不共享内存，修改新对象，旧对象保持不变。

```js
var x3 = { a: 0, b: { c: 0 } };

// 浅拷贝
var x4 = Object.assign({}, x3);
x4.b.c = 1
console.log(x3.b.c) // 1
console.log(x4.b.c) // 1

// 深拷贝
var x5 = JSON.parse(JSON.stringify(x3));
x5.b.c = 2
console.log(x3.b.c) // 1
console.log(x5.b.c) // 2
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

typeof(a)
typeof(b)
...
typeof(i)
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
}
```

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
```

## 数组

```js
// 定义数组
var a = [];
var a = new Array();

// 数组元素数量
a.length

// 添加元素到末尾
a.push("apple");

// 删除末尾元素
a.pop()

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
