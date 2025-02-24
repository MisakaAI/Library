# 内存缓存

- [Memory caching](https://docs.nextcloud.com/server/28/admin_manual/configuration_server/caching_configuration.html)

## APCu

```sh
apt install php-apcu
```

```fpm/php.ini
'memcache.local' => '\OC\Memcache\APCu',
```

```mods-available/apcu.ini
apc.enabled=1
apc.enable_cli=1
apc.shm_size=512M
```

## Redis
