# Micro Python

## 首次使用

- **Windows** is `COM*`
- **Linux** 下为 `/dev/ttyUSB*` 或 `/dev/ttyACM*`

Linux 下需要执行的部分

```sh
# 添加当前用户串口权限
sudo usermod -aG dialout $USER

# 或者暴力一点直接设置权限
ls /dev/ttyUSB*
sudo chmod 777 /dev/ttyUSB0

ls /dev/ttyACM*
sudo chmod 777 /dev/ttyACM0
```

### 使用 esptool 烧录 MicroPython 固件

```sh
# 安装 esptool
python -m venv .esp32
source .esp32/bin/activate
pip install esptool

# 检查板子是否可用
esptool --port /dev/ttyUSB0 flash-id
esptool --port /dev/ttyACM0 flash-id

# 擦除 Flash
esptool erase-flash  # esptool 将尝试使用ESP32自动检测串行端口
esptool --port /dev/ttyUSB0 erase-flash
esptool --port /dev/ttyACM0 erase-flash

# 烧录固件
# https://micropython.org/download/ESP32_GENERIC_S3/
esptool --port /dev/ttyUSB0 --baud 460800 write_flash 0 ESP32_GENERIC_S3-20250911-v1.26.1.bin
esptool --port /dev/ttyACM0 --baud 460800 write_flash 0 ESP32_GENERIC_S3-20250911-v1.26.1.bin
```

### REPL

使用 [Thonny](https://thonny.org/) 连接到 REPL

1. 运行
2. 配置解释器
3. 解释器：Thonny 应该是应哪种解释器来运行您的代码
`Micropython(ESP32)`
4. 端口或WebREPL
`USB Serial(/dev/ttyUSB0)`

```sh
# 或使用 screen （退出需要 kill -9），建议使用 Thonny
screen /dev/ttyUSB0 115200
```

#### 手动更新时间

```py
# 需要用 Wi-Fi 连接网络
import ntptime
ntptime.host = "ntp.aliyun.com"  # 使用国内 NTP 服务器
ntptime.settime()

print("UTC:", time.time())
print("LOCAL:", time.localtime())
```

## 参考文献

- [micropython](http://micropython.com.cn/en/latet/esp32/quickref.html)
