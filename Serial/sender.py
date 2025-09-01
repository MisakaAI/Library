import serial

'''
pip install pyserial
'''

# 打开配对的那个虚拟串口
ser = serial.Serial("COM9", 9600, timeout=1)

# Linux 测试
# ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

try:
    while True:
        # 接收数据
        received_data = ser.readline()
        if received_data:
            # 显示接收的数据
            print(f"接收到: {received_data.decode('utf-8').strip()}")
finally:
    ser.close()
