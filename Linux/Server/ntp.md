# 时间同步服务器

## systemd-timesyncd

当系统安装后，只要安装时网络畅通，则 Debian 会自动配置 systemd-timesyncd 并与 Debian 的官方时间服务器同步。

要增加 NTP 服务器，需要修改 `/etc/systemd/timesyncd.conf`

保存更改后，

```bash

# NTP=ntp.aliyun.com ntp1.aliyun.com ntp2.aliyun.com ntp3.aliyun.com ntp4.aliyun.com ntp5.aliyun.com ntp6.aliyun.com
sed -i "s/#NTP=/NTP=ntp.aliyun.com ntp1.aliyun.com ntp2.aliyun.com ntp3.aliyun.com ntp4.aliyun.com ntp5.aliyun.com ntp6.aliyun.com/g" /etc/systemd/timesyncd.conf
# 重启 systemd-timesyncd 服务
systemctl restart systemd-timesyncd

# 验证配置
timedatectl show-timesync --all

# 查看状态使用
timedatectl timesync-status
```

## NTP

NTP 是一种广泛使用的时间同步协议，采用 Marzullo 算法来确保在网络中实现高度准确的时间同步。
它通过使用多个参考时钟源（如GPS接收器或原子钟）来计算和校准时间。
NTP通常用于需要非常高精度时间同步的应用，例如科学实验、金融交易等。

## Chrony

Chrony 也是一个时间同步工具，但它采用不同的算法来实现更快速和精确的时间同步。
Chrony 使用一种称为"容忍性选择算法"的技术，可以在不同网络条件下更快地调整系统时钟，并且对于系统启动时的时间同步较为友好。
Chrony 适用于大多数常见的时间同步需求，尤其是对于桌面计算机、服务器和普通网络应用而言。

### 安装

```bash
dnf install -y chrony
```

### NTP 服务器配置

```bash
vi /etc/chronyd.conf
# 添加阿里云NTP服务器
pool ntp1.aliyun.com iburst
pool ntp2.aliyun.com iburst
pool cn.pool.ntp.org iburst
# 允许指定网段访问此时间服务器，不然只允许本地网络
allow 172.16.0.0/16

# 设置时区为亚洲/上海
timedatectl set-timezone Asia/Shanghai

# 配置防火墙，也可以设置允许123/UDP端口
firewall-cmd --add-service=ntp
firewall-cmd --runtime-to-permanent

# 重启时间服务 & 查看服务启动状态
systemctl restart chronyd && systemctl status chronyd

# 设置开机自启动
systemctl enable chronyd

# 验证工作是否正常
[root@localhost ~]# chronyc sources
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
^* 120.25.115.20                 2  10   347   815    -54us[  -65us] +/- 4415us
^- 203.107.6.88                  2  10   377   192  -5352us[-5352us] +/-   30ms
^- ntp5.flashdance.cx            2  10   245   725   -858us[ -858us] +/-  173ms
^- tock.ntp.infomaniak.ch        1  10   377   521  +1361us[+1361us] +/-  106ms
^- ntp.wdc1.us.leaseweb.net      2  10   375    91   +409us[ +409us] +/-  229ms
^- time.cloudflare.com           3  10   375   109  +1262us[+1262us] +/-  107ms
```

### NTP 客户端配置

```bash
# 安装chrony服务
dnf install -y chrony

# 就像`ntpdate`命令一样，我们可以使用`chronyd`命令手动将Linux服务器的时间与远程NTP服务器进行同步。
[root@outline ~]# chronyd -q 'server 172.16.11.141 iburst'
2022-12-02T06:55:47Z chronyd version 3.4 starting (+CMDMON +NTP +REFCLOCK +RTC +PRIVDROP +SCFILTER +SIGND +ASYNCDNS +SECHASH +IPV6 +DEBUG)
2022-12-02T06:55:47Z Initial frequency -9.614 ppm
2022-12-02T06:55:51Z System clock wrong by -0.000004 seconds (step)
2022-12-02T06:55:51Z chronyd exiting

# 配置服务器参数
vi /etc/chrony.conf
server 172.16.11.141 iburst

# 重启时间服务 & 查看服务启动状态
systemctl restart chronyd && systemctl status chronyd

# 设置开机自启动
systemctl enable chronyd
```

### 验证 chrony 的同步

```bash
# 在服务器端查看有哪些客户端通过此NTP服务器进行时钟同步
[root@localhost ~]# chronyc clients
Hostname                      NTP   Drop Int IntL Last     Cmd   Drop Int  Last
===============================================================================
172.16.11.188                 275      0  10   -  1076       0      0   -     -

# 验证系统时间是否已使用chrony同步
[root@outline ~]# chronyc tracking
Reference ID    : AC100B8D (172.16.11.141)
Stratum         : 4
Ref time (UTC)  : Fri Dec 02 07:01:43 2022
System time     : 0.000000019 seconds fast of NTP time
Last offset     : -0.000016983 seconds
RMS offset      : 0.000016983 seconds
Frequency       : 9.614 ppm slow
Residual freq   : -1.633 ppm
Skew            : 0.089 ppm
Root delay      : 0.006188698 seconds
Root dispersion : 0.001516752 seconds
Update interval : 2.0 seconds
Leap status     : Normal

# 检查chrony来源，列出有关chronyd使用的当前时间源的信息
[root@outline ~]# chronyc sources
210 Number of sources = 1
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
^* 172.16.11.141                 3   6    37    39   +765ns[  +94us] +/- 4682us

# 列出有关chronyd使用的每个源的漂移速度和偏移估计的信息
[root@outline ~]# chronyc sourcestats  -v
210 Number of sources = 1
                             .- Number of sample points in measurement set.
                            /    .- Number of residual runs with same sign.
                           |    /    .- Length of measurement set (time).
                           |   |    /      .- Est. clock freq error (ppm).
                           |   |   |      /           .- Est. error in freq.
                           |   |   |     |           /         .- Est. offset.
                           |   |   |     |          |          |   On the -.
                           |   |   |     |          |          |   samples. \
                           |   |   |     |          |          |             |
Name/IP Address            NP  NR  Span  Frequency  Freq Skew  Offset  Std Dev
==============================================================================
172.16.11.141               6   5   136     +0.306      3.073    +11us    42us

# 默认情况下，NTP 客户端每64秒执行一次时间同步。但是，您可以手动调整时钟而无需等待下一次同步轮询。
[root@outline ~]# chronyc makestep
200 OK
```

## 参考文献

- [时间同步](https://pan-xiao.gitbook.io/debian/config/ntp)
- [Rocky Linux 9 配置时间同步服务 chrony](https://rockylinux.cn/technical-blog/rocky-linux-9-pei-zhi-shi-jian-tong-bu-fu-wu-chrony.html)