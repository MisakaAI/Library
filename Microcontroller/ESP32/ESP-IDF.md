# ESP-IDF

```sh
# 安装依赖
sudo apt-get install git wget flex bison gperf python3 python3-pip python3-venv cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0

# 获取 ESP-IDF
mkdir -p ~/esp
cd ~/esp
git clone -b v5.5.1 --recursive https://github.com/espressif/esp-idf.git

# 设置工具
cd ~/esp/esp-idf
export IDF_GITHUB_ASSETS="dl.espressif.cn/github_assets"

# 在 全局 Python 环境 下安装 ESP-IDF
# 不能在 虚拟环境 下安装 ESP-IDF
./install.sh esp32s3

# 设置环境变量
. $HOME/esp/esp-idf/export.sh

# 获取 MicroPython 源码
cd ~/esp
git clone https://github.com/micropython/micropython.git
cd micropython
git submodule update --init --recursive

# 构建 mpy-cross
cd mpy-cross
make

# 配置 ESP32-S3
cd ../ports/esp32
idf.py set-target esp32s3

# 配置工程
idf.py menuconfig
```

- [menuconfig 说明](./idf_menuconfig.md)

## 编译工程

```sh
idf.py -D MICROPY_BOARD=ESP32_GENERIC_S3 build

# 烧录到设备
idf.py -p PORT flash
idf.py -p /dev/ttyACM0 flash

# 擦除 flash
idf.py -p PORT erase-flash
idf.py -p /dev/ttyACM0 flash
```

## 参考文献

- [ESP-IDF](https://docs.espressif.com/projects/esp-idf/zh_CN/v5.5.1/esp32s3/get-started/linux-macos-setup.html)
