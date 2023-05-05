## Virtual Machines

RHEL 9 提供了虚拟化功能，它允许运行 RHEL 9 的机器 托管多个虚拟机(VM)，也称为客户机（guest）。
VM 使用主机的物理硬件和计算资源，在主机操作系统中作为用户空间进程运行一个独立的虚拟操作系统（客户机操作系统）。

换句话说，虚拟化功能使在一个操作系统中执行其他操作系统成为可能。

## 启用虚拟化

### 在 AMD64 和 Intel 64 中启用虚拟化

要求：

- Red Hat Enterprise Linux 9 已在主机中安装并注册。
- 您的系统满足以下硬件要求以作为虚拟主机工作：
  - 主机的构架支持 KVM 虚拟化。
  - 有以下最小系统资源可用：
    - 主机有 6 GB 可用磁盘空间，以及每个预期的虚拟机需要额外 6 GB 空间。
    - 主机需要 2 GB RAM，以及每个预期的虚拟机需要额外 2 GB。

```sh
# 查看系统是否支持KVM
lsmod | grep kvm

# 或者用下面的命令
# 如果返回一个大于 0 的数字，则表示 CPU 支持虚拟化。
grep -Eoc '(vmx|svm)' /proc/cpuinfo
```

```sh
# 安装虚拟化 hypervisor 软件包
dnf install qemu-kvm libvirt virt-install virt-viewer
# 启动虚拟化服务
for drv in qemu network nodedev nwfilter secret storage interface; do systemctl start virt${drv}d{,-ro,-admin}.socket; done
```

```sh
# 确认您的系统已准备好成为虚拟化主机
# 如果所有 virt-host-validate 检查返回 PASS 值，则您的系统已准备好创建虚拟机。
virt-host-validate
```

#### QEMU: Checking for secure guest support

在客户机内部运行。

```sh
# 安装 QEMU 客户机代理
dnf install qemu-guest-agent

# 启动 QEMU 客户机代理
systemctl start qemu-guest-agent
```

## 创建虚拟机

要创建虚拟机并启动其操作系统安装，请使用 virt-install 命令以及以下强制参数：

- 新机器的名称(`--name`)
- 分配的内存量(`--memory`)
- 分配的虚拟 CPU 数量(`--vcpus`)
- 所分配的存储的类型和大小(`--disk`)
- OS 安装源的类型和位置（`--cdrom` 或 `--location`）

```sh
virt-install \
# 名称 win11
--name win11 \
# 内存 16384 MiB
--memory 16384 \
# vCPU 8 个
--vcpus 8 \
# 硬盘 50 GiB
--disk size=50\
# 设置要安装的操作系统
--os-variant win11 \
# 系统安装镜像的位置
--cdrom /data/windows.iso

## 获得可用操作系统版本列表以及相应的选项
osinfo-query os
```

命令行的方式太麻烦了，建议直接用 [web 控制台](Cockpit.md) 管理虚拟机。

### Windows 虚拟机

您可以在 RHEL 9 主机上创建完全虚拟化的 Windows 机器，在虚拟机(VM)中启动图形 Windows 安装程序，并优化已安装的 Windows 虚拟机操作系统(OS)。
要创建虚拟机并安装 Windows 客户机操作系统，请使用 virt-install 命令或 RHEL 9 web 控制台。

如果要安装 Windows 11，必须在主机上安装 `edk2-ovmf`、`swtpm` 和 `libtpms` 软件包。


```sh
# 在主机中准备 virtio 驱动程序安装介质
dnf install virtio-win

# 在主机机器上安装 edk2-OVMF 软件包
dnf install edk2-ovmf

# 在主机机器上安装 vTPM 软件包
dnf install swtpm libtpms
```

```sh
# 将文件作为光盘添加到现有 Windows 虚拟机中。
# 关机状态下才可以挂载。
virt-xml <WindowsVM> --add-device --disk virtio-win.iso,device=cdrom
```

## 参考文献

- [配置和管理虚拟化](https://access.redhat.com/documentation/zh-cn/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/index)