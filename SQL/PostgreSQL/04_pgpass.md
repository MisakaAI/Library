# pgpass

对数据库的大多数访问，包括`psql`程序，都要通过`libpq`库。
这个库包括一个特性，如果你指定一个名为`.pgpass`的文件（或`PGPASSFILE`引用的文件），你可以把作为用户连接所需的密码放在那里。
这允许通过 cron 等机制自动执行日常管理任务。

## 文件的位置

- Linux: `~/.pgpass`
- Windows: `%APPDATA%\postgresql\pgpass.conf`

## 文件的格式

```conf
主机名:端口:数据库:用户名:密码
hostname:port:database:username:password
```

当密码包含冒号`:`时，必须用反斜杠`\:`进行转义。
字符 `*` 可以匹配任何字段中的任何值（密码除外）。
注：如果设置了环境变量`PGPASSWORD`，则不读取 `~/.pgpass` 文件.

Windows 7 64位上带空格的路径的PGPASSFILE值示例：
`set PGPASSFILE=C：\Program Files\someapp\pgpass.conf`

请注意，环境变量值不能使用`"`（双引号）

## 文件权限

```sh
chmod 600 ~/.pgpass   # Linux/macOS
```
