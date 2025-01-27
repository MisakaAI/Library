# 代理

由于众所周知的原因，Nextcloud的插件需要使用代理服务器。

- [proxy](https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/config_sample_php_parameters.html#proxy)

打开 `config/config.php` 设置。

```php
'proxy' => '127.0.0.1:7890',
'proxyuserpwd' => 'user:pass',
'trusted_proxies' => array('172.16.0.200'),
; PHP 注释
```

`` 代理服务器
`` 可选身份验证
`trusted_proxies` 受信任的代理服务器列表
