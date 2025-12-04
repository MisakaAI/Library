# main.py

import uos
import time
import _thread
import micropython
from machine import UART
from led import LED
from wifi_ap import start_ap
from sdcard import init_sd
from micropyserver import MicroPyServer
from uart import UARTLogger
from route import (
    route_index,
    route_list,
    route_download,
    route_delete,
    route_delete_all,
)

# 分配紧急异常缓冲区，用于处理中断中的异常情况
micropython.alloc_emergency_exception_buf(100)

# 硬件 UART1 配置
# 使用GPIO17作为TX引脚，GPIO18作为RX引脚
TX = 17
RX = 18
uart = UART(1, baudrate=115200, tx=TX, rx=RX, rxbuf=8192, txbuf=1024)

# Wi-Fi 热点配置
# 设置默认的热点名称和密码
SSID = "ESP32-AP"
PASSWORD = "12345678"

# LED 配置
# 使用GPIO1控制LED，初始状态为高电平（熄灭状态）
led = LED(1, value=1)

# 线程锁
# 创建线程锁用于保护SD卡的并发访问
sd_lock = _thread.allocate_lock()


# 创建 HTTP 服务器
def start_server():
    """
    启动HTTP服务器并注册路由处理函数

    初始化MicroPyServer实例，配置各URL路由对应的处理函数，
    然后启动服务器开始监听HTTP请求。
    """
    # 创建服务器实例，监听所有网络接口的80端口
    srv = MicroPyServer(host="0.0.0.0", port=80)

    # 注册路由处理函数
    srv.add_route("/", route_index, method="GET")  # 主页路由
    srv.add_route("/list", route_list, method="GET")  # 文件列表路由
    srv.add_route("/download", route_download, method="GET")  # 文件下载路由
    srv.add_route(
        "/delete", lambda req, srv_: route_delete(req, srv_, sd_lock), method="POST"
    )  # 删除文件路由
    srv.add_route(
        "/delete_all",
        lambda req, srv_: route_delete_all(req, srv_, sd_lock),
        method="POST",
    )  # 删除所有文件路由

    # 启动服务器并处理异常
    try:
        srv.start()
    except KeyboardInterrupt:
        srv.stop()


# UART 数据采集
def start_uart():
    """
    启动UART数据采集功能

    创建UARTLogger实例，开始监听并记录UART接口接收到的数据。
    """
    # 启动 UARTLogger
    logger = UARTLogger(uart, sd_lock=sd_lock, led=led)
    logger.run()


def run():
    """
    主运行函数

    依次初始化Wi-Fi热点、SD卡，然后启动HTTP服务器和UART数据采集线程，
    最后进入主循环保持程序运行。
    """
    # 启动Wi-Fi热点
    start_ap(SSID, PASSWORD)

    # 初始化SD卡
    sd = init_sd()

    # 如果SD卡初始化成功，则启动服务器和UART线程
    if sd:
        # 启动HTTP服务器线程
        _thread.start_new_thread(start_server, ())
        # 启动UART数据采集线程
        _thread.start_new_thread(start_uart, ())

    # 主循环，保持程序运行
    while True:
        time.sleep(1)


# 当作为主模块运行时，启动系统
if __name__ == "__main__":
    run()
