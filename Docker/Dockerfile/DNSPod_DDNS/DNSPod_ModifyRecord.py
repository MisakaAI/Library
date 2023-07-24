#!/usr/bin/env python3

# 腾讯云 API
# https://cloud.tencent.com/document/api

# 将腾讯云 Python SDK 安装至您的项目中
# https://cloud.tencent.com/document/sdk/Python
# pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python

import os
import json
import datetime
from send_mail import send_mail
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models

# https://console.dnspod.cn/account/token/apikey
SecretId = ""
SecretKey = ""

# https://console.cloud.tencent.com/api/explorer
# DescribeRecordList

Domain = "" # 域名
SubDomain = "" # 前缀
hostname = SubDomain + '.' + Domain

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
    # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
    cred = credential.Credential(SecretId, SecretKey)
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    httpProfile = HttpProfile()
    httpProfile.endpoint = "dnspod.tencentcloudapi.com"

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 实例化要请求产品的client对象,clientProfile是可选的
    client = dnspod_client.DnspodClient(cred, "", clientProfile)

    def get_now(Domain, SubDomain):
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": Domain,
            "Subdomain": SubDomain
        }
        req.from_json_string(json.dumps(params))
        # 返回的resp是一个DescribeRecordListResponse的实例，与请求对象对应
        resp = client.DescribeRecordList(req)
        # 输出json格式的字符串回包
        return resp.RecordList[0]
    now = get_now(Domain, SubDomain)
    Value = os.popen('hostname -I').read().split()[-1]

    if now.Value != Value:
        print("[{}]".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        print('  域名: {}'.format(hostname))
        print('  当前解析: {}'.format(now.Value))
        print('  本机地址: {}'.format(Value))
        old_value = now.Value
        req = models.ModifyRecordRequest()
        params = {
            "Domain": Domain,
            "SubDomain": SubDomain,
            "RecordType": now.Type,
            "RecordLine": now.Line,
            "Value": Value,
            "RecordId": now.RecordId
        }
        req.from_json_string(json.dumps(params))
        resp = client.ModifyRecord(req)
        now = get_now(Domain, SubDomain)

        send_mail('主机的ipv6地址已经更新。', '{}\n旧地址：{}，\n新地址：{}\n'.format(hostname, old_value, now.Value))
except TencentCloudSDKException as err:
    print('  主机的ipv6地址更新时出现了错误。', str(err))
    send_mail('主机的ipv6地址更新时出现了错误。{}\n当前域名解析: {}\n本机IP地址: {}'.format(str(err),hostname,now,Value))
