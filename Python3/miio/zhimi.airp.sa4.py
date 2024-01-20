# 米家空气净化器 4 MAX
# from miio import AirPurifierMiot
from miio import DeviceFactory

ip = '192.168.31.1'
token = '00000000000000000000000000000000'

# s = AirPurifierMiot(ip,token)
dev = DeviceFactory.create(ip, token)
print(dev.status())
print(dev.settings())
print(dev.actions())

# 直接设置
'''
# [开关] 开：True 关：False
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 set air-purifier:on True

# [模式] 自动 Auto 0 静音 Silent 1 风扇 Fan 3
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 set air-purifier:mode 0

# [风扇等级] 0 1 2 3
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 set air-purifier:fan-level 0
'''

# 模拟按键
'''
# 获取可用操作
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 actions
# 开关
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 call air-purifier:toggle
# 切换模式
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 call habit:mode-switch
# 风扇等级
miiocli genericmiot --ip 192.168.31.1 --token 00000000000000000000000000000000 call habit:fan-level-switch
'''

# from miio.integrations.zhimi.airpurifier import AirPurifierMiot
# from miio import AirPurifierMiot

# > airpurifier_miot.py
# > _MAPPINGS 添加一行
# > "zhimi.airp.sa4": _MAPPING_VB4,

# 连接设备
# s = AirPurifierMiot(ip,token)

# 开关
# s.on()
# s.off()

# s.status() # 设备状态

# # 设置模式
# s.set_mode(OperationMode.Auto)   # 自动
# s.set_mode(OperationMode.Silent) # 静音
# s.set_mode(OperationMode.Fan)    # 风扇

# # 设置风扇转速
# s.set_fan_level(0) # 1 （需要把源代码中限制level大于1小于3的限制取消）
# s.set_fan_level(1.5) # 1
# s.set_fan_level(1)   # 2
# s.set_fan_level(2)   # 3

# 设备状态 status
'''
nion=None                       # 负离子
aqi=10                          # 空气质量指数
average_aqi=None                # 平均气温
buzzer=True                     # 蜂鸣器
buzzer_volume=None              # 蜂鸣器音量
child_lock=False                # 儿童锁
fan_level=2                     # 风扇等级
favorite_level=None             # 最爱级别
favorite_rpm=None               # 最爱转速
filter_hours_used=0             # 过滤器使用小时数
filter_left_time=None           # 过滤器剩余时间
filter_life_remaining=100       # 过滤器剩余寿命
filter_rfid_product_id=None     # 过滤 RFID 产品 ID
filter_rfid_tag=None            # 过滤 RFID 标签
filter_type=None                # 过滤器类型
gestures=None                   # 手势
humidity=45                     # 湿度
is_on=False                     # 正在进行
led=None                        # 发光二极管
led_brightness=None             # 亮度
led_brightness_level=None       # 亮度级别
mode=OperationMode.Fan          # 模式
motor_speed=None                # 电机速度
pm10_density=None               # PM10 浓度
power=off                       # 电源
purify_volume=None              # 净化体积
temperature=20                  # 温度
tvoc=None                       # 总挥发性有机化合物
use_time=None                   # 使用时间
'''
