# smartmontools

使用 S.M.A.R.T. 控制和监视存储系统

## 安装

```sh
apt install smartmontools
```

## 服务

```sh
# 开机启动
systemctl enable smartmontools.service
# 启动
systemctl start smartmontools.service
# 重启
systemctl restart smartmontools.service
```

## 使用

```sh
# 列出磁盘的名称，类型以及接口信息
smartctl --scan

# 检查磁盘的 Smart 功能是否启用
smartctl -i /dev/sda

# 启用磁盘的 Smart 功能
smartctl -s on /dev/sda

# 禁用磁盘的 Smart 功能
smartctl -s off /dev/sda

# 显示磁盘的详细 Smart 信息
smartctl -a /dev/sda

# 显示磁盘总体健康状况
smartctl -H /dev/sda

# 磁盘自检
# short测试将花费最多2分钟，而在long测试中没有时间限制，因为它会读取并验证磁盘的每个段
smartctl --test=short /dev/sda
smartctl --test=long /dev/sda
# smartctl --test=long /dev/sdb > /var/log/long.text

# 计算测试时间估值
smartctl -c  /dev/sda

# 查看磁盘的自检结果
smartctl -l selftest /dev/sda

# 显示磁盘错误日志
smartctl -l error /dev/sda
```

## 邮件

**[WARNING]** 本部分尚未经过测试

编辑 `/etc/smartd.conf`

```conf
/dev/sda -m ai@misaka.cn -M test
```

## 注释

```txt
严重警告（Critical Warning）：会显示控制器状态警告讯息，如果都显示 0x00 就表示没事；
温度（Temperature）：会显示当前 SSD 温度资讯；
可用备用空间（Available Spare）：SSD 剩余空间百分比；
可用备用临界值（Available Spare Threshold）：临界值全由厂商定义；
寿命百分比（Percentage Used）：目前 SSD 寿命百分比数值，具体取决于实际设备使用情况和厂商对设备寿命的预测；
资料读取（Data Units Read）：记录电脑从 SSD 读取 512 字节数据单元的总量，每 000 个单元记录一次，即这项 Raw 数据 1 的值等于 500KB；
资料写入（Data Units Read）：如上，就是写入总量；
主机读取命令（Host Read Commands）：主控收到的读取命令数量；
主机写入命令（Host Write Commands）：主控收到的写入命令数量；
控制器忙碌时间（Controller Busy Time）：主控忙于 I/O 命令的时间；
意外关机（Unsafe Shutdowns）：纪录不正常断电次数；
媒体和资料完整性错误（Media and Data Integrity Errors）：主控检测得到的未恢复的数据完整性错误次数；
错误资料纪录（Number of Error Information Log Entries）：主控总共收到的错误信息日志数量；

通常我们主要确认「寿命百分比（Percentage Used）」这项数值就好，通常达到 90% 以上就要额外注意。
```

## 常用命令

```sh
# 查询硬盘健康度
smartctl -H /dev/sda | grep 'overall-health'

# 查询固态硬盘寿命
smartctl -a /dev/nvme1 | grep 'Percentage Used'

# 查询固态硬盘写入量
smartctl -a /dev/nvme0 | grep 'Data Units Written'
```
