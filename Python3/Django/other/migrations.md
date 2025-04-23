# 重置迁移

1. **备份数据与版本控制**：备份已有数据库与代码。

```sh
pg_dump -h localhost -U postgres -d <DB_NAME> \
    --no-owner \
    --compress=zstd \
    --create \
    --clean > "sql_$(date +\%Y\%m\%d).sql.zst"
```

2. **删除迁移文件**：移除各个应用下 `migrations/` 目录中除 `__init__.py` 以外的所有文件。

```sh
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
```

3. **清空或删除数据库**：不保留数据。

SQLite 可直接删掉 `db.sqlite3` 文件
PostgreSQL 操作方法如下：

```sh
psql -U postgres -h localhost -p 5432 -d postgres
```

```sql
DROP DATABASE <DB_NAME>;
CREATE DATABASE <DB_NAME>;
```

4. **清理迁移记录表**：保留数据。

```sh
psql -U postgres -h localhost -p 5432 -d <DB_NAME>

# 或者在 DB shell 中执行
# python manage.py dbshell
```

```sql
-- 全部应用
DELETE FROM django_migrations;
-- 单个应用
DELETE FROM django_migrations WHERE app='<app_name>';
```

5. **重新生成并应用迁移**：执行 `makemigrations` 生成新迁移，再用 `migrate`（或 `migrate --fake`）将其应用到目标数据库。

```sh
python manage.py makemigrations

python manage.py migrate  # 不保留数据
python manage.py migrate --fake  # 保留数据
```

`--fake` 参数可跳过实际执行 SQL，只在迁移表中记录，使得数据库仍保持原有结构，但迁移历史已与新文件对齐。
