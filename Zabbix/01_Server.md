# Server

- [安装说明](https://www.zabbix.com/documentation/6.0/zh/manual/installation/install_from_packages/debian_ubuntu)

## 安装软件源

Zabbix 前端需要 PHP 7.2 或更新的版本来启动 Zabbix 5.0。

- Ubuntu
- PostgreSQL
- Apache
- PHP

```bash
wget https://repo.zabbix.com/zabbix/6.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.0-4%2Bubuntu22.04_all.deb
dpkg -i zabbix-release_6.0-4+ubuntu22.04_all.deb
apt update
```

## 安装server/agent/前端

```bash
apt install zabbix-server-pgsql zabbix-frontend-php php8.1-pgsql zabbix-apache-conf zabbix-sql-scripts zabbix-agent
```

## 创建初始数据库，导入初始数据

```bash
# 在数据库主机上运行以下代码。
sudo -u postgres createuser --pwprompt zabbix
sudo -u postgres createdb -O zabbix zabbix
# 导入初始架构和数据，系统将提示您输入新创建的密码。
zcat /usr/share/zabbix-sql-scripts/postgresql/server.sql.gz | sudo -u zabbix psql zabbix
```

## 为Zabbix server配置数据库

编辑配置文件 `/etc/zabbix/zabbix_server.conf`

```bash
DBPassword=password
```

## 为Zabbix前端配置PHP

编辑 `zabbix_proxy.conf`

```bash
# vim /etc/zabbix/zabbix_proxy.conf
DBHost=localhost
DBName=zabbix
DBUser=zabbix
DBPassword=<password>
```

## 启动server/agent进程

```bash
systemctl restart zabbix-server zabbix-agent apache2
systemctl enable zabbix-server zabbix-agent apache2
```

## 配置Zabbix前端

- [Web界面安装](https://www.zabbix.com/documentation/6.0/zh/manual/installation/frontend)


Apache: http://<server_ip_or_name>/zabbix
Nginx: http://<server_ip_or_name>

默认用户名是Admin，密码zabbix。