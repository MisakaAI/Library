# NextCloud

- [Nextcloud 应用](./apps.md)
- [内存缓存](./MemoryCache.md)
- [OCC](./OCC.md)
- [版本更新](./update.md)
- [WebDAV](./WebDAV.md)
- [使用代理](./proxy.md)

## 下载

### Server

- [Server](https://download.nextcloud.com/server/releases/latest.zip)

### Desktop

- [Desktop](https://download.nextcloud.com/desktop/releases/)

### Mobile

- [Android](https://download.nextcloud.com/android/)

## 安装

```sh
# 安装依赖
apt install php-fpm php-pgsql php-curl php-xml php-gd php-json php-mbstring php-zip php-bz2 php-intl php-gmp php-apcu php-imagick php-bcmath

# 下载 & 解压
wget -O /var/www/nextcloud.zip https://download.nextcloud.com/server/releases/latest.zip
unzip /var/www/nextcloud.zip -d /var/www/
rm /var/www/nextcloud.zip
chown -R www-data:www-data /var/www/nextcloud
```

修改 `/etc/nginx/conf.d/nextcloud.conf`

- [Nextcloud in the webroot of NGINX](https://docs.nextcloud.com/server/latest/admin_manual/installation/nginx.html#nginx-webroot-example)

### 存储大于512MB的大文件

修改 `/etc/php/8.2/fpm/php.ini`

```php.ini
; 定义单个 PHP 脚本可分配的最大内存
memory_limit = 4G
; 义 PHP 解析请求数据（如 POST 或文件上传）的最大时间（秒）
max_input_time = 3600
; 定义单个 PHP 脚本的最长运行时间（秒）
max_execution_time = 3600
; 定义单个上传文件的最大大小
upload_max_filesize = 16G
; 定义通过 POST 方法提交数据的最大总大小
post_max_size = 16G
; 禁用输出缓冲，默认值为 4096（4KB 缓冲区），设为 0 表示直接输出内容到客户端
output_buffering = 0
```

修改 `/etc/php/8.2/fpm/pool.d/www.conf`

```www.conf
clear_env = no
```

修改 `/etc/php/8.2/mods-available/apcu.ini`

```apcu.ini
; 启用 APCu（Alternative PHP Cache User Cache）的用户缓存功能，用于缓存用户数据（如变量、对象等），提升应用性能。
apc.enabled=1
; 在 PHP CLI（命令行接口）模式下启用 APCu 缓存
apc.enable_cli=1
; 定义 APCu 使用的共享内存（Shared Memory）大小，用于存储缓存数据。
apc.shm_size=512M
```

修改 `/etc/php/8.2/mods-available/opcache.ini`

```opcache.ini
; 启用 OPcache 扩展，缓存预编译的 PHP 脚本字节码，显著提升 PHP 性能
opcache.enable = 1
; 分配 128MB 内存给 OPcache
opcache.memory_consumption=128
; # 提高字符串缓存
opcache.interned_strings_buffer=8
; 60秒检查文件更新
opcache.revalidate_freq=60
; CLI 模式下启用（可选）
opcache.enable_cli=1
```

重启服务应用变更

```sh
systemctl restart php8.2-fpm.service
systemctl restart nginx.service
```

修改 Nextcloud 配置，编辑文件 `config/config.php`

```.php
<?php
$CONFIG = array (
  // 管理员操作的受信任IP范围
  'trusted_domains' =>
  array (
    0 => '192.168.0.0/24',
  ),
  // 用于本地存储数据的内存缓存后端
  'memcache.local' => '\\OC\\Memcache\\APCu',
  // 某些后台作业每天仅运行一次，值1将仅在UTC上午01：00和UTC上午05：00之间运行这些后台作业。
  'maintenance_window_start' => 1,
  // 启用代理
  'proxy' => '127.0.0.1:7890',
  // 邮件相关
  'mail_smtpmode' => 'smtp',
  'mail_smtpsecure' => 'ssl',
  'mail_sendmailmode' => 'smtp',
  'mail_from_address' => '***REMOVED SENSITIVE VALUE***',
  'mail_domain' => '***REMOVED SENSITIVE VALUE***',
  'mail_smtptimeout' => 30,
  'mail_smtphost' => 'smtp.exmail.qq.com',
  'mail_smtpport' => '465',
  'mail_smtpauth' => 1,
  'mail_smtpname' => '***REMOVED SENSITIVE VALUE***',
  'mail_smtppassword' => '***REMOVED SENSITIVE VALUE***',
);
```

#### 邮件

管理设置 - 基本设置 - 后台任务 - 电子邮件服务器

- 发送模式 `SMTP`
- 加密 `SSL`
- 服务器地址 `smtp.exmail.qq.com`
- 服务器端口 `465`
- 身份认证 `开启`
  - [腾讯企业邮箱](https://exmail.qq.com/)
  - [常用邮件客户端软件POP/IMAP协议设置](https://open.work.weixin.qq.com/help2/pc/19886?person_id=1)
  - 邮箱设置 - 账户 - 客户端专用密码 - 生成新密码

#### AxiosError: Request failed with status code 400

出现该错误的原因是没有设置用户的电子邮件！！！
个人设置 - 个人信息 - 电子邮件

### 定时任务

管理设置 - 基本设置 - 后台任务 - Cron（推荐）

```sh
crontab -u www-data -e
```

```crontab
*/5  *  *  *  * php -f /var/www/nextcloud/cron.php
```

### 安装完成后需要执行一次的命令

```sh
# 修复维护命令
sudo -u www-data php occ maintenance:repair --include-expensive
# 添加数据库缺失的索引
sudo -u www-data php occ db:add-missing-indices

# 列出系统配置
sudo -u www-data php occ config:list system
# 查看 Nextcloud 版本
sudo -u www-data php occ -V
# 查看系统状态
sudo -u www-data php occ status

# Collabora Online
sudo -u www-data php -d memory_limit=512M occ app:install richdocumentscode
```

#### occ status

- installed: true 已成功安装并完成初始化配置
- version: 30.0.6.2 内部版本标识符
- versionstring: 30.0.6 对用户可见的标准版本号
- edition: 标识 Nextcloud 的发行版类型，此处为空表示您使用的是**社区版**
- maintenance: false Nextcloud 未处于维护模式
- needsDbUpgrade: false 数据库结构与当前版本兼容，无需升级。若为 `true` 需要手动执行 `occ upgrade`
- productname: Nextcloud 产品名称，固定为 Nextcloud（用于区分衍生版本或分支）
- extendedSupport: false 未启用扩展支持服务

# 