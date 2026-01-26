import sys
# https://github.com/micropython/micropython-lib/tree/master/micropython/bluetooth

# 将当前目录添加到Python模块搜索路径中，以便导入本地模块
sys.path.append("")

# 从micropython导入const函数，用于定义常量
import asyncio
import aioble
import bluetooth

DERVICE_NAME = "ESP32_BLE"

# 自定义服务UUID
_CUSTOM_SERVICE_UUID = bluetooth.UUID("b906a793-99ed-4141-9d7c-0551612f8664")
# 自定义特征值UUID
_CUSTOM_CHARACTERISTIC_UUID = bluetooth.UUID("1c406797-9b20-4dc7-a6a4-3cc9c648c202")
# 广播间隔时间（微秒），控制蓝牙广告包发送频率为20Hz（50000微秒）
_ADV_INTERVAL_US = 50_000

# 注册GATT服务器服务
# 创建自定义服务
custom_service = aioble.Service(_CUSTOM_SERVICE_UUID)
# 创建自定义特征值，支持读取和通知功能
# 用于传输自定义数据字符串
custom_characteristic = aioble.Characteristic(custom_service, _CUSTOM_CHARACTERISTIC_UUID, read=True, notify=True)
# 注册服务到aioble框架中
aioble.register_services(custom_service)
# 当前连接的蓝牙设备
current_connection = None

# 向连接的客户端发送数据
def ble_notify(message):
    if current_connection is None:
        return False  # 未连接，不发送
    try:
        custom_characteristic.write(message, send_update=True)
        return True
    except Exception as e:
        print("BLE notify error:", e)
        return False

# 外设任务函数：处理蓝牙广播和连接
async def peripheral_task():
    global current_connection
    # 持续广播直到有中心设备连接
    while True:
        # 开始蓝牙广播并等待连接
        async with await aioble.advertise(
            _ADV_INTERVAL_US,  # 广播间隔（微秒）
            name=DERVICE_NAME,  # 设备广播名称
            services=[_CUSTOM_SERVICE_UUID],  # 提供的服务UUID列表
            # 移除了appearance参数，因为它是可选的
        ) as connection:
            current_connection = connection  # 保存当前连接
            # 当有设备连接时打印连接信息
            print("Connection from", connection.device)
            # 等待连接断开，timeout_ms=None表示无限等待
            await connection.disconnected(timeout_ms=None)
            current_connection = None  # 断开后清空

if __name__ == "__main__":
    # 启动异步事件循环，运行主函数
    asyncio.run(peripheral_task())
