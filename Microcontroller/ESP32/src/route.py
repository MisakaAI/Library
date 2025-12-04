# Route
# 路由处理

import uos
from utils import get_request_post_params, get_request_query_params, get_request_method

SD_ROOT = "/sd"  # SD卡根目录路径常量


def safe_filename(name):
    """安全文件名校验函数，防止路径遍历攻击

    参数:
        name: 待校验的文件名

    返回:
        如果文件名安全则返回原文件名，否则返回None
    """
    # 检查是否包含路径遍历字符（如..）或以/或\开头，防止访问系统其他目录
    if ".." in name or name.startswith("/") or "\\" in name:
        return None
    return name


def route_index(request, server):
    """首页路由处理函数，返回index.html页面内容

    参数:
        request: HTTP请求内容
        server: 服务器实例对象
    """
    # 发送HTTP响应头部，状态码200表示成功，内容类型为HTML，字符集为UTF-8
    server.send("HTTP/1.0 200 OK\r\n")
    server.send("Content-Type: text/html; charset=utf-8\r\n\r\n")
    # 以只读模式、UTF-8编码打开index.html文件
    with open("index.html", "r", encoding="utf-8") as f:
        # 循环读取文件内容，每次读取8192字节，以节省内存
        while True:
            chunk = f.read(8192)
            # 如果读取到文件末尾则结束循环
            if not chunk:
                break
            # 将读取到的内容发送给客户端
            server.send(chunk)


def route_list(request, server):
    """文件列表路由处理函数，列出SD卡根目录下的所有文件

    参数:
        request: HTTP请求内容
        server: 服务器实例对象

    返回:
        JSON格式的文件列表，每个文件包含文件名和大小
    """
    # 初始化文件列表数组
    files = []
    try:
        # 遍历SD卡根目录下的所有文件
        for fname in uos.listdir(SD_ROOT):
            # 拼接完整文件路径
            fpath = SD_ROOT + "/" + fname
            try:
                # 获取文件状态信息
                stat = uos.stat(fpath)
                # 从状态信息中提取文件大小（stat[6]是文件大小字段）
                size = stat[6] if isinstance(stat, (tuple, list)) else 0
            except Exception:
                # 如果获取文件状态失败，则文件大小为0
                size = 0
            # 将文件信息添加到列表中
            files.append({"name": fname, "size": size})
    except Exception as e:
        # 如果读取目录失败，返回500错误和错误信息
        server.send("HTTP/1.0 500 Internal Server Error\r\n")
        server.send("Content-Type: text/plain\r\n\r\n")
        server.send("Error listing SD: " + str(e))
        return
    # 简单实现JSON序列化（避免在某些MicroPython移植上import json可能出错的问题）
    j = (
        "["
        + ",".join(
            [
                '{"name":"%s","size":%d}' % (f["name"].replace('"', '\\"'), f["size"])
                for f in files
            ]
        )
        + "]"
    )
    # 发送HTTP响应头部，状态码200表示成功，内容类型为JSON
    server.send("HTTP/1.0 200 OK\r\n")
    server.send("Content-Type: application/json\r\n\r\n")
    # 发送JSON格式的文件列表数据
    server.send(j)


def route_download(request, server):
    """文件下载路由处理函数，允许用户下载SD卡中的文件

    参数:
        request: HTTP请求内容
        server: 服务器实例对象
    """
    # 从请求中获取查询参数
    params = get_request_query_params(request)
    # 获取文件名参数
    fname = params.get("file", "")
    # 校验文件名安全性
    fname = safe_filename(fname)
    # 如果文件名不安全，则返回400错误
    if not fname:
        server.send("HTTP/1.0 400 Bad Request\r\n")
        server.send("Content-Type: text/plain\r\n\r\n")
        server.send("Invalid file name")
        return
    # 拼接完整文件路径
    fpath = SD_ROOT + "/" + fname
    try:
        # 确认文件是否存在
        uos.stat(fpath)
    except Exception:
        # 如果文件不存在，返回404错误
        server.send("HTTP/1.0 404 Not Found\r\n")
        server.send("Content-Type: text/plain\r\n\r\n")
        server.send("Not found")
        return
    # 使用send_file流式发送文件（作为附件下载）
    server.send_file(fpath, download_name=fname)


def route_delete(request, server, sd_lock=None):
    """删除单个文件路由处理函数

    参数:
        request: HTTP请求内容
        server: 服务器实例对象
    """
    # 获取POST请求参数
    post = get_request_post_params(request)
    # 如果不是POST请求，则返回405错误提示使用POST方法
    if post is None:
        server.send("HTTP/1.0 405 Method not allowed\r\n")
        server.send("Content-Type: text/plain\r\n\r\n")
        server.send("Use POST")
        return
    # 从POST参数中获取文件名
    fname = post.get("file", "")
    # 校验文件名安全性
    fname = safe_filename(fname)
    # 如果文件名不安全，则返回400错误
    if not fname:
        server.send("HTTP/1.0 400 Bad Request\r\n")
        server.send("Content-Type: text/plain\r\n\r\n")
        server.send("Invalid file")
        return
    # 拼接完整文件路径
    fpath = SD_ROOT + "/" + fname
    try:
        # 获取锁
        if sd_lock:
            sd_lock.acquire()
        # 删除指定文件
        uos.remove(fpath)
        # 删除成功，返回成功信息
        server.send("HTTP/1.0 200 OK\r\n")
        server.send("Content-Type: text/plain\r\n\r\n")
        server.send("Deleted " + fname)
    except Exception as e:
        # 删除失败，返回500错误和错误信息
        server.send("HTTP/1.0 500 Internal Server Error\r\n")
        server.send("Content-Type: text/plain\r\n\r\n")
        server.send("Delete failed: " + str(e))
    finally:
        # 释放锁
        if sd_lock:
            sd_lock.release()


def route_delete_all(request, server, sd_lock=None):
    """删除所有文件路由处理函数

    参数:
        request: HTTP请求内容
        server: 服务器实例对象
    """
    # 检查请求方法是否为POST，不是则返回405错误
    if get_request_method(request) != "POST":
        server.send("HTTP/1.0 405 Method not allowed\r\n")
        server.send("Content-Type: text/plain\r\n\r\n")
        server.send("Use POST")
        return
    try:
        # 获取锁
        if sd_lock:
            sd_lock.acquire()
        # 遍历SD卡根目录下的所有文件
        for fname in uos.listdir(SD_ROOT):
            # 拼接完整文件路径
            fpath = SD_ROOT + "/" + fname
            try:
                # 删除文件
                uos.remove(fpath)
            except Exception as e:
                # 如果删除单个文件失败，打印错误信息但继续删除其他文件
                print("failed remove", fpath, e)
        # 所有文件删除成功，返回成功信息
        server.send("HTTP/1.0 200 OK\r\n")
        server.send("Content-Type: text/plain\r\n\r\n")
        server.send("Deleted all files in /sd")
    except Exception as e:
        # 删除过程中出现错误，返回500错误和错误信息
        server.send("HTTP/1.0 500 Internal Server Error\r\n")
        server.send("Content-Type: text/plain\r\n\r\n")
        server.send("Delete all failed: " + str(e))
    finally:
        # 释放锁
        if sd_lock:
            sd_lock.release()
