# 重置 ID 序列

## 生成重置序列的 SQL 语句

```sh
# 将 <app_name> 替换为应用名
python manage.py sqlsequencereset <app_name>
```

## 执行生成的 SQL

```sql
-- 将 <model_name> 替换为模型对应的表名
SELECT setval(pg_get_serial_sequence('"<myapp_mymodel>"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "<myapp_mymodel>";
```

## 通过管道直接执行

```sh
python manage.py sqlsequencereset myapp | python manage.py dbshell
```
