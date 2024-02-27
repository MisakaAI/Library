# OCC

## 显示您的Nextcloud版本

```sh
sudo -u www-data php occ -V
```

## 修复数据库的索引

```sh
sudo -u www-data php occ db:add-missing-indices
```
