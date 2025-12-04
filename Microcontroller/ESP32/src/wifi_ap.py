# Wifi AP
# 无线热点

import network


# 初始化 & 开启 Wifi 热点
def start_ap(ssid, password):
    wlan = network.WLAN(network.AP_IF)
    wlan.active(True)
    wlan.config(essid=ssid, password=password, authmode=network.AUTH_WPA2_PSK)
    print("Wi-Fi AP 启动:", wlan.ifconfig())
    return wlan


# 关闭 Wifi 热点
def stop_ap(wlan):
    wlan.active(False)
    print("Wi-Fi AP 已关闭")


if __name__ == "__main__":
    SSID = "MicroPython"
    PASSWORD = "12345678"
    start_ap(SSID, PASSWORD)
