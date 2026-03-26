# MAVLink

[MAVLink](https://mavlink.io/zh/) （Micro Air Vehicle Link） 是一种轻量级、二进制通信协议，主要用于无人机（UAV）与地面站（GCS）、机载计算机之间的数据通信。

- 二进制格式（比 JSON/XML 更省带宽）
- 支持串口、UDP、TCP、无线电等多种链路
- 跨平台（C / Python / Java / JS 等）

## 协议结构（数据包格式）

核心：通过 MsgID 定义消息类型 + Payload 承载数据

字段|说明
-|-
STX|起始标志（0xFD）
LEN|payload 长度
Incompat Flags|不兼容标志
Compat Flags|兼容标志
Seq|包序号
SysID|系统 ID
CompID|组件 ID
MsgID|消息 ID
Payload|实际数据
Checksum|CRC校验
Signature（可选）|安全签名

## 目录

0. [安装 MAVLink 工具链](0.Install_MAVLink.md)
1. [本地双程序通信](1.Local_Dual-Program_Communication.md)
2. [自定义 dialect](2.Custom_dialect.md)
