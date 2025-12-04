# UART
# 串口数据

"""
该模块提供了通过UART接口接收数据并将其记录到SD卡文件中的功能。
支持中断驱动的数据接收和缓冲写入机制，以提高效率并减少数据丢失的风险。
"""

import uos
import time
from machine import UART
from rtc import rtc_check


class UARTLogger:
    """UART日志记录器类

    该类负责处理UART数据接收、缓冲和写入文件的操作。
    使用中断机制确保及时处理接收到的数据，避免缓冲区溢出。
    """

    def __init__(self, uart: UART, sd_lock=None, led=None):
        """
        初始化UART日志记录器

        Args:
            uart (UART): UART实例，用于接收数据
            sd_lock (Lock, optional): 用于SD卡写入的线程锁，防止多线程冲突
            led (LED, optional): LED对象，用于指示写入状态
        """
        self.uart = uart  # UART实例
        self.led = led  # LED指示灯对象
        self.sd_lock = sd_lock  # SD卡线程锁
        self.buffer = bytearray()  # 数据缓冲区
        self.write_count = 0  # 写入计数器
        self.flush_interval = 50  # 文件刷新间隔(写入次数)
        self.file_size_limit = 1024 * 1024 * 100  # 文件大小限制（100MB）
        self.max_buffer_size = 8192  # 最大缓冲区大小

        # 自动生成初始文件名
        rtc = rtc_check()
        if rtc:
            # 如果RTC时间有效，则使用RTC时间作为文件名前缀
            self.base_name = f"/sd/{rtc}"
        else:
            # 如果RTC时间无效，则使用SD卡中文件数量作为文件名前缀
            existing = uos.listdir("/sd")
            self.base_name = f"/sd/{len(existing)}"

        # 初始文件序号为1
        self.file_index = 1
        self.filename = f"{self.base_name}_{self.file_index}.txt"
        self.file = open(self.filename, "wb")

    def _reinitialize(self):
        """
        重新初始化文件和相关状态
        用于异常恢复后重新开始记录
        """
        try:
            # 关闭当前文件（如果已打开）
            if hasattr(self, "file") and self.file:
                self.file.close()
        except Exception:
            pass

        # 重新生成文件名（使用当前时间或新的序号）
        rtc = rtc_check()
        if rtc:
            self.base_name = f"/sd/{rtc}"
        else:
            existing = uos.listdir("/sd")
            self.base_name = f"/sd/{len(existing)}"

        # 文件序号递增，避免覆盖
        self.file_index += 1
        self.filename = f"{self.base_name}_{self.file_index}.txt"

        # 重新打开文件
        self.file = open(self.filename, "wb")
        self.buffer = bytearray()  # 清空缓冲区
        self.write_count = 0  # 重置写入计数器

        print(f"重新初始化完成，新文件: {self.filename}")

    def _rollover_file(self):
        """
        文件滚动切换

        当当前文件大小达到限制时，关闭当前文件并创建一个新的文件继续写入。
        """
        self.file.flush()
        self.file.close()
        self.file_index += 1
        self.filename = f"{self.base_name}_{self.file_index}.txt"
        self.file = open(self.filename, "wb")

    def _log_error(self, error_line: bytes, info: str):
        """
        记录错误信息到错误日志文件

        Args:
            error_line (bytes): 出错的数据行
            info (str): 错误描述信息
        """
        if self.sd_lock:
            self.sd_lock.acquire()
        try:
            error_log = f"{self.base_name}_error.txt"
            with open(error_log, "a") as f:
                f.write(f"{time.time()},{info},{error_line}\n")
        finally:
            if self.sd_lock:
                self.sd_lock.release()

    def _write_line(self, line: bytes):
        """
        将校验通过的数据写入文件

        Args:
            line (bytes): 校验通过的数据行
        """
        if self.sd_lock:
            self.sd_lock.acquire()
        try:
            self.file.write(line + b"\n")
            self.write_count += 1
            # 达到刷新间隔时刷新文件缓冲区
            if self.write_count >= self.flush_interval:
                self.file.flush()
                self.write_count = 0
        finally:
            if self.sd_lock:
                self.sd_lock.release()

        # 检查文件大小是否超出限制
        if self.file.tell() >= self.file_size_limit:
            self._rollover_file()

    def process_buffer(self):
        """
        按行处理缓冲区中的数据

        解析缓冲区中的数据帧，将有效的数据写入文件，
        将无效的数据记录到错误日志中。
        """
        # 处理缓冲区中的完整帧
        while True:
            # 如果缓冲区太小（小于10字节），等待更多数据
            if len(self.buffer) <= 10:
                break

            # 查找帧头标识"MCU"
            start = self.buffer.find(b"MCU")
            if start == -1:
                if self.buffer:
                    # 无帧头的垃圾数据记录到错误日志
                    self._log_error(self.buffer, "无帧头的垃圾数据记录")
                    # 清空无效数据
                    self.buffer = bytearray()
                break

            # 查找帧尾标识"\n"
            end = self.buffer.find(b"\n", start)
            if end == -1:
                # 没有完整帧，保留剩余数据等待下次处理
                if start > 0:
                    # 丢弃帧头之前的垃圾数据并记录到错误日志
                    self._log_error(self.buffer[:start], "丢弃帧头之前的垃圾数据")
                    self.buffer = self.buffer[start:]
                break

            # 取出完整帧并去除末尾空白字符
            line = self.buffer[start:end].rstrip()
            # 更新缓冲区，去掉已处理数据
            self.buffer = self.buffer[end + 1 :]

            # 校验通过，写入文件
            self._write_line(line)

        # 最大缓冲区保护，防止缓冲区无限增长
        if len(self.buffer) > self.max_buffer_size:
            self._log_error(self.buffer, "最大缓冲区保护")
            self.buffer = bytearray()

    def run(self, interval=0.05):
        """
        主循环，持续读取并处理UART数据

        Args:
            interval (float): 每次循环的休眠时间（秒）
        """
        while True:
            try:
                # 检查是否有数据待读取
                if self.uart.any():
                    data = self.uart.read()
                else:
                    data = None

                if data:
                    # 将读取到的数据加入缓冲区并处理
                    self.buffer += data
                    self.process_buffer()
            except KeyboardInterrupt:
                # 处理键盘中断（Ctrl+C）
                self.process_buffer()
                self.file.flush()
                self.file.close()
                raise  # 重新抛出异常
            except Exception:
                # 确保文件被正确关闭
                try:
                    self.file.flush()
                    self.file.close()
                except Exception:
                    # 如果文件关闭也出错，忽略
                    pass
                # 重新初始化文件
                try:
                    self._reinitialize()
                except Exception:
                    # 等待1秒后重试
                    time.sleep(1)
            finally:
                # 等待下一个循环周期
                time.sleep(interval)
                # 如果配置了LED，则切换LED状态作为运行指示
                if self.led:
                    self.led.toggle()


# 当作为主模块运行时执行以下代码
if __name__ == "__main__":
    import uos
    import _thread
    import micropython
    from sdcard import init_sd
    from led import LED

    # 分配紧急异常缓冲区，用于处理中断中的异常情况
    micropython.alloc_emergency_exception_buf(100)

    # 创建LED对象，GPIO1，默认高电平
    led = LED(1, value=1)

    # 创建UART实例
    # UART1, 波特率115200, TX引脚17, RX引脚18
    # 接收缓冲区8192字节，发送缓冲区1024字节
    uart = UART(1, baudrate=115200, tx=17, rx=18, rxbuf=8192, txbuf=1024)

    # 创建线程锁，用于保护SD卡的并发写入
    sd_lock = _thread.allocate_lock()

    # 挂载SD卡
    sd = init_sd()
    if sd:
        # 启动 UARTLogger
        logger = UARTLogger(uart, sd_lock=sd_lock, led=led)
        logger.run()
