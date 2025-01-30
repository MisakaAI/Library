# MariaDB

- [MariaDB](https://mariadb.org/)

MariaDB 数据库管理系统是 MySQL 的一个分支，主要由开源社区在维护，采用 GPL 授权许可。
MariaDB 的目的是完全兼容 MySQL ，包括 API 和命令行，使之能轻松成为 MySQL 的代替品。

## 安装

1. 安装依赖并导入密钥

```sh
sudo apt-get install apt-transport-https curl
sudo mkdir -p /etc/apt/keyrings
sudo curl -o /etc/apt/keyrings/mariadb-keyring.pgp 'https://mariadb.org/mariadb_release_signing_key.pgp'
```

2. 创建仓库配置文件

创建 `/etc/apt/sources.list.d/mariadb.sources`

```txt
# MariaDB 11 Rolling repository list - created 2025-01-30 02:43 UTC
# https://mariadb.org/download/
X-Repolib-Name: MariaDB
Types: deb
# deb.mariadb.org is a dynamic mirror if your preferred mirror goes offline. See https://mariadb.org/mirrorbits/ for details.
# URIs: https://deb.mariadb.org/11/debian
URIs: https://mirrors.tuna.tsinghua.edu.cn/mariadb/repo/11.rolling/debian
Suites: bookworm
Components: main
Signed-By: /etc/apt/keyrings/mariadb-keyring.pgp
```

3. 安装

```sh
sudo apt-get update
sudo apt-get install mariadb-server
```

## 连接器

- Python
  - [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/) MySQL 官方维护，性能较好，支持最新协议。
  - [PyMySQL](https://pypi.org/project/PyMySQL/) 社区维护，纯 Python 实现，兼容性好（适合无 C 编译环境）。
