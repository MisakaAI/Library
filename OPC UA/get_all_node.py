#!/usr/bin/env python3

import asyncio
import psycopg2

from asyncua import Client, ua
from asyncua.common import ua_utils

# create table scada_list
#
# id serial primary key not null
# device varchar(10) not null
# item varchar(100) not null
# value varchar(200) not null
# type varchar(10)
#
# create table scada_list (id serial primary key not null,device varchar(10) not null,item varchar(100) not null,value varchar(200) not null,type varchar(10));

url = ""
database = ''
host = ''
port = ''
user = ''
password = ''

# 打开数据库连接
db = psycopg2.connect(database=database, host=host,
                      port=port, user=user, password=password)

# 设置数据库连接打开自动提交模式
db.autocommit = True

# 创建游标对象
cursor = db.cursor()

# 读取节点并写入数据库


async def main():
    client = Client(url)
    # client.session_timeout = 2000
    # root = client.nodes.root
    async with client:
        node_List = await ua_utils.get_node_children(client.nodes.objects)
        for n in node_List:
            nodeClass = await n.read_node_class()
            if nodeClass == ua.NodeClass.Variable:
                if 'ZS' in str(n):
                    sql = "insert into scada_list (value) values ('{}');".format(
                        n)
                    cursor.execute(sql)
                    print(sql)

# 获取节点值的类型，并写入数据库


async def add_type():
    sql = "select * from scada_list;"
    cursor.execute(sql)
    _list = cursor.fetchall()
    async with Client(url) as client:
        for i in _list:
            try:
                var = client.get_node(i[1])
                value = await var.read_value()
                _type = str(type(value)).split("'")[1]
                sql = "update scada_list set type = '{}' where id = {};".format(
                    _type, i[0])
                cursor.execute(sql)
            except:
                print(i)

if __name__ == "__main__":
    asyncio.run(main())
    # asyncio.run(add_type())
