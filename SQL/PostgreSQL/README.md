# PostgreSQL

http://www.postgres.cn/docs/14/index.html

PostgreSQL是一种特性非常齐全的自由软件的对象-关系型数据库管理系统（ORDBMS）
是以加州大学计算机系开发的POSTGRES 4.2版本为基础的对象关系型数据库管理系统

## 目录

- [查询基本信息](01_base.sql)
- [备份](02_pgdump.md)
- [公网访问](03_public_access.md)

## 安装

这是最简单的方式。

```bash
apt install postgresql
```

如果只需要客户端。

```bash
apt install postgresql-client
```

或者使用新一点的版本，比如官方库的？

```bash
# Download
# https://www.postgresql.org/download/

# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql
```

## 安装完成后

PostgreSQL的数据库不能直接使用root账户登录。
一般来说，需要用`postgres`这个用户，这也是安装过程种会自动创建的系统用户。



我们使用`$`代表系统命令，使用`=>`代表在psql中的命令。

```bash

# 首先，切换到这个用户
$ su postgres
# 然后可以直接打开数据库
$ psql
```

然后就可以对数据库进行一些基本的操作啦！
除了SQL语句，PostgreSQL中还可以用一些反斜杠命令。

```sql
# 显示反斜杠命令的帮助 / show help on backslash commands
=> \?
# 有关SQL命令语法的帮助 / help on syntax of SQL commands, * for all commands
=> \h
# 退出psql  / quit psql
=> \q
# 链接到数据库 / connect to new database (currently "postgres")
=> \c
# 列出角色 / list roles
=> \du
# 列出数据库 / list databases
=> \l
# 列出表  / list tables
=> \dt
# 列出表、视图和序列访问权限 / list table, view, and sequence access privileges
=> \dp or \z
# 在shell中执行命令或启动交互式shell / execute command in shell or start interactive shell
=> \! [COMMAND]
# 显示或设置客户端编码 / show or set client encoding
=> \encoding [ENCODING]
# 显示当前连接的信息 / display information about current connection
=> \conninfo
# 安全地更改用户的密码 / securely change the password for a user
=> \password
```

通常来说，先用`\password`设置一个密码总是没错的。

## 访问数据库

psql是PostgreSQL交互终端。
所以，使用`psql`可以访问数据库。

除了切换到`postgres`这个用户，然后直接用`psql`打开数据库之外。
我们也还有一些其他的操作。

```bash
$ psql -d postgres -U postgres -h 127.0.0.1 -p 5432

# 用法:
  psql [OPTION]... [DBNAME [USERNAME]]
# 选项:
  -d, --dbname=DBNAME      要连接到的数据库名称 (默认值: "root")
  -U, --username=USERNAME  数据库用户名 (默认值: "root")
  -h, --host=HOSTNAME      数据库服务器主机或套接字目录 (默认值: "/var/run/postgresql")
  -p, --port=PORT          数据库服务器端口 (默认值: "5432")
```

### 配置文件

[文件位置](http://www.postgres.cn/docs/14/runtime-config-file-locations.html)

#### 主服务器配置文件

[postgresql.conf](http://www.postgres.cn/docs/14/runtime-config.html)

```conf
listen_addresses = 'localhost'
# 指定服务器在哪些 TCP/IP 地址上监听客户端连接。
# 特殊项'*'对应所有可用 IP 接口
# 0.0.0.0允许监听所有 IPv4 地址
# ::允许监听所有 IPv6 地址
# 如果列表为空，服务器将根本不会监听任何 IP 接口
# 默认是localhost，只允许建立本地 TCP/IP 环回连接

port = 5432
# 服务器监听的 TCP 端口，默认是 5432
```

#### 基于主机认证配置文件

[pg_hba.conf](http://postgres.cn/docs/14/auth-pg-hba-conf.html)

可以用`postgres`这个用户，使用`psql`直接访问数据库的原理是，认证方式为`peer`。
修改配置文件，便可以像其他sql那样，使用用户名密码登录了。

```conf
# /etc/postgresql/14/main/pg_hba.conf
local         DATABASE  USER  METHOD  [OPTIONS]
```

第一个字段是连接类型：

- "local" 是Unix域套接字
- "host" 是TCP/IP套接字（加密或不加密）
- "hostssl" 是一个经过SSL加密的TCP/IP套接字
- "hostnossl" 是一个未经SSL加密的TCP/IP套接字
- "hostgssenc" 是一个经过GSSAPI加密的TCP/IP套接字
- "hostnogssenc" 是一个未经GSSAPI加密的TCP/IP套接字

DATABASE 可以是 `all`，或者其他库的名字。
USER 可以是 `all`，或者其他用户的名字。
ADDRESS 指定记录匹配的主机，如果希望允许所有ip访问，就设置成`0.0.0.0/0`。
OPTIONS 是一组用于格式验证的选项，比如`peer` `trust` `md5` `scram-sha-256` 等

- trust
无条件地允许连接
- reject
无条件地拒绝连接
- scram-sha-256
执行SCRAM-SHA-256认证来验证用户的口令
- md5
执行SCRAM-SHA-256或MD5认证来验证用户的口令
- ident
通过联系客户端的 ident 服务器获取客户端的操作系统名，并且检查它是否匹配被请求的数据库用户名。Ident 认证只能在 TCIP/IP 连接上使用。当为本地连接指定这种认证方式时，将用 peer 认证来替代。
- peer
从操作系统获得客户端的操作系统用户，并且检查它是否匹配被请求的数据库用户名。这只对本地连接可用
- cert
使用 SSL 客户端证书认证

#### 用于用户名称映射的配置文件

[pg_ident.conf](http://www.postgres.cn/docs/14/auth-username-maps.html)
