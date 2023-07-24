# 通过 腾讯云 Python SDK 更新本机的 ipv6 地址

## 使用方法

```bash
docker build -t dnspod .
docker run --name dnspod --net="host" dnspod
```

```cron
*/10 * * * * docker start dnspod
```
