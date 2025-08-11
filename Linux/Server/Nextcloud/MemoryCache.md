# 内存缓存

- [Memory caching](https://docs.nextcloud.com/server/28/admin_manual/configuration_server/caching_configuration.html)

## APCu

```sh
apt install php-apcu
```

修改 Nextcloud 配置，编辑文件 `config/config.php`

```php
<?php
$CONFIG = array (
  'memcache.local' => '\OC\Memcache\APCu',
);
```

```mods-available/apcu.ini
apc.enabled=1
apc.enable_cli=1
apc.shm_size=512M
```

## Redis

```sh
apt install -y redis-server
apt install -y php-redis
systemctl enable redis-server.service --now
usermod -aG redis www-data
```

编辑 `/etc/redis/redis.conf`

```conf
unixsocket /run/redis/redis-server.sock
unixsocketperm 770
maxmemory-policy allkeys-lru
```

编辑 `/etc/php/8.2/fpm/php.ini`

```ini
redis.session.locking_enabled=1
redis.session.lock_retries=-1
redis.session.lock_wait_time=10000
```

重启服务

```sh
systemctl restart redis-server.service
systemctl restart php8.2-fpm.service
systemctl restart nginx.service
```

修改 Nextcloud 配置，编辑文件 `config/config.php`

```php
<?php
$CONFIG = array (
  'memcache.locking' => '\OC\Memcache\Redis',
  'redis' => array(
  'host' => '/run/redis/redis-server.sock',
  'port' => 0,
  'timeout' => 0.0,
  ),
);
```