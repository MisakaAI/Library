# h5ai

[h5ai](https://larsjung.de/h5ai/)

## 依赖

```bash
# apt install zip
dnf install zip

# apt install ffmpeg
dnf install ffmpeg-free

# apt install imagemagick
dnf install ImageMagick

# apt install nginx
dnf install nginx

# apt install php-fpm php-common php-curl php-xml php-gd php-json php-mbstring php-zip php-pgsql php-bz2 php-intl php-smbclient php-gmp php-apcu php-imagick
dnf install -y php-fpm php-common php-curl php-xml php-gd php-json php-mbstring php-zip php-pgsql php-bz2 php-intl php-smbclient php-gmp php-apcu php-imagick
```

## 安装

```bash
# 切换到工作目录
cd /var/www/html/

# 下载
wget https://release.larsjung.de/h5ai/h5ai-0.30.0.zip

# 解压
unzip h5ai-0.30.0.zip
```

## 配置

```conf
location / {
    root   /var/www/html;
    index  index.html  index.php  /file/_h5ai/public/index.php;
}
```
