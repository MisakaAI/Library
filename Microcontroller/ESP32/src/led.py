# LED
from machine import Pin
import time


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


if __name__ == "__main__":
    # 创建LED对象，初始化为高电平（灭）
    led = LED(1, value=1)

    # 使用blink方法实现闪烁
    while True:
        led.blink(duration=500, times=1)  # 闪烁一次，间隔500ms
