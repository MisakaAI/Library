# -*- coding: utf-8 -*-
# 推送钉钉工作通知
# 需要手动配置 AgentId、AppKey、AppSecret 这三个参数

import argparse
import requests

# 设置
# https://open-dev.dingtalk.com/fe/app#/corp/app

AgentId = 
AppKey = ""
AppSecret = ""

# 获取企业接口凭证

# 使用方法
# access_token = get_access_token()

def get_access_token():
    url = "https://oapi.dingtalk.com/gettoken?appkey={}&appsecret={}".format(AppKey,AppSecret)
    r = requests.get(url)
    return r.json()['access_token']

# 获取用户ID
# mobile - 手机号
# access_token - 企业接口凭证

# 使用方法
# userid = get_userid('手机号',get_access_token())
# userid = 'A001'
# userid = 'A001,A002'

def get_userid(mobile,access_token):
    url = "https://oapi.dingtalk.com/topapi/v2/user/getbymobile?access_token={}".format(access_token)
    data = {
        "mobile":str(mobile)
    }
    r = requests.post(url,json=data)
    if r.json()['errmsg'] == 'ok':
        return r.json()['result']['userid']
    else:
        return r.json()['errmsg']

# 发送工作通知

# msg - 消息内容
# userid - 用户ID（工号）
# access_token - 企业接口凭证

# 使用方法
# send_message("Hello World !",userid,access_token)

def send_message(msg,userid,access_token):
    url = "https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2?access_token={}".format(access_token)
    data = {
        "agent_id":AgentId,
        "msg":{
            "msgtype":"text",
                "oa":{
                "body":{
                "content":msg
            }
        },
        "text":{
            "content":msg
            }
        },
        "userid_list":userid
    }
    r = requests.post(url,json=data)
    return r.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="推送钉钉工作通知。")
    parser.add_argument('-p', '--phone', type=int, metavar='手机号', required=True)
    parser.add_argument('-m', '--message', metavar='消息内容', required=True)
    args = parser.parse_args()
    access_token = get_access_token()
    userid = get_userid(args.phone,access_token)
    send_message(args.message,userid,access_token)
