# 查看 Linux 系统温度

## 直接读取系统文件

```bash
# 读取温度值
name=$(cat /sys/class/hwmon/hwmon0/name)
temp=$(cat /sys/class/hwmon/hwmon0/temp1_input)

# 将温度值转换为摄氏度
celsius=$(awk "BEGIN {printf \"%.2f\n\", $temp / 1000}")

# 输出文本
echo "$name: $celsius ℃"
```

## sensors

### 安装

```bash
# Ubuntu
apt install lm-sensors

# RHEL
dnf install lm_sensors
```

#### 初始化

在终端中运行 `sensors-detect` 命令，初始化。

传感器配置过程中出现一些问题，需要回答 `yes` 或 `no`，但是你可以通过参数 `--auto` 来使用默认的回答。

参数 ``--auto`` 在自动、非交互式模式下运行。
所有的问题会回答默认答案。
请注意这不一定是安全的，因为内部逻辑可能会导致程序尝试进行具有潜在危险的探测。

##### 警告

传感器检测需要访问用于大多数芯片检测的硬件。
根据定义，它在识别出芯片之前，它不知道有哪些芯片。
这意味着它可以访问以这些芯片不喜欢的方式使用芯片，导致从SMBus锁定到永久锁定等问题。
可能会导致硬件损坏（谢天谢地，这是一种罕见的情况。）

作者尽最大努力使检测尽可能安全，结果证明在大多数情况下都可以，但无法保证传感器检测不会锁定或杀死一个特定的系统。
因此，根据经验，**您不应该在生产服务器上运行传感器检测**，如果你负担不起更换系统的随机部分，你就不应该运行传感器进行检测。
而且建议不要强制执行默认情况下会跳过的检测步骤，除非您知道你在做什么。

## 使用

```bash
# 显示温度
sensors

# 仅显示 k10temp-pci-00c3 的温度
sensors | grep "k10temp-pci-00c3" -A 2

# 监控温度
watch sensors
```
