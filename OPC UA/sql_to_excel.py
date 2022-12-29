import os
import datetime
import psycopg2
from pathlib import Path
from openpyxl import Workbook

desktop=Path(os.path.join(os.path.expanduser("~"), 'Desktop'))
wb = Workbook()
ws_d = wb[wb.sheetnames[0]]

# 数据库 地址
database = ''
host = ''
port = ''
user = ''
password = ''

# 查询内容
## 设备
uid = ''
## 开始时间
## 格式：2022-01-01 00:00
time_start = ""
## 结束时间
time_end = ""

# 打开数据库连接
db = psycopg2.connect(database=database, host=host, port=port, user=user, password=password)

# 设置数据库连接打开自动提交模式
db.autocommit = True

# 创建游标对象
cursor = db.cursor()

# 查询语句
sql = "select * from scada_{} where uid = '{}' and creat_time >= '{}' and creat_time <= '{}' order by creat_time".format(time_start.split('-')[0] + '_' + time_start.split('-')[1],uid,time_start,time_end)
cursor.execute(sql)
a = cursor.fetchall()

l = {}
for i in a:
    if str(i[4])[:-3] not in l:
        l[str(i[4])[:-3]] = {}
    l[str(i[4])[:-3]][i[2].split()[0]] = i[3]

x = []
for i in l:
    for n in l[i]:
        if n not in x:
            x.append(n)

ws_d.append(['设备','时间'] + x)

for i in l:
    z = [uid,i]
    for y in x:
        if y in l[i]:
            z.append(l[i][y])
        else:
            z.append('')
    ws_d.append(z)

wb.save(desktop.joinpath("SCADA数据导出.xlsx"))
