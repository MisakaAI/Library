# CalDAV

- [caldav](https://caldav.readthedocs.io/)

## 使用

- [教程](https://caldav.readthedocs.io/v3.1.0/tutorial.html)

```py
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from icalendar import Calendar, Event
from caldav import DAVClient

url = ""
username = ""
password = ""

with DAVClient(url, username=username, password=password) as client:
    principal = client.get_principal()
    calendars = principal.calendars()
    for cal in calendars:
        name = cal.get_display_name()
        print(name, cal.url)

        if name == "个人":
            print("找到个人日历，准备添加事件")
            print("=" * 30)

            # 创建 ICS
            cal_ics = Calendar()
            event = Event()

            tz = ZoneInfo("Asia/Shanghai")

            start = datetime.now(tz) + timedelta(days=1)
            end = start + timedelta(hours=1)

            event.add("summary", "测试事件")
            event.add("dtstart", start)
            event.add("dtend", end)

            cal_ics.add_component(event)

            # 上传到 Nextcloud
            cal.add_event(cal_ics.to_ical())

        events = cal.events()
        for e in events:
            cal_data = Calendar.from_ical(e.data)

            for comp in cal_data.walk():
                if comp.name != "VEVENT":
                    continue

                summary = comp.get("summary")
                summary = str(summary) if summary else "无标题事件"

                dtstart = comp.get("dtstart")
                dtend = comp.get("dtend")

                # 转换为 Python 时间对象
                start = dtstart.dt if dtstart else None
                end = dtend.dt if dtend else None

                print("标题:", summary)
                print("开始:", start)
                print("结束:", end)
                print("-" * 30)

                # 删除测试事件
                if summary.startswith("测试"):
                    e.delete()
```

## iCalendar

- [icalendar](https://icalendar.readthedocs.io/en/stable/)

## 公共日历

- [大陆中文](https://calendars.icloud.com/holidays/cn_zh.ics)
- [香港中文](https://calendars.icloud.com/holidays/hk_zh.ics)
- [美国英文](https://calendars.icloud.com/holidays/us_en.ics)
- [日本日文](https://calendars.icloud.com/holidays/jp_ja.ics)

### DEMO

#### 显示当前月份的节日

```py
from datetime import datetime, date
from zoneinfo import ZoneInfo
import requests
from icalendar import Calendar


def get_holiday_from_ics(ics_url, timezone_str):
    try:
        # 获取 ICS 文件
        response = requests.get(ics_url, timeout=10)
        response.raise_for_status()

        # 用 bytes 解析（避免乱码）
        calendar = Calendar.from_ical(response.content)

        # 当前日期（指定时区）
        today = datetime.now(ZoneInfo(timezone_str)).date()

        # 测试日期（直接覆盖）
        # today = date(2026, 5, 5)

        for component in calendar.walk():
            if component.name != "VEVENT":
                continue

            event_start = component.get("dtstart").dt

            # 统一转换为 date
            if isinstance(event_start, datetime):
                event_date = event_start.date()
            elif isinstance(event_start, date):
                event_date = event_start
            else:
                continue

            # 匹配今天
            if event_date == today:
                summary = component.get("summary")

                # 处理编码
                summary = str(summary)

                # 判断国家
                if "cn_" in ics_url:
                    country = "中国"
                elif "us_" in ics_url:
                    country = "美国"
                elif "jp_" in ics_url:
                    country = "日本"
                else:
                    country = "未知"

                return [country, summary]

        return None

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    ics_urls = {
        "cn": "https://calendars.icloud.com/holidays/cn_zh.ics",
        "us": "https://calendars.icloud.com/holidays/us_en.ics",
        "jp": "https://calendars.icloud.com/holidays/jp_ja.ics",
        "hk": "https://calendars.icloud.com/holidays/hk_zh.ics",
    }

    for k, url in ics_urls.items():
        result = get_holiday_from_ics(url, "Asia/Shanghai")
        print(result)
```
