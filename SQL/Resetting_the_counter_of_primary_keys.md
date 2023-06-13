# 重置主键计数

```sql
-- 重置到1
ALTER SEQUENCE table_name_id_seq RESTART WITH 1;
```

```sql
-- 查找表中最大的主键值
SELECT MAX(id) FROM table_name;

-- 重置序列的值
ALTER SEQUENCE table_name_id_seq RESTART WITH (最大主键值 + 1);
```
