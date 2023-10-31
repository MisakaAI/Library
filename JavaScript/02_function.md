# JavaScript 函数

## 定义函数

```js
function f() {
    alert("Hello World !");
}

var a = function() {
    document.write("Hello World !");
}
```

## 传递参数

```js
// 固定参数
function add(a,b,c) {
    console.log(a+b+c);
}

add(1,2,3); // 6

// 不固定参数数量
// 参数默认放入 arguments 数组中
function add() {
    console.log(arguments);
    var a = 0;
    for (i in arguments){
        a = a + arguments[i];
        console.log(a,i);
    }
    console.log(a);
}

add(1,2,3,4,5); // 15
```

## 函数返回值

```js
function add(a,b,c) {
    var x = a+b+c;
    return x;
}

var n = add(1,2,3); // 6
```

### 闭包

外部函数将内部函数作为返回值 return 出去。

```js
function f() {
    var a = 0;
    return function(x) {
        a = a + x;
        console.log(a);
    }
}

var inner = f();

inner(1); // 1
inner(1); // 2
inner(1); // 3
```

### 自执行函数

经常搭配闭包进行使用。

```js
(
    function() {
        console.log(123);
    }
) ();

// 使用闭包的范例改为自执行函数

var inner = (function() {
        var a = 0;
        return function(x) {
            a = a + x;
            console.log(a);
        }
    }) ();
```

## 构造函数 new

**`this` 永远指向当前函数的调用者。**

```js
// 函数对象
function Fruit(name,smell,color) {
    this.name = name;
    this.smell = smell;
    this.color = color;
}

var apple1 = new Fruit('Apple','sweet','red')

// 约等于对象
var apple2 = {
    name: "Apple",
    smell: "sweet",
    color: "red"
};

```

## 回调函数 callback

把一个函数的定义作为参数传递给另外一个函数。

```js
function eat(food,callback) {
    callback(food);
}

eat('Apple',function(food) {
    console.log(food);
});

eat('Apple',function(food) {
    alert(food);
});
```
