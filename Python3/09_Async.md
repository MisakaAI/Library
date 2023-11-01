# 异步编程 Asyncio

## 区分同步与异步

同步（Sync）：同步世界中，事件一次只发生一个。
调用一个函数时，你的程序只能等待它完成，然后继续做下一件事情。

异步（Async）：在异步世界中，多个事情可以同时发生。
当启动一个操作或调用一个函数时，程序将会继续运行，你可以执行其他操作或调用其他函数，而不只是等待异步函数执行完成。
一旦异步函数完成了工作，程序就可以访问异步函数的执行结果。

**异步是最终目的，多线程、多进程、协程等都是中间手段。**

## 参考文献

- [Python并发、并行编程概念篇：并行VS并发、同步VS异步](https://zhuanlan.zhihu.com/p/537188524)
- [python并行编程之Asyncio](https://zhuanlan.zhihu.com/p/537203065)