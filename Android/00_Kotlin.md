# Kotlin

```Kotlin
fun main() {
    println("Hello, world!")
}
```

## 基础语法

### 变量和数据类型

- `String` 字符串
- `Int` 整数
- `Double` 小数
- `Float` 小数（不如 Double 精确），数字末尾带有 f 或 F。
- `Boolean` 布尔值

```Kotlin
fun main() {
    val x = 5
    val x: Int = 5
    println("Total: $x")

    x = 20
    println("Total: $x")

}
```

### 函数

```Kotlin
fun sum(a: Int, b: Int): Int {
    return a + b
}

fun main() {
    println(sum(3, 5))
}
```

### 类与实例

```Kotlin
class Rectangle(val height: Double, val length: Double) {
    val perimeter = (height + length) * 2
}
fun main() {
    val rectangle = Rectangle(5.0, 2.0)
    println("The perimeter is ${rectangle.perimeter}")
}
```

### 注释

```Kotlin
// 这是一个行注释

/* 这是一个多行的
   块注释。 */
```

## 条件表达式

```Kotlin
fun maxOf(a: Int, b: Int): Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}

fun maxOf(a: Int, b: Int) = if (a > b) a else b

fun main() {
    println("max of 0 and 42 is ${maxOf(0, 42)}")
}
```

### for 循环

```Kotlin
fun main() {
    val items = listOf("apple", "banana", "kiwifruit")
    for (item in items) {
        println(item)
    }
}

fun main() {
    val items = listOf("apple", "banana", "kiwifruit")
    for (index in items.indices) {
        println("item at $index is ${items[index]}")
    }
}
```

### while 循环

```Kotlin
fun main() {
    val items = listOf("apple", "banana", "kiwifruit")
    var index = 0
    while (index < items.size) {
        println("item at $index is ${items[index]}")
        index++
    }
}
```

### when 表达式

```Kotlin
fun describe(obj: Any): String =
    when (obj) {
        1          -> "One"
        "Hello"    -> "Greeting"
        is Long    -> "Long"
        !is String -> "Not a string"
        else       -> "Unknown"
    }

fun main() {
    println(describe(1))
    println(describe("Hello"))
    println(describe(1000L))
    println(describe(2))
    println(describe("other"))
}
```

### 区间

```Kotlin
// 使用 in 操作符来检测某个数字是否在指定区间内
fun main() {
    val y = 9
    if (x in 1..y+1) {
        println("fits in range")
    }
}

// 检测某个数字是否在指定区间外
fun main() {
    val list = listOf("a", "b", "c")

    if (-1 !in 0..list.lastIndex) {
        println("-1 is out of range")
    }
    if (list.size !in list.indices) {
        println("list size is out of valid list indices range, too")
    }
}

// 区间迭代
fun main() {
    for (x in 1..5) {
        print(x)
    }
}

// 数列迭代
fun main() {
    for (x in 1..10 step 2) {
        print(x)
    }
    println()
    for (x in 9 downTo 0 step 3) {
        print(x)
    }
}
```

### 集合

```Kotlin
// 对集合进行迭代
fun main() {
    val items = listOf("apple", "banana", "kiwifruit")
    for (item in items) {
        println(item)
    }
}

// 使用 in 操作符来判断集合内是否包含某实例
fun main() {
    val items = setOf("apple", "banana", "kiwifruit")
    when {
        "orange" in items -> println("juicy")
        "apple" in items -> println("apple is fine too")
    }
}

// 使用 lambda 表达式来过滤（filter）与映射（map）集合：
fun main() {
    val fruits = listOf("banana", "avocado", "apple", "kiwifruit")
    fruits
      .filter { it.startsWith("a") }
      .sortedBy { it }
      .map { it.uppercase() }
      .forEach { println(it) }
}
```

## 参考文献

- [Kotlin](https://kotlinlang.org/)
- [基本语法](https://book.kotlincn.net/text/basic-syntax.html)
