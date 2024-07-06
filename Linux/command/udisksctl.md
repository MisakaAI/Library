# udisksctl

`udisksctl` 是一个用于管理磁盘和存储设备的命令行工具。

## 安装

```sh
apt install udisks2
```

## 使用

- 列出可用设备：`udisksctl status`
这会列出当前系统上所有可用的磁盘和分区。
- 挂载设备：`udisksctl mount -b /dev/sdx`
这会将指定的设备（例如 /dev/sdx）挂载到系统上的适当位置。
- 卸载设备：`udisksctl unmount -b /dev/sdx`
这会卸载指定的设备，使其从系统中断开。
- 格式化设备：`udisksctl format -t filesystem_type -b /dev/sdx`
这会将指定设备格式化为指定的文件系统类型（如 ext4、ntfs 等）。
- 显示设备详细信息：`udisksctl info -b /dev/sdx`
这会显示特定设备的详细信息，包括设备类型、容量、已使用空间等。
- 显示分区信息：`udisksctl status --block-device /dev/sdx`
- 关闭电源：`udisksctl power-off -b /dev/sdx`

```sh
#!/bin/bash
udisksctl unmount -b /dev/sdb1
udisksctl unmount -b /dev/sdc1
udisksctl power-off -b /dev/sdb
```
