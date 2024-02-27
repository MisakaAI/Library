# 内存缓存

- [Memory caching](https://docs.nextcloud.com/server/28/admin_manual/configuration_server/caching_configuration.html)

## APCu

```sh
apt install php-apcu
```

```php
'memcache.local' => '\OC\Memcache\APCu',
```

## Redis
