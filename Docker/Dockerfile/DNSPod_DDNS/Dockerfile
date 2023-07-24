FROM python:latest
WORKDIR /usr/src/app
ENV TZ=Asia/Shanghai
ADD send_mail.py DNSPod_ModifyRecord.py ./
RUN pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python
CMD [ "python", "./DNSPod_ModifyRecord.py" ]
