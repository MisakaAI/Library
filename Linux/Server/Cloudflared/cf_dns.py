#!/usr/bin/env python3
# 获取当前网络公网 IP 地址，并更新到 Cloudflared

import requests

# 设置 API 请求的 URL 和头
url = "<要更新的域名>"
ZONE_ID = "<ZONE_ID>"
API_TOKEN = "<API_TOKEN>"

ip_sb_v4 = "https://api-ipv4.ip.sb/ip"  # IPv4
ip_sb_v6 = "https://api-ipv6.ip.sb/ip"  # IPv6

ip_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

cloudflare_api = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/"

cloudflare_headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}


# 获取 DNS 解析地址
dns_records_response = requests.get(cloudflare_api, headers=cloudflare_headers)
if dns_records_response.status_code == 200:
    dns_records = dns_records_response.json()
    for r in dns_records["result"]:
        if r["name"] == url:
            if r["type"] == "A":
                ip_response = requests.get(ip_sb_v4, headers=ip_headers)
            elif r["type"] == "AAAA":
                ip_response = requests.get(ip_sb_v6, headers=ip_headers)
            else:
                print(f'域名解析类型为 {r["type"]}，无法更新')
                exit(2)
            if ip_response.status_code == 200:
                ip = ip_response.text.strip()
                if r["content"] != ip:
                    data = {
                        "content": ip,
                        "name": url,
                        "proxied": False,  # 不使用 Cloudflared 代理
                        "type": r["type"],
                        "ttl": 1,
                    }
                    update_response = requests.patch(
                        cloudflare_api + r["id"],
                        headers=cloudflare_headers,
                        json=data,
                    )
                    if (
                        update_response.status_code == 200
                        and update_response.json()["success"]
                    ):
                        print("域名解析更新成功")
                        exit()
                    else:
                        print(
                            f"域名解析更新失败，状态码: {update_response.status_code}"
                        )
                        exit(update_response.status_code)
                else:
                    print("域名解析未变化")
                    exit()
            else:
                print(f"获取当前网络 IP 失败，状态码: {ip_response.status_code}")
                exit(ip_response.status_code)

else:
    print(f"获取域名解析状态失败，状态码: {dns_records_response.status_code}")
    exit(dns_records_response.status_code)
