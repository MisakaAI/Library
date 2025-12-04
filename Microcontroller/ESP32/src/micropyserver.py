# MicroPyServer
# https://github.com/troublegum/micropyserver
# 这是一个为 MicroPython 设计的轻量级 Web 服务器实现

# 增加文件下载功能 send_file()

import re
import socket
import sys
import io


class MicroPyServer(object):
    """MicroPython Web服务器类"""

    def __init__(self, host="0.0.0.0", port=80):
        """构造函数，初始化服务器配置

        参数:
            host: 服务器监听的主机地址，默认为"0.0.0.0"（监听所有网络接口）
            port: 服务器监听的端口号，默认为80
        """
        self._host = host  # 服务器主机地址
        self._port = port  # 服务器端口号
        self._routes = []  # 路由表，存储URL路径与处理函数的映射关系
        self._connect = None  # 当前连接对象
        self._on_request_handler = None  # 请求处理钩子函数
        self._on_not_found_handler = None  # 404未找到处理钩子函数
        self._on_error_handler = None  # 错误处理钩子函数
        self._sock = None  # socket对象

    def start(self):
        """启动服务器，开始监听和处理请求"""
        # 创建TCP socket对象
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置socket选项，允许地址重用
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定主机和端口
        self._sock.bind((self._host, self._port))
        # 开始监听，最大等待连接数为1
        self._sock.listen(1)
        print("Server start")
        # 服务器主循环
        while True:
            # 如果socket为None，说明服务器已停止
            if self._sock is None:
                break
            try:
                # 接受客户端连接
                self._connect, address = self._sock.accept()
                # 获取请求数据
                request = self.get_request()
                # 如果请求为空，则关闭连接并继续下一次循环
                if len(request) == 0:
                    self._connect.close()
                    continue
                # 如果设置了请求处理钩子函数
                if self._on_request_handler:
                    # 调用钩子函数，如果返回False则继续下一次循环
                    if not self._on_request_handler(request, address):
                        continue
                # 查找匹配的路由
                route = self.find_route(request)
                # 如果找到匹配的路由，则调用对应的处理函数
                if route:
                    route["handler"](request, self)
                else:
                    # 如果未找到匹配的路由，则调用未找到处理函数
                    self._route_not_found(request)
            except Exception as e:
                # 处理内部错误
                self._internal_error(e)
            finally:
                # 关闭当前连接
                self._connect.close()

    def stop(self):
        """停止服务器"""
        # 关闭连接和socket
        self._connect.close()
        self._sock.close()
        self._sock = None
        print("Server stop")

    def add_route(self, path, handler, method="GET"):
        """添加新的路由映射

        参数:
            path: URL路径
            handler: 处理函数
            method: HTTP方法，默认为"GET"
        """
        self._routes.append({"path": path, "handler": handler, "method": method})

    def send(self, data):
        """向客户端发送数据

        参数:
            data: 要发送的数据（字符串或字节）
        """
        # 检查是否有有效的连接
        if self._connect is None:
            raise Exception("Can't send response, no connection instance")
        try:
            # 尝试将数据编码为字节后发送
            self._connect.sendall(data.encode())
        except Exception:
            # 如果已经是字节数据，则直接发送
            self._connect.sendall(data)

    def send_bytes(self, bdata):
        """向客户端发送字节数据

        参数:
            bdata: 要发送的字节数据
        """
        # 检查是否有有效的连接
        if self._connect is None:
            raise Exception("Can't send response, no connection instance")
        # 发送字节数据
        self._connect.sendall(bdata)

    def find_route(self, request):
        """查找匹配的路由

        参数:
            request: HTTP请求数据

        返回:
            匹配的路由信息字典，未找到则返回None
        """
        # 将请求按行分割
        lines = request.split("\r\n")
        # 使用正则表达式提取HTTP方法（GET、POST等）
        method = re.search("^([A-Z]+)", lines[0]).group(1)
        # 使用正则表达式提取请求路径
        match = re.search(r"^[A-Z]+\s+(/[^\s?]*)", lines[0])
        path = match.group(1) if match else "/"
        # 遍历路由表查找匹配的路由
        for route in self._routes:
            # 如果HTTP方法不匹配，则跳过
            if method != route["method"]:
                continue
            # 如果路径完全匹配，则返回该路由
            if path == route["path"]:
                return route
            else:
                # 尝试使用正则表达式匹配路径
                match = re.search("^" + route["path"] + "$", path)
                if match:
                    print(method, path, route["path"])
                    return route

    def get_request(self, buffer_length=4096):
        """获取HTTP请求数据

        参数:
            buffer_length: 缓冲区大小，默认为4096字节

        返回:
            HTTP请求数据字符串
        """
        # 初始化数据字节
        data = b""
        # 循环接收数据
        while True:
            # 接收指定长度的数据
            part = self._connect.recv(buffer_length)
            # 如果没有接收到数据，则跳出循环
            if not part:
                break
            # 将接收到的数据添加到总数据中
            data += part
            # 如果已经读取到HTTP头部结束标记，则跳出循环
            if b"\r\n\r\n" in data:
                break
        # 将字节数据解码为字符串并返回
        return data.decode("utf8", "ignore")

    def on_request(self, handler):
        """设置请求处理钩子函数

        参数:
            handler: 请求处理函数
        """
        self._on_request_handler = handler

    def on_not_found(self, handler):
        """设置404未找到处理钩子函数

        参数:
            handler: 404处理函数
        """
        self._on_not_found_handler = handler

    def on_error(self, handler):
        """设置错误处理钩子函数

        参数:
            handler: 错误处理函数
        """
        self._on_error_handler = handler

    def _route_not_found(self, request):
        """路由未找到处理函数

        参数:
            request: HTTP请求数据
        """
        # 如果设置了自定义的未找到处理函数，则调用它
        if self._on_not_found_handler:
            self._on_not_found_handler(request)
        else:
            """默认的未找到处理函数"""
            # 发送404状态码和提示信息
            self.send("HTTP/1.0 404 Not Found\r\n")
            self.send("Content-Type: text/plain\r\n\r\n")
            self.send("Not found")

    def _internal_error(self, error):
        """内部错误处理函数

        参数:
            error: 异常对象
        """
        # 如果设置了自定义的错误处理函数，则调用它
        if self._on_error_handler:
            self._on_error_handler(error)
        else:
            """默认的内部错误处理函数"""
            # 如果sys模块中有print_exception函数，则使用它输出异常信息
            if "print_exception" in dir(sys):
                output = io.StringIO()
                sys.print_exception(error, output)
                str_error = output.getvalue()
                output.close()
            else:
                # 否则直接将异常转换为字符串
                str_error = str(error)
            # 发送500状态码和错误信息
            self.send("HTTP/1.0 500 Internal Server Error\r\n")
            self.send("Content-Type: text/plain\r\n\r\n")
            self.send("Error: " + str_error)
            # 在控制台打印错误信息
            print(str_error)

    def send_file(self, fs_path, download_name=None):
        """发送文件给客户端

        参数:
            fs_path: 文件系统路径
            download_name: 下载时的文件名，可选
        """
        try:
            # 发送HTTP成功状态行
            self._connect.sendall(b"HTTP/1.0 200 OK\r\n")
            # 根据文件扩展名设置相应的内容类型
            if fs_path.endswith(".html"):
                self._connect.sendall(b"Content-Type: text/html\r\n")
            elif fs_path.endswith(".css"):
                self._connect.sendall(b"Content-Type: text/css\r\n")
            elif fs_path.endswith(".js"):
                self._connect.sendall(b"Content-Type: application/javascript\r\n")
            else:
                # 默认二进制流类型
                self._connect.sendall(b"Content-Type: application/octet-stream\r\n")
            # 如果指定了下载文件名，则添加Content-Disposition头部
            if download_name:
                disposition = (
                    'Content-Disposition: attachment; filename="{}"\r\n'.format(
                        download_name
                    )
                )
                self._connect.sendall(disposition.encode())
            # 发送空行，表示HTTP头部结束
            self._connect.sendall(b"\r\n")
            # 以二进制模式打开文件并分块发送
            with open(fs_path, "rb") as f:
                while True:
                    # 每次读取10240字节
                    chunk = f.read(10240)
                    # 如果读取到文件末尾则结束循环
                    if not chunk:
                        break
                    # 发送文件块
                    self._connect.sendall(chunk)
        except Exception as e:
            # 如果出现错误，则打印错误信息
            print("send_file error:", e)
