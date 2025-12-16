# 虚拟串口软件

## 下载

- [com0com](https://sourceforge.net/projects/com0com/)

## 使用

`setupc.exe`

```sh
# 查看当前虚拟串口列表
list

# 安装虚拟串口 COM8 和 COM9
# install  PortName=串口名1 PortName=串口名2
install  PortName=COM8 PortName=COM9
```

COM8发送的数据，会被COM9接收。
COM9发送的数据，会被COM8接收。

## 测试程序

- [发送](sender.py)
- [接收](receiver.py)
