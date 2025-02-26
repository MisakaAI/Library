# nut

## 安装

```sh
apt install nut
```

- 和硬件交互: `upsdrvctl` + `ups.conf`
- 提供硬件状态的接口: `upsd` + `upsd.conf` / `upsd.users`
- 查询server的能力: `upsc`
- 特定情况下触发的脚本: `upsmon` + `upsmon.conf` / `upssched.conf`
- 查看监听日志 `upslog`

## 配置

### 设置 nut 的运行模式

编辑 `/etc/nut/nut.conf`

```conf
# nut 作为独立的系统运行
MODE=standalone
```

### 定义 UPS 设备和驱动程序

编辑 `/etc/nut/ups.conf`

```conf
[apc]
    driver = usbhid-ups
    port = auto
    desc = "APC UPS"
    ignorelb                            # 忽略 UPS 传来的低电量状态标志
    override.battery.runtime.low = -1   # 表示不使用剩余最大可运行时间触发 LOWBATT
    override.battery.charge.low = 50    # 设置电池电量低于 30% 时触发 LOWBATT
```

```sh
systemctl enable --now nut-server
systemctl restart nut-server
systemctl status nut-server

# 查看 ups 列表
upsc -L
# 查看 ups 信息
upsc apc@localhost
# 查询 ups 状态
upsc apc@localhost ups.status
```

- `ups.status`
  - `OL`: line power（使用外部供电）
  - `OB`: on battery （使用电池供电）
  - `LB`: low battery （电量低）

#### 直接扫描 UPS 并添加到 `ups.conf` 文件中

```sh
nut-scanner -q >> /etc/nut/ups.conf
```

### 创建 nut 用户

编辑 `/etc/nut/upsd.users`

```conf
[admin]
    password = PASSWORD
    actions = SET
    instcmds = ALL
```

### 监视 UPS 的状态

编辑 `/etc/nut/upsmon.conf`

```conf
# MONITOR <UPS名称>@<主机名> <UPS数量> <用户名> <密码> <模式>
MONITOR apc@localhost 1 admin PASSWORD primary
# SHUTDOWNCMD 关机命令
SHUTDOWNCMD "/sbin/shutdown -h +0"
# NOTIFYCMD 脚本
NOTIFYCMD /usr/sbin/upssched
# NOTIFYMSG <notify type> "message"
NOTIFYMSG ONLINE        "UPS %s 在线，使用交流电"
NOTIFYMSG ONBATT        "UPS %s 离线，进入电源模式"
NOTIFYMSG LOWBATT       "UPS %s 电池电量低，即将关机"
NOTIFYMSG SHUTDOWN      "自动注销和关机"
NOTIFYMSG FSD           "UPS %s 正在被主电源强制关闭"
NOTIFYMSG COMMOK        "UPS %s 建立通信"
NOTIFYMSG COMMBAD       "UPS %s 通信中断"
NOTIFYMSG REPLBATT      "UPS %s 电池损坏，需要更换"
NOTIFYMSG NOCOMM        "UPS %s 不可用"
NOTIFYMSG NOPARENT      "关闭系统的进程死亡（无法关闭）"
# NOTIFYFLAG <notify type> <flag>[+<flag>][+<flag>]
NOTIFYFLAG ONLINE       SYSLOG+WALL
NOTIFYFLAG ONBATT       SYSLOG+WALL
NOTIFYFLAG LOWBATT      SYSLOG+WALL+EXEC
```

- **MONITOR** 要监视的系统
  - <模式> `primary` 主
  - <模式> `secondary` 次
- **SHUTDOWNCMD** 关闭系统时运行此命令
- **NOTIFYCMD** 配置当 UPS 状态发生变化时要执行的脚本或命令
- **NOTIFYMSG** 发生某些事件时，由 upsmon 发送的消息
- **NOTIFYFLAG**
  - \<flag> `SYSLOG` 写入系统日志
  - \<flag> `WALL` 通过 `wall` 命令，给所有已登录的用户发送内容为 `NOTIFYMSG` 的消息
  - \<flag> `EXEC` 执行 `NOTIFYCMD` 中配置的脚本
  - \<flag> `IGNORE` 什么都不做

```sh
systemctl enable --now nut-monitor
systemctl restart nut-monitor
systemctl status nut-monitor
```

#### 

- **battery.charge**: 100
电池当前电量的百分比，100 表示电池已完全充电
- **battery.charge.low**: 95
当电池电量低于该值时，UPS 将进入 LOWBATT 状态
当前设置为 95，意味着当电池电量低于 95% 时，会触发低电量警告
- **battery.mfr.date**: 2024/06/18
电池的制造日期
- **battery.runtime**: 3618
电池的剩余运行时间，单位为秒
- **battery.runtime.low**: 120
电池电量低时剩余的运行时间阈值，单位为秒
- **battery.type**: PbAc
电池类型，`PbAc` 表示铅酸电池（Lead Acid）
- **battery.voltage**: 13.7
当前电池电压，13.7 伏特
- **battery.voltage.nominal**: 12.0
电池的额定电压，12.0 伏特
- **device.mfr**: American Power Conversion
设备的制造商
- **device.model**: Back-UPS BK650M2_CH
UPS 型号
- **device.serial**:
UPS 的序列号
- **device.type**: ups
设备类型
- **driver.name**: usbhid-ups
当前使用的 UPS 驱动程序
- **driver.parameter.pollfreq**: 30
驱动程序的轮询频率
- **driver.parameter.pollinterval**: 2
驱动程序的轮询间隔
- **driver.parameter.port**: auto
UPS 连接端口
- **driver.parameter.synchronous**: auto
驱动程序的同步设置
- **driver.version**: 2.8.0
驱动程序的版本号
- **driver.version.data**: APC HID 0.98
与 UPS 驱动相关的数据
- **driver.version.internal**: 0.47
驱动程序的内部版本号
- **driver.version.usb**: libusb-1.0.26 (API**: 0x1000109)
USB 驱动程序的版本
- **input.sensitivity**: medium
输入电源的灵敏度
- **input.transfer.high**: 266
当输入电压超过此阈值时，UPS 将启动保护模式
- **input.transfer.low**: 180
当输入电压低于此阈值时，UPS 将启动保护模式
- **input.voltage**: 228.0
当前的输入电压，228.0 伏特
- **input.voltage.nominal**: 220
输入电源的额定电压，220 伏特
- **ups.beeper.status**: disabled
UPS 的蜂鸣器状态 禁用
- **ups.delay.shutdown**: 20
在关机之前的延迟时间，20 秒
- **ups.load**: 4
当前 UPS 的负载百分比
- **ups.mfr**: American Power Conversion
UPS 的制造商
- **ups.mfr.date**: 2024/04/17
UPS 的制造日期
- **ups.model**: Back-UPS BK650M2_CH
UPS 型号
- **ups.productid**: 0002
UPS 产品 ID
- **ups.realpower.nominal**: 390
UPS 的标称实际功率
- **ups.serial**:
UPS 的序列号
- **ups.status**: OL CHRG
UPS 的当前状态
`OL` 表示在线状态（Online），`CHRG` 表示正在充电。
- **ups.test.result**: Done and passed
UPS 测试结果 `Done and passed` 表示最近的自检已通过
- **ups.timer.reboot**: 0
系统重启的定时器，当前为 0，表示没有设置重启定时
- **ups.timer.shutdown**: -1
系统关机的定时器，当前为 -1，表示没有设置关机定时
- **ups.vendorid**: 051d
UPS 的供应商 ID

## 当停电以后发生了什么？

1. UPS 断电并使用电池供电
1. UPS 电池电量即将耗尽（此时 `ups.status: OB LB`）
1. master `upsmon` 监听到这一事件，并且设置 `FSD(forced shutdown)` 的标识来告诉所有的 `slave` 准备关机
1. `slave` 收到 `FSB` 信号，它会：
    1. 触发 `NOTIFY_SHUTDOWN` 事件
    1. 等待 `FINALDELAY` 秒（一般来说5秒）
    1. 执行 `SHUTDOWNCMD` 脚本
    1. 断开与 `upsd` 的链接
1. master `upsmon` 最多等待 `HOSTSYNC` 秒（通常是15秒），让辅助系统断开与 upsd 的链接。
如果在这段时间后仍有任何连接，`upsmon` 就会停止等待并继续后续操作。
1. master 收到 `FSB` 信号，它会：
    1. 触发 `NOTIFY_SHUTDOWN` 事件
    1. 等待 `FINALDELAY` 秒（一般来说5秒）
    1. 创建名为 `POWERDOWNFLAG` 的文件（通常叫 `/etc/killpower`）
    1. 执行 `SHUTDOWNCMD` 脚本
    1. `init` 准备回收系统资源，关闭进程、卸载挂载等
1. `init` 执行关机的脚本。此时会去检查 `POWERDOWNFLAG` 文件，并告诉 UPS 关闭供电
1. 整个系统的电力供给完全停止
1. 随着时间推移，电力恢复，UPS 重新开启
1. 所有系统重启

## 参考文献

- [使用NUT控制UPS电源](https://lh-love.top/posts/technical/%E8%AE%BE%E7%BD%AEnutnetwork-ups-tools/)
