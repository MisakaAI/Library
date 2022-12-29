#!/usr/bin/env python3

import time
import asyncio
import psycopg2
from pathlib import Path
from asyncua import Client

# 日志文件
log_file = Path("/home/scada/error.log")

# SCADA 地址
url = ''

# 数据库 地址
database = ''
host = ''
port = ''
user = ''
password = ''

async def main():
    # 同步执行sql命令
    async def exec_sql(sql):
        cursor.execute(sql)

    # 更新设备状态
    async def update_comm_status(zs_id, CommStatus):
        sql = "insert into scada_comm_status (uid,value,time) values ('{uid}',{value},'{time}');".format(
            uid=zs_id,
            value=CommStatus,
            time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        cursor.execute(sql)

    # 打开数据库连接
    db = psycopg2.connect(database=database, host=host, port=port, user=user, password=password)

    # 设置数据库连接打开自动提交模式
    db.autocommit = True

    # 创建游标对象
    cursor = db.cursor()

    # 带日期的表名
    # 数据分表，每个月创建一个表
    table_name = time.strftime("scada_%Y_%m", time.localtime())

    # 查询表是否存在
    sql = "select count(*) from information_schema.tables where table_name = '{}'".format(table_name)
    cursor.execute(sql)

    # 如果不存在就创建一个新的表
    if cursor.fetchone()[0] == 0:
        sql = "create table {}(id bigserial primary key not null,\
        uid char(10) not null,\
        item char(30) not null,\
        value decimal not null,\
        creat_time timestamp not null);".format(table_name)
        cursor.execute(sql)

    # 查询错误日志是否存在
    # error_table_name = time.strftime("error_%Y_%m", time.localtime())
    error_table_name = "scada_error_log"
    sql = "select count(*) from information_schema.tables where table_name = '{}'".format(error_table_name)
    cursor.execute(sql)

    # 如果不存在就创建一个新的表
    if cursor.fetchone()[0] == 0:
        sql = "create table {}(id bigserial primary key not null,\
        uid char(10) not null,\
        item char(30) not null,\
        creat_time timestamp not null);".format(error_table_name)
        cursor.execute(sql)

    # 获取设备列表
    sql = "select * from scada_list where value like '%CommStatus%';"
    cursor.execute(sql)
    scada_list = cursor.fetchall()

    # 连接 SCADA 服务器
    async with Client(url) as client:

        # 循环注塑机列表
        for i in scada_list:
            # 创建表记录SCADA连通状态：scada_comm_status
            # 查询表是否存在
            sql = "select count(*) from information_schema.tables where table_name = '{}'".format(
                'scada_comm_status')
            cursor.execute(sql)

            # 如果不存在就创建一个新的表
            if cursor.fetchone()[0] == 0:
                sql = "create table scada_comm_status(id serial primary key not null,uid char(10) not null,value boolean not null,time timestamp not null);"
                cursor.execute(sql)
            # 查询SCADA连通状态
            var = client.get_node(i[1])
            zs_id = i[1].split('.')[2]
            CommStatus = await var.read_value()

            # 筛选最新的一条状态
            sql = "select value from scada_comm_status where uid = '{}' order by time desc limit 1;".format(
                zs_id)
            cursor.execute(sql)
            status = cursor.fetchone()

            # 如果数据库中无状态
            if status == None:
                await update_comm_status(zs_id, CommStatus)

            # 如果数据库中的状态不等于当前注塑机状态
            elif type(status) is tuple:
                if status[0] != CommStatus:
                    await update_comm_status(zs_id, CommStatus)

            # 如果能连通状态为 True
            if CommStatus:
                # 获取注塑机的信息列表
                sql = "select * from scada_list where value like '%{}%' and value not like '%CommStatus%';".format(zs_id)
                cursor.execute(sql)
                scada_value_list = cursor.fetchall()
                # 循环注塑机的信息列表
                for x in scada_value_list:
                    try:
                        # 获取数值
                        var = client.get_node(x[1])
                        value = await var.read_value()

                        # 更新数据类型
                        _type = str(type(value)).split("'")[1]
                        sql = "update scada_list set type = '{}' where id = {};".format(
                            _type, i[0])
                        cursor.execute(sql)

                        # 如果是布尔值，转换为1和0
                        if type(value) == bool:
                            if value:
                                value = 1
                            else:
                                value = 0
                        # 存进数据库中
                        sql = "insert into {table_name} (uid,item,value,creat_time) values ('{uid}','{item}',{value},'{creat_time}');".format(
                            table_name=table_name,
                            uid=zs_id,
                            item=x[1].split('.')[-1],
                            value=value,
                            creat_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        await exec_sql(sql)
                    except:
                        # 如果出错，将错误日志写入数据库
                        sql = "insert into {table_name} (uid,item,creat_time) values ('{uid}','{item}','{creat_time}');".format(
                            table_name=error_table_name,
                            uid=zs_id,
                            item=x[1].split('.')[-1],
                            creat_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        await exec_sql(sql)

    # 释放游标及数据库连接
    cursor.close()
    db.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        # 其他错误写入日志文件
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write("{}: {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), e))
