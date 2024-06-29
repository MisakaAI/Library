# 树莓派配置U盘启动

`Raspberry Pi 5`, `Raspberry Pi 4`, `400`, `Compute Module 4`, `Compute Module 4S` 使用 `EEPROM` 启动系统。
所有其他型号的树莓派都使用位于 `boot` 文件系统中的 `bootcode.bin` 文件。

## 更新引导加载程序配置

引导加载程序的 `default` 版本代表最新的出厂默认固件映像。
它更新以提供关键错误修复，硬件支持，并在 `latest` 版中测试功能后定期更新。
`latest` 引导加载程序更新更频繁，包括最新的修复和改进。

高级用户可以切换到 `latest` 引导加载程序以获得最新的功能。

```sh
raspi-config
# - Advanced Options
# - Bootloader Version
# - Latest
```

设置完成后会要求重启，重启后更新系统。

```sh
apt update
apt upgrade
```

然后就可以更新你的 `bootloader` 了

```sh
sudo rpi-eeprom-update -a
sudo reboot
```

运行`sudo rpi-eeprom-update`，现在应该看到 CURRENT 日期已更新为最新版本的引导加载程序。

## 读取当前引导加载程序配置

查看当前正在运行的引导加载程序所使用的配置

```sh
rpi-eeprom-config
```

## 从引导加载程序映像读取配置

```sh
rpi-eeprom-config pieeprom.bin
```

然后将树莓派镜像烧录进U盘。

## 参考文献

- [Raspberry Pi boot EEPROM](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-boot-eeprom)
- [树莓派4B配置U盘启动](https://www.quarkbook.com/?p=638)
