# 零信任网络访问

Cloudflare Zero Trust 支持无缝、基于身份和上下文的应用程序访问和软件定义的安全性，使您能够在不牺牲性能或用户体验的情况下保护远程团队、设备和数据。

## 注册

[Zero Trust overview](https://one.dash.cloudflare.com/)

可选择免费的方案，需要有一张外币信用卡（Visa/Mastercard）

### 隧道 Networks / Tunnels

1. Create a tunnel
2. Cloudflared > Next
3. Tunnel name > Save tunnel
4. Choose your environment (选择操作环境)
    - Debian
    - 64-bit
5. Install and run a connector (安装并运行连接器)

    ```sh
    curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && 

    sudo dpkg -i cloudflared.deb && 

    sudo cloudflared service install <keys>

    # systemctl status cloudflared
    ```

6. Add public hostname (添加公共主机名)
7. 设置 `Subdomain`.`Domain`/`Path`
8. 设置 `Type` `://` `URL` (For example, https://localhost:8001)
9. Save hostname (保存主机名)
10. 注意：本机中 `Nginx` 要配置 `server_name` 为 `localhost`，且注意 `return 301` `error_page 497` 等配置
11. 目前没搞清楚 `https` 协议与 `Nginx` 的 `SSL` 相互作用的机理，建议先使用 `http` 协议

#### Example

`docker` 运行的 `qbittorrent` 使用的 Web 端口为 `8080`
则设置 `qb.example.com` 为 `http://127.0.0.1:8080`
之后直接访问 `http://qb.example.com` 即可通过隧道访问 `qbittorrent`
