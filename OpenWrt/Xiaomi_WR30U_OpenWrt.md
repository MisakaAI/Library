# 小米 WR30U 路由器刷 OpenWrt 指南

## Step 1 配置路由器

1. 将端口1设置为固定WAN口
2. 启用与智能网关的无线配置同步
3. 将Internet连接类型设置为`DHCP`，自动配置DNS

## Step 2 电脑配置网络

将计算机连接到可用的无线网络，并在无线网络适配器的属性上启用Internet连接共享。
找到 `控制面板\网络和 Internet\网络和共享中心`
查看` WLAN状态\属性\共享`
勾选 `允许其他用户通过此计算机的Internet连接来连接`，并在下面的家庭网络连接中选择 `以太网`

将计算机的有线网口，通过网线连接到路由器上的端口1。
此时，以太网的信息中，默认网关/DNS应该为`192.168.137.1`

## Step 3 使用 ssh 连接路由器

运行 `server_emulator.py` 并等待路由器找到连接。
（下载地址：[server_emulator.py](https://raw.githubusercontent.com/PatriciaLee3/wr30u_ssh/main/server_emulator.py)）

```powershell
python.exe server_emulator.py
```

等待大约一分钟后，当终端输出路由器的信息时，表示连接成功。按任意键继续。

```txt
Waiting for device
Device infomation:
{'vendor':'xiaomi',...}
Press any key to continue...
finish
```

使用 ssh 连接路由器，用户名`root`,密码`admin`

```powershell
ssh root@192.168.31.1
```

此步骤要使用`PowerShell`或者`cmd`，不能使用`WSL`，`WSL`会出现无法连接问题，原因不明。

看到 ARE U OK 则本步骤成功。

以上步骤以 [wr30u_ssh](https://github.com/PatriciaLee3/wr30u_ssh/) 为准。

## Step 4 刷入 uboot

去 hanwckf 仓库 [releases](https://github.com/hanwckf/bl-mt798x/releases/) 页面下载对应的 `uboot` 文件
将计算机的有线网口，通过网线连接到路由器上的端口2~4上。
通过 `scp` 将 `uboot` 传到路由器上。

```powershell
scp mt7981_wr30u-fip-fixed-parts-multi-layout.bin root@192.168.31.1:/tmp
```

`192.168.31.1` 为小米路由器默认的ip地址。

通过 `ssh` 登录路由器，并刷入`uboot`

```sh
# ssh 登录
ssh root@192.168.31.1

# 查看当前分区布局
# cat /proc/mt

# 将 uboot 刷入 FIP 分区
mtd write /tmp/mt7981_wr30u-fip-fixed-parts-multi-layout.bin FIP

# 关机
poweroff
```

## Step 5 进入 uboot

拔掉路由器电源，使用针或牙签等物品，按住重置键不放，再接上电源。
等待 10s 左右松开，路由器的系统灯变蓝后就是成功进入 `uboot` 了。

~~因 uboot 不支持 DHCP 功能，需要把电脑的 IP 地址设置成固定 IP：~~
~~电脑通过网线连接路由器，然后在网络设置里将以太网设置为静态，IP地址：192.168.31.100，子网掩码：255.255.255.0，网关：192.168.31.1，首选 DNS：192.168.31.1，最后保存~~

浏览器访问 `192.168.31.1`，不行的话，再试上面的手动配置IP。

## Step 6 刷入 OpenWrt

### 官方固件

[Techdata: Xiaomi WR30U](https://openwrt.org/toh/hwdata/xiaomi/xiaomi_wr30u)

- `Firmware OpenWrt Install URL` 的 `.ubi` 文件
- `Firmware OpenWrt Upgrade URL` 的 `.bin` 文件

选择文件后缀 `.ubi` 文件，然后点击 `upload`。
会刷入固件并且自动重启。

重启后进入`192.168.1.1`，如果这个ip和光猫的ip冲突，建议先拔掉WAN口网线进行配置。

默认用户名为`root`,密码`admin`。

此时刷入的固件为临时固件，找到 [System / Flash operations](http://192.168.1.1/cgi-bin/luci/admin/system/flash)
在底部的 `Flash new firmware image` 中，选择并刷入`.bin` 的固件。

路由器会再次重启，完成全部刷机工作。

#### 设置界面为中文

I'm Chinese !

更新软件列表：找到 `System / Software`，点击 `Update lists`。

查找 `luci-i18n-base-zh-cn` ，然后点击 `Install...` 进行安装。

通常刷新一下会自动变成中文界面，如果没变，在`System / System / Language and Style`中，调整 Language 为中文即可。

### 第三方固件

[潘多拉 QWRT MT7981 小米 WR30U 联通版](https://www.right.com.cn/forum/thread-8284824-1-1.html)

#### 网易UU游戏加速器

[OpenWrt插件安装百科](https://router.uu.163.com/app/html/online/baike_share.html?baike_id=5f963c9304c215e129ca40e8)

## DNS

1. **WAN口dns** 最常用的DNS设置方式。可以由DHCP请求获得，或自行设置。在静态IP的情况下，必须设置，否则无法查询外面的主机
2. **LAN 口dns** 如果路由器用于桥接方式，并且使用静态IP时，无法用DHCP请求的方式得到DNS，这是该选项的主要用途。其他场合下，则会忽略由DHCP服务器的DNS设置，改用这个设置。
3. **lan口DHCP通告** 如果该机器是子网的DHCP服务器，用于设置DHCP客户端的DNS。如果留空，默认则用自身的IP。通常客户端看到的DNS是这个（手机，电脑等）
4. **DHCP/DNS里的dns转发** 如果自己是子网的DNS服务器，用于设置转发服务器。如果不设置，则用上游DNS（由1或2）服务器

## 参考文献

- [【路由器】小米 WR30U 解锁并刷机](https://www.cnblogs.com/ywang-wnlo/p/WR30U.html)
- [OpenWrt：刷机小米WR30U（AX3000T）](https://zhuanlan.zhihu.com/p/659735701)
- [mt798x uboot 功能介绍](https://cmi.hanwckf.top/p/mt798x-uboot-usage/)
- [qust 首页/路由器/WR30U](https://share.qust.me/%E8%B7%AF%E7%94%B1%E5%99%A8/WR30U)
