# 小米智能多模网关2
from miio import Gateway

ip = '192.168.31.1'
token = '00000000000000000000000000000000'
gw = Gateway(ip, token)

print(gw.ip)
print(gw.mac)
print(gw.devices)
