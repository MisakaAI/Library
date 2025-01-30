# 公网访问

## 编辑 `postgresql.conf` 文件

```conf
listen_addresses = '*'
```

## 编辑 `pg_hba.conf` 文件

```conf
# 局域网
host    all     all     192.168.0.0/24      md5

# 公网
host    all     all     0.0.0.0/24      md5
```

## 重新启动服务

```sh
systemctl restart postgresql.service
```
