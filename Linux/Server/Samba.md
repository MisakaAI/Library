# SAMBA

Samba文件服务器支持通过网络在不同的操作系统之间共享文件。

## 安装

```bash
apt install -y samba
```

## 创建共享目录

```bash
mkdir /home/username/sambashare
```

## 配置

编辑 `/etc/samba/smb.conf`

备份 `cp /etc/samba/smb.conf /etc/samba/smb.conf.bak`

```conf
[sambashare]
    comment = Samba on Ubuntu
    path = /home/username/sambashare
    read only = no
    browsable = yes
```

[global]
samba服务器的全局设置，对整个服务器有效。

workgroup
语法：workgtoup = <工作组群>;
预设：workgroup = MYGROUP
说明：设定 Samba Server 的工作组
例：workgroup = workgroup 和WIN2000S设为一个组，可在网上邻居可中看到共享。

server string
语法：server string = <说明>;
预设：sarver string = Samba Server
说明：设定 Samba Server 的注释
其他：支持变量 t%-访问时间 I%-客户端IP m%-客户端主机名 M%-客户端域名 S%-客户端用户名
例：server string = this is a Samba Server 设定出现在Windows网上邻居的 Samba Server 注释为 this is a Samba Server

hosts allow
语法：hosts aoolw = <IP地址>; ...
预设：; host allow = 192.168.1. 192.168.2. 127.
说明：限制允许连接到 Samba Server 的机器，多个参数以空格隔开。表示方法可以为完整的IP地址，如 192.168.0.1 网段，如 192.168.0.
例：hosts allow = 192.168.1. 192.168.0.1 表示允许 192.168.1 网段的机器网址为 192.168.0.1 的机器连接到自己的 samba server

printcap name
语法：printcap name = <打印机配置文件>;
预设：printcap name = /etc/printcap
说明：设定 samba srever 打印机的配置文件
例：printcap name = /etc/printcap 设定 samba srever 参考 /etc/printcap 档的打印机设定。

load printers
语法：load printers = <yes/no>;
预设：load printers = yes
说明：是否在开启 samba server 时即共享打印机。

printing
语法：printing = <打印机类型>;
预设：printing = lprng
说明：设定 samba server 打印机所使用的类型，为目前所支持的类型。

guest account
语法：guert account = <帐户名称>;
预设：   = pcguest
说明：设定访问 samba server 的来宾帐户(即访问时不用输入用户名和密码的帐户)，若设为pcguest的话则为默认为"nobody"用户。
例：guert account = andy 设定设定访问 samba server 的来宾帐户以andy用户登陆，则此登陆帐户享有andy用户的所有权限。

log file
语法：log file = <日志文件>;
预设：log file = /var/log/samba/%m.log
说明：设定 samba server 日志文件的储存位置和文件名(%m代表客户端主机名)

max log size
语法：max log size = <??KB>;
预设：max log size = 0
说明：设定日子文件的最大容量，单位KB 这里的预设值0代表不做限制。

security
语法：security = <等级>;
预设：security = user
说明：设定访问 samba server 的安全级别共有四种：
share---不需要提供用户名和密码。
user----需要提供用户名和密码，而且身份验证由 samba server 负责。
server--需要提供用户名和密码，可指定其他机器(winNT/2000/XP)或另一台 samba server作身份验证。
domain--需要提供用户名和密码，指定winNT/2000/XP域服务器作身份验证。

password server
语法：password server = <IP地址/主机名>;
预设：password server = <NT-Server-Name>;
说明：指定某台服务器(包括windows 和 linux)的密码，作为用户登入时验证的密码。
其他：此项需配合 security = server时，才可设定本参数。

password level
语法：password level = <位数>;
username level = <位数>;
预设：password level = 8

username level
username level = 8
说明：设定用户名和密码的位数，预设为8位字符。

encrypt passwords
语法：encrypt passwords = <yes/no>;
预设：encrypt passwords = yse
说明：设定是否对samba的密码加密。

smb passwd file
语法：smb passwd file = <密码文件>;
预设：smb passwd file = /etc/samba/smbpasswd
说明：设定samba的密码文件。

local master
语法：local master = <yes/no>;
预设：local master = no
说明：设定 samba server 是否要担当LMB角色(LMB负责收集本地网络的Browse List资源)，通常无特殊原因设为no

os level
语法：os level = <数字>;
预设：os level = 33
说明：设定 samba server的os level. os level从 0 到 255 . winNT的os level为33, win95/98的os level 是 1 .若要拿samba server 当LMB或DMB则它的os level至少要大于NT的33以上。

domain master
语法：domain master = <yes/no>;
预设：domain master = yes
说明：设定 samba server 是否要担当DMB角色(DMB会负责收集其他子网的Browse List资源)，通常无特殊原因设为no

preferred master
语法：preferred master = <yes/no>;
预设：preferred master = yes
说明：设定 samba server 是否要担当PDC角色(PDC会负责追踪网络帐户进行的一切变更)，通常无特殊原因设为no，(同一网段内不可有两个PDC,他们会每5分钟抢主控权一次)

wins support
语法：wins support = <yes/no>;
预设：wins support = yes
说明：设定samba server 是否想网络提供WINS服务，通常无特殊原因设为no。除非所处网络上没有主机提供WINS服务且需要此台samba server提供WINS服务是才设yes，其他 wins support 和 wins server 只能选择一个

wins server
语法：wins server = <IP地址>;
预设：wins server = w.x.y.z
说明：设定samba server 是否要使用别台主机提供的WINS服务，通常无特殊原因设为no。除非所处网络上有一台主机提供WINS服务才要设yes，其他 wins support 和 wins server
例：wins server = 192.168.0.1 表示samba server要使用192.168.0.1提供的WINS服务

#============================== Share Definitions =============================

[homes]
        comment = Home Directories
        browseable = no
        writable = yes
        valid users = %S

使用者本身的"家"目录，当使用者以samba使用者身份登入samba server 后，samba server 底下会看到自己的家目录，目录名称是使用者自己的帐号。

[printers]
        comment = All Printers
        path = /var/spool/samba
        browseable = no
        guest ok = no
        writable = no
        printable = yes

设置了samba服务器中打印共享资源的属性，samba服务器除了可以提供文件共享，还可以提供打印共享。

[分享的资源名称]
<指令1>; = (参数)
<指令2>; = (参数)

要提供分享资源时，须先把欲分享的资源以 [ ] 符号括住，底下通常会带指令和参数来表示此资源的设定和存取权限等，详情如下：

comment---------注释说明
path------------分享资源的完整路径名称，除了路径要正确外，目录的权限也要设对
browseable------是yes/否no在浏览资源中显示共享目录，若为否则必须指定共享路径才能存取
printable-------是yes/否no允许打印
hide dot ftles--是yes/否no隐藏隐藏文件
public----------是yes/否no公开共享，若为否则进行身份验证(只有当security = share 时此项才起作用)
guest ok--------是yes/否no公开共享，若为否则进行身份验证(只有当security = share 时此项才起作用)
read only-------是yes/否no以只读方式共享当与writable发生冲突时也writable为准
writable--------是yes/否no不以只读方式共享当与read only发生冲突时，无视read only
vaild users-----设定只有此名单内的用户才能访问共享资源(拒绝优先)(用户名/@组名)
invalid users---设定只有此名单内的用户不能访问共享资源(拒绝优先)(用户名/@组名)
read list-------设定此名单内的成员为只读(用户名/@组名)
write list------若设定为只读时，则只有此设定的名单内的成员才可作写入动作(用户名/@组名)
create mask-----建立文件时所给的权限
directory mask--建立目录时所给的权限
force group-----指定存取资源时须以此设定的群组使用者进入才能存取(用户名/@组名)
force user------指定存取资源时须以此设定的使用者进入才能存取(用户名/@组名)
allow hosts-----设定只有此网段/IP的用户才能访问共享资源
allwo hosts = 网段 except IP
deny hosts------设定只有此网段/IP的用户不能访问共享资源
allow hosts=本网段指定IP指定IP
deny hosts=指定IP本网段指定IP

## 系统服务

```bash
# 启动
systemctl start smbd.service
# 重启
systemctl restart smbd.service
# 开机启动
systemctl enable smbd.service
# 取消开机启动
systemctl disable smbd.service
```

## 设置用户帐户

使用的用户名必须属于系统帐户，否则不会保存。

```bash
smbpasswd -a username
```

常用参数：
-L 本地模式（必须是第一个选项）

-D LEVEL 调试级别
-r MACHINE 远程主机
-U USER 远程用户名
-c smb.conf 使用指定的smb.conf文件路径

-a 添加用户
-x 删除用户
-d 禁用用户
-e 启用用户
-n 设置无密码

### pdbedit

用于管理存储在sam数据库中的用户账户，只能由 root 运行。

```bash
# 列出当前所有已注册的 Samba 用户
pdbedit -L

# 列出Samba用户列表详细信息
pdbedit -Lv

# -a 新建账户
# -r 修改账户
# -x 删除账户
# -L 列出用户列表，读 passdb.tdb 数据库文件
# -v 列出用户列表详细信息
# -P 设置用户访问密码
```

## 访问

### Windows

打开文件管理器并将文件路径编辑为：`\\<ip-address>\sambashare`

### macOS

在Finder菜单中，单击 转到>连接到服务器 然后输入：`smb://<ip-address>/sambashare`

## Linux

```bash
# 匿名samba
mount -t cifs //ip-address>/sambashare /mnt/samba -o guest
# 非匿名samba
mount -t cifs //ip-address>/sambashare /mnt/samba -o username=samba,password=samba,iocharset=utf-8
```

## smb.conf

```conf
[global]
    # 工作组
    workgroup = MISAKANETWORK
    # 服务描述
    server string = Samba Server Version %v

    # 日志文件
    log file = /var/log/samba/log.%m
    # 单个日志文件的最大大小 （以KiB为单位）
    max log size = 1000
    # 文件
    logging = file

    # user ：使用 SAMBA 本身的密码数据库，密码数据库与底下的 smb passwd file 有关
    security = user
    # 用户后台类型
    passdb backend = tdbsam
    # 允许登录的主机
    hosts allow = 192.168.0.0/24

    # 关闭打印共享功能
    load printers = no
[homes]
        comment = Home Directories
        valid users = %S, %D%w%S
        browseable = no
        read only = yes
        inherit acls = yes

[public]
    # 描述
    comment = samba public
    # 目录
    path = /data
    # 是否只读
    read only = no
    # 是否可写
    writable = yes
    # 新创建的文件 预设权限为 0644
    create mask = 0644
    # 新创建的目录 预设权限为 0755
    directory mask = 0755
    # 开放给其他人浏览
    browseable = yes
    # 是否让所有可以登入的用户看到这个项目
    public = yes
    guest ok = yes
    # 指定能够进入到此资源的特定用户
    # 多用户或组使用逗号隔开，@group表示group用户组
    valid users = root
```

## 参考文献

- [Linux Samba服务主配文件smb.conf中文详解](https://www.cnblogs.com/fatt/p/5856892.html)
