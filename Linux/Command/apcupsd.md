# apcupsd

## 安装

```sh
apt install apcupsd
```

## 查看USB连接情况

```sh
lsusb
# Bus 001 Device 038: ID 051d:0002 American Power Conversion Uninterruptible Power Supply
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
UPSNAME SER6Pro_UPS   # 在 UPSNAME 后面给个易懂的名字
UPSCABLE usb          # 使用USB线缆连接
UPSTYPE usb           # 指定UPS类型为USB通信
DEVICE                # 保持为空（自动检测）或设为/dev/usb/hiddev0
LOCKFILE /var/lock    # 确保守护程序可以创建锁定文件
```

### 关闭网络服务

```conf
NETSERVER off
```

## 启用

编辑 `/etc/default/apcupsd`，`systemd` 不需要

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
NETSERVER on

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

编辑 `/etc/apcupsd/appcontrol`

```sh
# 修改 doshutdown 的内容
doshutdown)
    <其他命令>
    ${SHUTDOWN} -h now "apcupsd UPS ${2} initiated shutdown"
;;
```

### 重启

```sh
systemctl restart apcupsd
```

## 检查 UPS 状态

使用 `apcaccess` 命令查看

### 基本信息

- **APC88**    : 通信协议和数据格式的信息
- **DATE**     : 报告生成的日期和时间
- **HOSTNAME** : 连接的主机名称
- **VERSION**  : 监控软件的版本
- **UPSNAME**  : 名称

### 连接与硬件信息

- **CABLE**    : 通过 USB 线缆连接到主机
- **DRIVER**   : 使用的是 USB UPS 驱动程序
- **UPSMODE**  : 工作在独立模式（Stand Alone），即没有与其他 UPS 并联或配置为主从关系
- **STARTTIME**: 监控软件的启动时间
- **MODEL**    : 型号
- **SERIALNO** : 序列号

### 运行状态

- **STATUS**   : 当前状态（`ONLINE`，表示它正在使用交流电源供电，电池未被使用。）
- **LINEV**    : 输入的交流电压
- **LOADPCT**  : 当前负载占 UPS 额定功率的百分比
- **BCHARGE**  : 电池充电状态
- **TIMELEFT** : 如果交流电源中断，电池可以支持当前负载运行时间
- **BATTV**    : 当前电池电压

### 电源转移与历史

- **LASTXFER** :最后一次电源转移（从交流电切换到电池）是由于自动或手动自检
- **NUMXFERS** :自 UPS 启动以来，切换到电池供电的次数
- **TONBATT**  :当前在电池供电上的时间
- **CUMONBATT**:累计使用电池供电的时间
- **XOFFBATT** :最后一次从电池供电切换回交流电的时间（`N/A` 为不适用，因为没有发生过电源切换）

### 设置与阈值

- **MBATTCHG** : 最小电池充电百分比，在电量低于此值时触发某些操作的阈值
- **MINTIMEL** : 最小剩余时间，表示电池剩余时间低于此值时会执行关机等动作
- **MAXTIME**  : 最大运行时间，表示没有设置最长运行时间限制
- **SENSE**    : 灵敏度设置，影响 UPS 对电压波动的反应速度
- **LOTRANS**  : 低转移电压
- **HITRANS**  : 高转移电压
- **ALARMDEL** : 报警延迟设置为无报警，不会发出警报声

### 标称参数

- **NOMINV**   : 标称输入电压
- **NOMBATTV** : 标称电池电压
- **NOMPOWER** : 标称输出功率，表示 UPS 的额定功率

### 自检与状态

- **SELFTEST-** :  自检结果
- **STATFLAG-** :  状态标志（十六进制数），代表 UPS 的内部状态位（具体含义需参考 APC 文档）。
- **BATTDATE-** :  电池安装或更换日期

### 结束信息

- **END APC-**  :  报告结束时间
