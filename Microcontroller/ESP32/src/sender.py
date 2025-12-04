# Sender
# 通过串口发送数据

import uos
import time
import machine
from machine import UART, Pin

# UART
TX = 17
RX = 18
uart = UART(1, baudrate=115200, tx=TX, rx=RX, rxbuf=1024, txbuf=8192)


# SD 卡初始化
def init_sd():
    try:
        sd = machine.SDCard(slot=2, width=8, sck=12, miso=13, mosi=11, cs=2)
        vfs = uos.VfsFat(sd)
        uos.mount(vfs, "/sd")
        print(f"挂载 SD 后的系统目录:{uos.listdir()}\n{uos.listdir('/sd')}")
        return sd
    except Exception as e:
        print("SD 挂载失败:", e)
        return None


# 挂载 SD 卡
sd = init_sd()

# 日志文件
filename = f"/sd/send_log_{len(uos.listdir('/sd'))}.txt"


# LED
# 初始化LED
class LED:
    def __init__(self, pin, value=1):
        """
        LED
        :param pin: GPIO引脚编号
        :param value: 初始值，1为高电平（灭），0为低电平（亮）
        """
        self.led = Pin(pin, Pin.OUT, value=value)

    def on(self):
        """打开LED（低电平）"""
        self.led.value(0)

    def off(self):
        """关闭LED（高电平）"""
        self.led.value(1)

    def value(self, val=None):
        """设置或获取LED状态"""
        if val is not None:
            self.led.value(val)
        return self.led.value()

    def toggle(self):
        """切换LED状态"""
        self.led.value(not self.led.value())

    def blink(self, duration=500, times=1):
        """
        LED闪烁
        :param duration: 闪烁间隔时间（毫秒）
        :param times: 闪烁次数
        """
        for _ in range(times):
            self.toggle()  # 切换状态（亮→灭 或 灭→亮）
            time.sleep_ms(duration)
            self.toggle()  # 切换回原状态
            time.sleep_ms(duration)


led = LED(1, value=1)


def run():
    if sd is None:
        return
    # 主循环
    try:
        with open(filename, "a") as f:
            while True:
                msg = b"MCU+123456789\r\n"
                uart.write(msg)
                f.write(msg)
                f.flush()
                led.toggle()
                time.sleep(0.05)  # 20Hz
    except Exception as e:
        print("SD 写入错误:", e)


# 当作为主模块运行时，启动系统
if __name__ == "__main__":
    run()
