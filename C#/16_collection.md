# 集合

## 非泛型集合

在 `System.Collections` 命名空间中。
使用的是 `object` 类型存储元素，因此可以存储任何类型的对象。
但这种集合缺乏类型安全，并且需要进行装箱和拆箱操作，性能不佳。

常见的非泛型集合类：

- `ArrayList`：动态数组，可以存储不同类型的对象。
- `Hashtable`：键值对集合，其中键和值都是 `object` 类型。
- `Queue`：先进先出（FIFO）的集合。
- `Stack`：后进先出（LIFO）的集合。

```cs
using System;
using System.Collections;

class Program
{
    static void Main()
    {
        ArrayList list = new ArrayList();
        list.Add(1);
        list.Add("hello");
        list.Add(true);

        foreach (var item in list)
        {
            Console.WriteLine(item);
        }
    }
}
```

## 泛型集合

在 `System.Collections.Generic` 命名空间中。
是 C# 2.0 引入的集合类型，提供类型安全和高性能的集合操作。
泛型集合类避免了非泛型集合中的装箱和拆箱操作，并且在编译时进行类型检查。

常见的泛型集合类：

- `List<T>`：类似于数组，但大小可以动态变化。
- `Dictionary<TKey, TValue>`：键值对集合，键和值的类型可以指定。
- `Queue<T>`：先进先出（FIFO）队列。
- `Stack<T>`：后进先出（LIFO）堆栈。
- `LinkedList<T>`：双向链表，支持高效的插入和删除操作。
- `HashSet<T>`：不允许重复元素的无序集合。

```cs
// List
// https://learn.microsoft.com/zh-cn/dotnet/api/system.collections.generic.list-1?view=net-8.0
List<int> numbers = new List<int> { 1, 2, 3 };
numbers.Add(4);
numbers.Add(2);
numbers.Remove(2);
numbers.Add(4);

foreach (var n in numbers)
{
    Console.WriteLine(n);
}

numbers.Capacity //  在需要调整大小之前可以存储的元素 List<T> 数
numbers.Count; //  实际位于 中的 List<T> 元素数

numbers.Add(T); // 将对象添加到 List<T> 的末尾。
numbers.Remove(T); // 从 List<T> 中删除特定对象的第一个匹配项。
numbers.Clear(); // 从 List<T> 中删除所有元素。
numbers.Contains(T) // 确定元素是否在 List<T> 中。
numbers.Find(Predicate<T>) // 搜索与指定谓词定义的条件匹配的元素，并返回整个 List<T> 中的第一个匹配项。
numbers.Insert(Int32, T) // 将元素插入指定索引处的 List<T>。
numbers.Sort() // 使用默认比较器对整个 List<T> 中的元素进行排序。
numbers.ToArray() // 将 List<T> 的元素复制到新数组。
numbers.ToString() // 返回一个表示当前对象的字符串。

// Dictionary
Dictionary<string, int> ages = new Dictionary<string, int>();
ages.Add("Alice", 25);
ages.Add("Bob", 30);

foreach (var kvp in ages)
{
    Console.WriteLine($"{kvp.Key}: {kvp.Value}");
}
```

## 并发集合

在 `System.Collections.Concurrent` 命名空间中。
并发集合是为多线程环境设计的集合，保证了线程安全，可以安全地在多个线程间进行读写操作。

常见的并发集合类：

- `ConcurrentDictionary<TKey, TValue>`：线程安全的键值对集合。
- `ConcurrentQueue<T>`：线程安全的先进先出队列。
- `ConcurrentStack<T>`：线程安全的后进先出堆栈。
- `BlockingCollection<T>`：支持线程间的阻塞和限量操作的集合。

```cs
using System.Collections.Concurrent;

ConcurrentDictionary<string, int> dict = new ConcurrentDictionary<string, int>();
dict.TryAdd("key1", 1);
int value = dict["key1"];
Console.WriteLine(value);
```

## 特殊集合

如 `System.Collections.Specialized` 中的集合。
提供了用于特殊情况的集合类型，如：

- `NameValueCollection`：一个键可以对应多个值的集合。
- `OrderedDictionary`：有序的键值对集合。
- `StringCollection`：专门用于存储字符串的集合。

这些集合通常用于特定的应用场景，如配置管理或 HTTP 请求头处理等。

## 常用的集合

- `List<T>` 泛型集合类，它是动态数组，允许按索引访问元素。
- `Dictionary<TKey, TValue>` 键值对集合，通过键来快速查找值。键不能重复，而值可以重复。
- `HashSet<T>` 不允许重复元素的集合，适用于快速判断元素是否存在。
- `Queue<T>` 先进先出的集合。可以使用 `Enqueue` 添加元素，使用 `Dequeue` 移除并返回队列的第一个元素。
- `Stack<T>` 后进先出的集合。可以使用 `Push` 添加元素，使用 `Pop` 移除并返回栈顶的元素。

```cs
// List<T>
List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
numbers.Add(6);      // 添加元素
numbers.Remove(3);   // 删除元素
int first = numbers[0]; // 通过索引访问

// Dictionary<TKey, TValue>
Dictionary<string, int> dict = new Dictionary<string, int>();
dict.Add("apple", 5);
dict.Add("banana", 3);
int value = dict["apple"]; // 通过键获取值

// HashSet<T>
HashSet<int> set = new HashSet<int> { 1, 2, 3 };
set.Add(2); // 不会添加重复的元素
bool exists = set.Contains(2); // 判断元素是否存在

// Queue<T>
Queue<int> queue = new Queue<int>();
queue.Enqueue(1);
queue.Enqueue(2);
int first = queue.Dequeue(); // 返回并移除第一个元素

// Stack<T>
Stack<int> stack = new Stack<int>();
stack.Push(1);
stack.Push(2);
int top = stack.Pop(); // 返回并移除栈顶元素
```
