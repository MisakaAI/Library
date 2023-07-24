#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage

def send_mail(sub,text,to=''):
    host = 'smtp.exmail.qq.com'
    port = 465
    user = ""
    key = ""

    s = smtplib.SMTP_SSL(host, port)
    s.connect(host, port)
    s.login(user,key)

    msg = EmailMessage()
    msg['Subject'] = sub
    msg['From'] = '发件人名称 <' + user + '>'
    msg['To'] = to
    msg.set_content(text)
    s.send_message(msg)
    s.quit()
