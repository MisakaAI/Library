# Wekan

- [Wekan](https://wekan.team/)
- [github](https://github.com/wekan/wekan)
- [Docker](https://github.com/wekan/wekan/blob/main/docs/Platforms/FOSS/Docker/Docker.md)

```bash
docker run -d --restart=always --name wekan-db mongo:5
docker run -d --restart=always --name wekan \
    --link "wekan-db:db" \
    -e "WITH_API=true" \
    -e "MONGO_URL=mongodb://wekan-db:27017/wekan" \
    -e "ROOT_URL=https://wekan.misaka.cn" \
    -p 2000:8080 wekanteam/wekan:latest
```

## 备份

- [Backup](https://github.com/wekan/wekan/wiki/Backup)

Backup to directory dump:

```sh
docker stop wekan-app
docker exec wekan-db rm -rf /data/dump
docker exec wekan-db mongodump -o /data/dump
docker cp wekan-db:/data/dump .
docker start wekan-app
```

Copy dump directory to other server or to your backup.

## 恢复

```sh
docker stop wekan-app
docker exec wekan-db rm -rf /data/dump
docker cp dump wekan-db:/data/
docker exec wekan-db mongorestore --drop --dir=/data/dump
docker start wekan-app
```
