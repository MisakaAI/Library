# asyncua

opcua-asyncio 是一个基于 python-opcua 的 OPC UA 客户端和服务器，支持python3.7以上的版本。
异步编程允许更简单的代码（例如，更少地需要锁）和潜在的性能增益。

OPC UA 二进制协议的实现已经在许多不同的 OPC UA 栈上进行了测试。
API提供了一个低级接口来发送和接收所有UA定义的结构，以及允许在几行中编写服务器或客户端的高级类。在一个应用程序中很容易混合高级对象和低级UA调用。
大多数低级代码是从xml规范自动生成的。

## 安装

```sh
pip install asyncua
```

## 使用

- [获取命名空间索引](get_namespace.py)
- [获取指定 Node 下所有 Node 节点](get_children.py)
- [读取节点数据](read_value.py)

## 参考文档

- [opcua-asyncio](https://github.com/FreeOpcUa/opcua-asyncio)
- [Python opcua-asyncio Documentation](https://opcua-asyncio.readthedocs.io/en/latest/)
- [Python OPC-UA Documentation](https://readthedocs.org/projects/python-opcua/downloads/pdf/stable/)