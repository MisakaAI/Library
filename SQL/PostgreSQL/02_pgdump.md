# 备份

`pg_dump [connection-option...] [option...] [dbname]`

选项参数:

-h host 或 --host=host：指定运行服务器的主机名。
-p port 或 --port=port：监听端口号，默认端口为5432。
-U username 或 --username=username：指定要连接的用户名。
-c 或 --clean：只对纯文本格式有意义。指定输出的脚本中是否生成清理该数据库对象语句（如drop table 命令）。
-C 或 --create：只对纯文本格式有意义。指定脚本中是否输出一条 create database 语句和连接到该数据库的语句。一般在备份的源数据库和目标数据库的名称一致时，才指定此参数。



```bash
pg_dump -h 192.168.0.120 -U postgres -C dbname > backup.sql
```
## 恢复

使用 `psql` 的 -f 参数进行导入

```bash
psql -h localhost -U postgres -f backup.sql
```