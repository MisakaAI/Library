# Q & A

## 远程时卡在 “正在下载 VS Code 服务器”

在 VS Code 的设置中搜索 remote.serverDownloadBaseUrl，将其值改为国内镜像地址

```json
"remote.serverDownloadBaseUrl": "http://vscode.cdn.azure.cn"
```
