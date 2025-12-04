# RTC
from machine import RTC


# 获取 RTC 时间戳
def get_rtc_timestamp():
    year, month, day, weekday, hour, minute, second, _ = RTC().datetime()
    # 格式化为 YYYYMMDD-HHMMSS
    timestamp = "{:04d}{:02d}{:02d}_{:02d}{:02d}{:02d}".format(
        year, month, day, hour, minute, second
    )
    return timestamp


# RTC 校验
def rtc_check():
    if RTC().datetime()[0] >= 2025:
        return get_rtc_timestamp()
    else:
        return False


if __name__ == "__main__":
    t = get_rtc_timestamp()
    print(t)
