# Open WebUI

## with Docker

```sh
docker pull ghcr.io/open-webui/open-webui:main
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

访问 [http://localhost:3000/](http://localhost:3000/)

## 参考文献

- [Open WebUI](https://docs.openwebui.com/)
