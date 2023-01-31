# 基础数据库基本信息

```sql
-- 查询数据库版本信息
SELECT VERSION();

-- 查询数据库占用空间大小
SELECT pg_size_pretty(pg_database_size('table_name'));

-- 查看当前数据库所有表大小
SELECT relname, pg_size_pretty(pg_relation_size(relid))
FROM pg_stat_user_tables
WHERE schemaname='public'
ORDER BY pg_relation_size(relid) DESC;
```