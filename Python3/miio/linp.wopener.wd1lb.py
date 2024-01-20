# 领普智能平移推窗器WD1
from miio import Device

# 使用所连接的网关的IP及令牌
ip = '192.168.31.1'
token = '00000000000000000000000000000000'

# 连接网关
gw = Device(ip, token)

# 查询当前状态 get_properties
r = gw.send("get_properties", [{'did':'1089943179','siid':2,'piid':2}])

# 发送指令 set_properties

# 开窗
# miiocli device --ip 192.168.31.1 --token 00000000000000000000000000000000 raw_command set_properties "[{'did':'1089943179','value':1 ,'siid':2,'piid':1}]"
gw.send("set_properties", [{'did':'1089943179','value':1 ,'siid':2,'piid':1}])

# 关窗
# miiocli device --ip 192.168.31.1 --token 00000000000000000000000000000000 raw_command set_properties "[{'did':'1089943179','value':2 ,'siid':2,'piid':1}]"
gw.send("set_properties", [{'did':'1089943179','value':2 ,'siid':2,'piid':1}])

# 指定位置 开启30%
# miiocli device --ip 192.168.31.1 --token 00000000000000000000000000000000 raw_command set_properties "[{'did':'1089943179','value':30 ,'siid':2,'piid':3}]"
gw.send("set_properties", [{'did':'1089943179','value':30 ,'siid':2,'piid':3}])

# SIID: 2 (window-opener) 开窗器
# PIID:1 (motor-control) 电机控制 [写] 0 - Pause 暂停 1 - Open 开 2 - Close 关
# PIID:2 (current-position) 当前位置 [读] 范围: 0 ~ 100  步长: 1
# PIID:3 (target-position) 目标位置 [读写] 范围: 0 ~ 100  步长: 1
# PIID:5 (fault) 设备故障 [读] 0 - No Faults 无故障 1 - Motor Fault 电机故障 2 - Windows Obstructed 车窗受阻

# 参考文献
# https://home.miot-spec.com/spec?type=urn:miot-spec-v2:device:window-opener:0000A043:linp-wd1lb:1:0000C825
# https://sspai.com/post/68306
