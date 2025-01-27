# 挂载硬盘

## 查找硬盘的 UUID

```sh
blkid
```

## 手动挂载硬盘

```sh
mount /dev/sda1 /mnt/c
```

## 开机自动挂载硬盘

编辑 `/etc/fstab`

```fstab
UUID=1234-5678  /mnt/mydisk  ext4  defaults  0  2
```

1. `<file system>`：文件系统
    - 设备名 `/dev/sda1`
    - UUID `UUID=1234-5678`
    - 标签 `LABEL=mydisk`
    - 网络文件系统地址 `//server/share`
2. `<mount point>`：挂载点
    - `/mnt/mydisk`
3. `<type>`：文件系统类型
    - `ext4`
    - `xfs`
    - `vfat`
    - `nfs`
    - `ntfs`
4. `<options>`：挂载选项
    - `defaults`：使用默认挂载选项。
    - `ro`：只读挂载。
rw`：读写挂载。
    - `noexec`：不允许执行二进制文件。
    - `nosuid`：不允许设置用户 ID 位。
    - `nodev`：不解释设备文件。
    - `auto`：在启动时自动挂载。
    - `noauto`：在启动时不自动挂载。
    - `user`：允许普通用户挂载。
    - `nouser`：仅允许超级用户挂载。
5. `<dump>`：备份
是否在执行 `dump` 命令时备份此文件系统
    - `0`：不备份此文件系统。
    - `1`：备份此文件系统。
6. `<pass>`：文件系统检查顺序
**文件系统检查顺序**：此字段用于指定在系统启动时，fsck 工具检查文件系统的顺序。
    - `0`：不检查此文件系统。
    - `1`：首先检查此文件系统（通常用于根文件系统 /）。
    - `2`：其次检查此文件系统，其他所有文件系统通常都设置为 2。
