import time
import serial

'''
pip install pyserial
'''

# 打开一个虚拟串口
ser = serial.Serial("COM8", 9600, timeout=1)

# Linux 测试
# ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

try:
    while True:
        # 获取当前时间并格式化
        data = time.strftime("%Y-%m-%d %H:%M:%S")
        # 在发送数据时，每条数据后添加换行符 \n，这样接收端使用 readline() 就能正确分隔每条数据：
        ser.write((data + "\n").encode('utf-8'))
        # 显示发送的数据
        print(f"已发送: {data}")
        # 每秒发送一次
        time.sleep(1)
finally:
    ser.close()
