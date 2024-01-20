# 米家智能侧吸油烟机S1
from miio import DeviceFactory

ip = '192.168.31.1'
token = '00000000000000000000000000000000'

dev = DeviceFactory.create(ip, token)
print(dev.status())
print(dev.settings())

'''
# [开关] 开：True 关：False
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 set hood:on True

# [灯光] 开：True 关：False
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 set light:on True

# [延迟关闭] 开：True 关：False
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 set hood:off-delay True

# [延迟关闭时间] 1-7
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 set hood:off-delay-time 1

# [风扇等级] 低速 0 高速 1 爆炒 2
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 set fan-control:fan-level 0
'''