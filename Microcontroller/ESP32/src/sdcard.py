# SD Card
import machine
import uos

"""
SDCard参数|含义|值|说明
-|-|-|-
slot|SD 控制器编号|2|ESP32 有 2 个 SD 控制器，常用 slot=2（外部 SD）
width|数据总线宽度|8|表示 8-bit 总线（一般是 SDMMC 模式才支持）
sck|时钟线（CLK）|12|连接 SD 卡的 CLK 引脚
miso|主输入从输出|13|从 SD 卡读数据的引脚（即 DO）
mosi|主输出从输入|11|向 SD 卡写数据的引脚（即 DI）
cs|片选信号线|2|用于 SPI 模式时选择 SD 卡设备
"""


# 初始化 & 挂载 SD 卡
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


# 卸载 SD 卡
def umount_sd():
    try:
        uos.umount("/sd")
    except Exception as e:
        print("SD 卸载失败:", e)
        return None


if __name__ == "__main__":
    init_sd()
