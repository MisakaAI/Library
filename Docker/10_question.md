# 一些小问题

## 解决 Dcoker logs 不显示 Python print() 的问题

在 Docker 容器里跑 Python 程序时，我们经常遇到通过 print 函数或者 logging 模块输出的信息在容器 log 中迷之失踪，过了好久又迷之出现。
这是因为 Python 在写 stdout 和 stderr 的时候有缓冲区，导致输出无法实时更新进容器 log。

1. `Dockerfile` 中设置 `ENV PYTHONUNBUFFERED=1`
2. `docker logs  --details`
3. `python -u main.py`

## 将正在运行的容器设为自启动

```sh
# 开机自启
docker update --restart=always <CONTAINER ID>

# 取消开机自启
docker update --restart=no <CONTAINER ID>
```
