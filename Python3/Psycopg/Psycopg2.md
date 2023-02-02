# Psycopg 2

虽然说有 Psycopg3 了，但是 Django 目前只支持到2。
所以还是得有点了解吧。

[pypi](https://pypi.org/project/psycopg2/)
[psycopg2](https://www.psycopg.org/docs/)

## 安装

```sh
# Python3 & pip
apt install python3
apt install python3-pip

# Postgresql
apt install postgresql

# psycopg2 二进制
# 二进制包是开发和测试的实用选择，但在生产中建议使用从源代码构建的包。
pip install psycopg2-binary

# psycopg2
# 从源代码构建，所以需要先安装 libpq-dev 和 python3-dev
apt install python3-dev libpq-dev
pip install psycopg2
```

## 使用

```python
import psycopg2

# 打开数据库连接
conn = psycopg2.connect("dbname=test user=postgres")

# 也可以使用：
# conn = psycopg2.connect(dbname="test", user="postgres", password="secret")

# 基本连接参数包括：
# dbname – 数据库名称（database是过时的别名）
# user – 用于身份验证的用户名
# password – 用于身份验证的密码
# host – 数据库主机地址（如果未提供，则默认为UNIX套接字）
# port – 连接端口号（如果未提供，则默认为5432）

# 将连接设置为自动提交模式：这样，所有执行的命令将被立即提交，并且不可能回退。
db.autocommit = True

# 创建游标对象
cur = conn.cursor()

# 执行SQL语句
cur.execute("sql 语句")

# 查询数据库并获取Python对象形式的数据

# 获取查询结果集的下一行，返回单个元组，或在没有更多数据可用时返回 None
cur.fetchone()

# 获取查询结果的下一组行，返回元组。当没有更多行可用时，将返回空列表
# 下面例子中为返回 2 行数据
cur.fetchmany(2)

# 获取查询结果的所有（剩余）行，并将它们作为列表返回元组。
cur.fetchall()

# 提交对数据库的更改
# 如果设置了自动提交，可以省略这一步
conn.commit()

# 关闭与数据库的通信
cur.close()
conn.close()
```
