# 基本模块使用

基本的 Psycopg 用法。

```python
import psycopg

with psycopg.connect("dbname=test user=postgres") as conn:
    with conn.cursor() as cur:
        cur.execute("SQL语句")
        for record in cur:
            print(record)
        conn.commit()
```

## Connection

[Connection classes](https://www.psycopg.org/psycopg3/docs/api/connections.html#psycopg.Connection.connect)

```python

# 连接数据库
conninfo='host=localhost port=5432 dbname=mydb user=postgres password=postgres connect_timeout=10'
Connection.connect(conninfo='', *, autocommit=False, prepare_threshold=5, row_factory=None, cursor_factory=None, context=None, **kwargs)

# conninfo 连接信息
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING

# autocommit 自动提交
# prepare_threshold 连接的 prepare_threshold 属性的初始值
# row_factory 用于指定要创建的读取数据记录类型 默认值：~psycopg.rows.tuple_row()
# cursor_factory 连接的 cursor_factory
# context 初始适配器配置的上下文

# 关闭数据库连接
Connection.close()

```


## Cursor

[Cursor classes](https://www.psycopg.org/psycopg3/docs/api/cursors.html)

```python
# 此游标正在使用的连接
Cursor.connection

# 对数据库执行查询或命令
Cursor.execute("SQL 语句")

# 执行多个查询或命令
Cursor.executemany()

# 启动 COPY 操作并返回一个对象来管理它
Cursor.copy()

# 查询返回的数据的格式。
Cursor.format

# 返回当前记录集中的下一条记录
Cursor.fetchone()

# 返回当前记录集中的下一个size的数据
Cursor.fetchmany(size=0)

# 返回当前记录集中所有剩余的记录
Cursor.fetchall()

# 移到通过 executemany() 执行的下一个查询的结果集
# 或者如果 execute() 返回多个结果集，则移到下一个结果集。
Cursor.nextset()

# 描述当前结果集的对象
Cursor.description

# 上次执行的SQL命令的命令状态标记。
Cursor.statusmessage

# 受先前操作影响的记录数。
Cursor.rowcount

# 当前结果中要提取的下一行的索引。
Cursor.rownumber

# 关闭连接
Cursor.close()
```

## Shortcuts

the Connection objects exposes an execute() method, equivalent to creating a cursor, calling its execute() method, and returning it.

```python
# In Psycopg 2
cur = conn.cursor()
cur.execute(...)

# In Psycopg 3
cur = conn.execute(...)
```

The Cursor.execute() method returns self. This means that you can chain a fetch operation, such as fetchone(), to the execute() call:

```python
# In Psycopg 2
cur.execute(...)
record = cur.fetchone()

cur.execute(...)
for record in cur:
    ...

# In Psycopg 3
record = cur.execute(...).fetchone()

for record in cur.execute(...):
    ...
```

## Connection context

```python
# use the connection
with psycopg.connect() as conn:
    ... # use the connection

# It is roughly the equivalent of:
conn = psycopg.connect()
try:
    ... # use the connection
except BaseException:
    conn.rollback()
else:
    conn.commit()
finally:
    conn.close()
```