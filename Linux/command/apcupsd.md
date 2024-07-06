# apcupsd

## 安装

```sh
apt install apcupsd
```

## 备份配置文件

```sh
cp /etc/apcupsd/apcupsd.conf /etc/apcupsd/apcupsd.conf.bak
cp /etc/default/apcupsd /etc/default/apcupsd.bak
```

## 配置

### 建立 USB 通信

编辑 `/etc/apcupsd/apcupsd.conf`

```conf
# 在 DEVICE 后为空，这样系统会自动检测 USB 连接 UPS
DEVICE
```

### 关闭网络服务

```conf
NETSERVER off
```

## 启用

编辑 `/etc/default/apcupsd`

ISCONFIGURED 是一个配置变量，用于指示 apcupsd 守护进程是否已经配置。

```txt
ISCONFIGURED=yes
```

## 配置文件说明

编辑 `/etc/apcupsd/apcupsd.conf`

UPSCABLE 和 UPSTYPE 选项，设置为对应的连接方式和设备类型。
ONBATTERYDELAY 选项，设置为多长时间后发送关机命令，单位为分钟。
BATTERYLEVEL 选项，设置为在电量低于多少百分比时发送关机命令。
MINUTES 选项，设置为在电源正常恢复前多长时间内禁止自动关机。

```conf
# 指定 UPS 名称
UPSNAME PowerGem
# 指定 UPS 连接的电缆/接口类型
UPSCABLE usb
# 指定 UPS 的类型
UPSTYPE usb
# 指定 UPS 的设备路径
DEVICE /dev/usb/hiddev0
# 指定一个锁文件的路径，用于 apcupsd 管理并发访问 UPS 的控制。
LOCKFILE /var/lock
# 指定 apcupsd 使用的脚本存放目录的路径。
SCRIPTDIR /etc/apcupsd
# 指定电源故障事件脚本的存放目录路径。
PWRFAILDIR /etc/apcupsd
# 指定禁止登录时的配置文件路径。
NOLOGINDIR /etc
# 设置 UPS 进入电池供电模式后，系统等待多少秒后触发相应的动作。
ONBATTERYDELAY 6
# 设置 UPS 电池剩余电量的阈值，当电池电量低于这个阈值时，系统会触发相关动作。
BATTERYLEVEL 5
# 设置 UPS 可以提供电力的最短时间阈值。
MINUTES 3
# 设置 UPS 在掉电后等待重新启动的时间。
TIMEOUT 0
# 设置发送警告消息的时间间隔。
ANNOY 300
# 设置发送警告消息之间的最小时间间隔。
ANNOYDELAY 60
# 设置禁用登录时的处理。
NOLOGON disable
# 设置在系统关机之前等待的时间。
KILLDELAY 0
# 设置启用网络服务器功能，允许其他系统访问 apcupsd 的状态信息。
NETSERVER off
# 设置 apcupsd 网络服务器监听的 IP 地址。
NISIP 127.0.0.1
# 设置 apcupsd 网络服务器监听的端口号。
NISPORT 3551
# 设置事件记录的文件路径。
EVENTSFILE /var/log/apcupsd.events
# 设置事件文件的最大数量。
EVENTSFILEMAX 10
# 设置 UPS 的类型，这里是独立（standalone）类型。
UPSCLASS standalone
# 设置 UPS 的工作模式，这里设置为禁用（disable）。
UPSMODE disable
# 设置统计信息更新的时间间隔。
STATTIME 0
# 设置状态信息记录的文件路径。
STATFILE /var/log/apcupsd.status
# 设置是否记录统计信息日志，这里设置为关闭（off）。
LOGSTATS off
# 设置数据更新的时间间隔。
DATATIME 0
```

### 重启

```sh
systemctl stop apcupsd
```

## 检查 UPS 状态

使用 `apcaccess status` 命令查看

```text
APC: UPS 的型号和产品编号
DATE: 系统生成此输出的日期和时间，包括时区偏移。
HOSTNAME: 运行 apcaccess 命令的计算机名称。
UPSNAME: UPS 的名称。
CABLE: 连接 UPS 和计算机的电缆类型。
DRIVER: UPS 使用的驱动程序类型。
UPSMODE: UPS 的工作模式。
  - Stand Alone: 表示 UPS 正在独立工作，没有与其他 UPS 或服务器组成集群。
STARTTIME: UPS 启动时间。
MODEL: UPS 的型号。
STATUS: UPS 的当前状态。
LINEV: 输入电压。
LOADPCT: 负载百分比，当前负载占总容量的百分比。
BCHARGE: 电池剩余容量百分比。
TIMELEFT: 电池可以提供电力的剩余时间。
  - 在当前负载条件下，电池可以维持供电状态的剩余时间
MBATTCHG: 电池充电百分比。
MINTIMEL: 最短的电池供电时间。
ALARMDEL: 是否有警告声音。
  - No alarm: 没有警报声音触发。
BATTV: 电池电压。
SELFTEST: UPS 的自检结果。
```
