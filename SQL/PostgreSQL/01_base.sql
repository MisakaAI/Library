-- 查询数据库版本信息
SELECT
    VERSION();

-- 查询某个数据库占用空间大小
-- 先生，\l+ 了解一下
SELECT
    pg_size_pretty(pg_database_size('database_name'));

-- 查看当前数据库中所有表大小
-- 为什么不试试神奇的 \dt+ 呢？
SELECT
    relname,
    pg_size_pretty(pg_relation_size(relid))
FROM
    pg_stat_user_tables
WHERE
    schemaname = 'public'
ORDER BY
    pg_relation_size(relid) DESC;

-- 查看表的字段名、类型、非空、注释
SELECT
    a.attname AS 字段名,
    format_type(a.atttypid, a.atttypmod) AS 类型,
    a.attnotnull AS 非空,
    col_description(a.attrelid, a.attnum) AS 注释
FROM
    pg_class AS c,
    pg_attribute AS a
WHERE
    a.attrelid = c.oid
    AND a.attnum > 0
    AND c.relname = '表名';