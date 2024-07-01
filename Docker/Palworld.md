# 幻兽帕鲁

```sh
docker run -d \
    --name palworld-server \
    -p 8211:8211/udp \
    -p 27015:27015/udp \
    -v ./palworld:/palworld/ \
    -e PUID=1000 \
    -e PGID=1000 \
    -e PORT=8211 \
    -e PLAYERS=16 \
    -e MULTITHREADING=true \
    -e RCON_ENABLED=true \
    -e RCON_PORT=25575 \
    -e TZ=UTC \
    -e ADMIN_PASSWORD="<ADMIN_PASSWORD>" \
    -e SERVER_PASSWORD="<SERVER_PASSWORD>" \
    -e COMMUNITY=false \
    -e SERVER_NAME="<服务器名称>" \
    -e SERVER_DESCRIPTION="<服务器说明>" \
    -e ALLOW_CONNECT_PLATFORM="Steam" \
    --restart unless-stopped \
    --stop-timeout 30 \
    thijsvanloef/palworld-server-docker:latest
```

## 参考文献

- [palworld-server-docker](https://github.com/thijsvanloef/palworld-server-docker)
