# python-miio

用于控制使用小米的 `miIO` 及 `MIoT` 协议。

## 安装

```bash
pip install git+https://github.com/rytilahti/python-miio.git
```

## 使用

### 获取令牌

```sh
miiocli cloud
Username: example@example.com
Password:

== name of the device (Device offline ) ==
    Model: example.device.v1
    Token: 00000000000000000000000000000000
    IP: 192.168.xx.xx (mac: ab:cd:ef:12:34:56)
    DID: 123456789
    Locale: cn
```

### 获取通用信息

```sh
miiocli device --ip <ip> --token <token> info
```

### 控制现代（MIoT）设备

```sh
# [设备状态] status 将显示当前设备状态，以及接受的设置值（标记为访问RW）
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 status

# [更改设置] set
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 set light:brightness 0

# [行动] actions
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 actions

# [执行] call 执行 actions 获取的行动
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 call light:toggle

# [帮助] help
```

### API

```py
from miio import DeviceFactory

dev = DeviceFactory.create("<ip address>", "<token>")
dev.status()    # 对设备执行 info 查询以检测型号。
dev.sensors()   # 获取传感器信息。
dev.settings()  # 获取有关可更改的可用设置的信息。
dev.actions()   # 返回有关可用设备操作的信息。
```

## 设备

- [米家空气净化器 4 MAX](zhimi.airp.sa4.py)
- [米家智能侧吸油烟机S1](viomi.hood.v12.py)
- [小米智能多模网关2](lumi.gateway.mcn001.py)
- [领普智能平移推窗器WD1](linp.wopener.wd1lb.py)

## 参考文献

- [Github](https://github.com/rytilahti/python-miio)
- [官方文档](https://python-miio.readthedocs.io/en/latest/)
- [小米/米家产品库 - Xiaomi Miot Spec](https://home.miot-spec.com/)
