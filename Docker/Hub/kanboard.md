# kanboard

```sh
docker pull kanboard/kanboard:latest
docker run -d \
  --name kanboard \
  -p 1111:80 \
  -v /var/www/kanboard/data:/var/www/app/data \
  -v /var/www/kanboard/plugins:/var/www/app/plugins \
  --restart unless-stopped \
  kanboard/kanboard:latest
```

默认用户名 `admin`
默认密码 `admin`
