# 命令行工具

## 范例

```bash
# 获取名称空间
uals --url=opc.tcp://10.0.200.100:4840

# 列出 i=85 下全部的节点
uals -u=opc.tcp://10.0.200.100:4840 -n='i=85'

# 读取某个节点的值
uaread -u=opc.tcp://10.0.200.100:4840 -n='ns=1;s=D1234.产量'
```

## 命令

`uabrowse`
浏览OPC-UA节点并打印结果。

`uacall`
调用一个节点的方法。

`uaclient`
连接到服务器并启动Python shell，根节点和对象节点可用，命令行中指定的节点可作为mynode变量。

`uadiscover`
执行OPC UA发现并打印服务器和端点的信息。

`uageneratestructs`
从xml结构定义（.bsd）生成一个Python模块，节点参数通常是i=93的一个子节点。

`uahistoryread`
读取一个节点的历史。

`uals`
浏览OPC-UA节点并打印结果。

`uaread / uawrite`
读取/写入节点的属性，默认读取节点的值。

`uaserver`
运行一个OPC-UA服务器的例子。通过导入xml定义和使用uawrite命令行，甚至有可能使用这个服务器暴露真实数据。

`uasubscribe`
订阅一个节点并打印结果。