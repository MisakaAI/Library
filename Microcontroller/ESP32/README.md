# ESP32

- [ESP-IDF](./ESP-IDF.md)
- [Micro Python](./micropython.md)
- [Thonny](https://thonny.org/)

## 功能模块

- [boot](./src/boot.py)
- [main](./src/main.py)
- [LED](./src/led.py)
- [SD卡](src/sdcard.py)
- [Wi-fi 热点](./src/wifi_ap.py)
- [MicroPyServer](./src/micropyserver.py)
    - [index.html](./src/index.html)
    - [utils](./src/utils.py)
    - [路由](./src/route.py)
- [串口读取](./src/uart.py)
- [串口发送](./src/sender.py)
- [低功耗蓝牙](./src/ble.py)
- 看门狗

## 使用说明

*注：`.bat` 脚本未经过测试，仅供参考*

### 烧录 MicroPython 固件

烧录 MicroPython 固件，参考 [Micro Python](./micropython.md)

```sh
# 擦除 Flash
esptool --port /dev/ttyUSB0 erase-flash
# 烧录固件
esptool --port /dev/ttyUSB0 --baud 460800 write_flash 0 ESP32_GENERIC_S3-20250911-v1.26.1.bin
```

### 预编译

交叉编译为 `.mpy` 文件可以实现：

1. 更快的加载速度，省去了在设备上的编译步骤
2. 运行时占用更少 RAM
3. 一定程度上的代码混淆（但不是加密）

```sh
# Windows
.\build.bat

# Linux
./build.sh
```

### 使用 ampy 上传到 ESP32

将 `dist` 目录下的全部文件，上传到ESP32中。
可以使用 `ampy`或 [Thonny](https://thonny.org/)进行上传。
基于 `ampy` 的上传脚本 `upload.sh` 或 `upload.bat` （需要配置端口后使用）

```sh
## 安装 ampy
pip install adafruit-ampy

# Windows
.\upload.sh

# Linux
./upload.sh
```

## 参考文献

- [正点原子](http://www.openedv.com/docs/boards/esp32/ATK-DNESP32S3.html)
- [MicroPyServer](https://github.com/troublegum/micropyserver)
