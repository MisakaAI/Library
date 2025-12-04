# MicroPyServer 工具模块
# https://github.com/troublegum/micropyserver/blob/master/utils.py

import re

""" HTTP 响应状态码及对应描述信息
这是一个字典，包含了常见的 HTTP 状态码及其标准描述信息，
用于在 HTTP 响应中提供标准的状态描述。
例如: 200: "Ok" 表示请求成功
"""
HTTP_CODES = {
    100: "Continue",  # 继续：客户端应继续其请求
    101: "Switching protocols",  # 切换协议：服务器根据客户端请求切换协议
    102: "Processing",  # 处理中：请求正在处理中，尚未完成
    200: "Ok",  # 成功：请求成功
    201: "Created",  # 已创建：请求成功并且服务器创建了新的资源
    202: "Accepted",  # 已接受：请求已经被接受，但尚未处理完成
    203: "Non authoritative information",  # 非授权信息：请求成功，但返回的元信息不在原始服务器上
    204: "No content",  # 无内容：服务器成功处理，但未返回内容
    205: "Reset content",  # 重置内容：服务器处理成功，用户终端应重置文档视图
    206: "Partial content",  # 部分内容：服务器成功处理了部分GET请求
    207: "Multi status",  # 多状态：由WebDAV返回的多状态
    208: "Already reported",  # 已报告：DAV绑定的成员已经在（多状态）响应的前面部分被列举
    226: "Im used",  # IM已使用：服务器已经满足了对资源的请求
    300: "Multiple choices",  # 多种选择：针对请求，服务器可执行多种操作
    301: "Moved permanently",  # 永久移动：请求的资源已被永久的移动到新URI
    302: "Found",  # 临时移动：请求的资源临时从不同的URI响应请求
    303: "See other",  # 查看其它地址：对应当前请求的响应可以在另一个URI上被找到
    304: "Not modified",  # 未修改：所请求的资源未修改，服务器返回此状态码时不会返回任何资源
    305: "Use proxy",  # 使用代理：被请求的资源必须通过指定的代理才能被访问
    307: "Temporary redirect",  # 临时重定向：请求的资源临时从不同的URI响应请求
    308: "Permanent redirect",  # 永久重定向：请求的资源已被永久的移动到新URI
    400: "Bad request",  # 客户端请求的语法错误，服务器无法理解
    401: "Unauthorized",  # 请求要求用户的身份认证
    402: "Payment required",  # 保留，将来使用
    403: "Forbidden",  # 服务器理解请求客户端的请求，但是拒绝执行此请求
    404: "Not found",  # 服务器无法根据客户端的请求找到资源
    405: "Method not allowed",  # 客户端请求中的方法被禁止
    406: "Not acceptable",  # 服务器无法根据客户端请求的内容特性完成请求
    407: "Proxy authentication required",  # 请求要求代理的身份认证
    408: "Request timeout",  # 服务器等待客户端发送的请求时间过长
    409: "Conflict",  # 服务器完成客户端的PUT请求时可能返回此代码，服务器处理请求时发生了冲突
    410: "Gone",  # 客户端请求的资源已经不存在
    411: "Length required",  # 服务器无法处理缺少有效内容长度标头字段的请求
    412: "Precondition failed",  # 客户端请求信息的先决条件错误
    413: "Request entity too large",  # 由于请求的实体过大，服务器无法处理
    414: "Request uri too long",  # 请求的URI过长
    415: "Unsupported media type",  # 服务器无法处理请求附带的媒体格式
    416: "Request range not satisfiable",  # 客户端请求的范围无效
    417: "Expectation failed",  # 服务器无法满足Expect的请求头信息
    418: "I am a teapot",  # 一个幽默的HTTP状态码，用于拒绝冲泡咖啡的请求
    422: "Unprocessable entity",  # 请求格式良好，但由于语义错误而无法处理
    423: "Locked",  # 当前资源被锁定
    424: "Failed dependency",  # 由于前一个请求失败，导致依赖的请求失败
    426: "Upgrade required",  # 客户端应当切换到不同的协议
    428: "Precondition required",  # 要求先决条件，用于防止"丢失更新"问题
    429: "Too many requests",  # 请求次数超过限制
    431: "Request header fields too large",  # 请求头字段太大
    500: "Internal server error",  # 服务器内部错误，无法完成请求
    501: "Not implemented",  # 服务器不支持请求的功能
    502: "Bad gateway",  # 作为网关或代理工作的服务器尝试处理请求时，从远程服务器接收到无效响应
    503: "Service unavailable",  # 由于超载或系统维护，服务器暂时的无法处理客户端的请求
    504: "Gateway timeout",  # 充当网关或代理的服务器，未及时从远端服务器获取请求
    505: "Http version not supported",  # 服务器不支持请求的HTTP协议的版本
    506: "Variant also negotiates",  # 服务器存在内部配置错误
    507: "Insufficient storage",  # 服务器无法存储完成请求所必须的内容
    508: "Loop detected",  # 服务器在处理请求时检测到无限循环
    510: "Not extended",  # 获取资源所需的策略没有被满足
    511: "Network authentication required",  # 客户端需要进行身份验证才能获得网络访问权限
}


def send_response(
    server, response, http_code=200, content_type="text/html", extend_headers=None
):
    """发送HTTP响应

    参数:
        server: 服务器实例对象
        response: 响应内容
        http_code: HTTP状态码，默认为200（成功）
        content_type: 响应内容类型，默认为"text/html"
        extend_headers: 额外的HTTP头部信息，可选
    """
    # 发送HTTP状态行，包含协议版本、状态码和状态描述
    server.send("HTTP/1.0 " + str(http_code) + " " + HTTP_CODES.get(http_code) + "\r\n")
    # 发送内容类型头部
    server.send("Content-Type: " + content_type + "\r\n")
    # 如果有额外的头部信息，则逐一发送
    if extend_headers is not None:
        for header in extend_headers:
            server.send(header + "\r\n")
    # 发送空行，表示HTTP头部结束
    server.send("\r\n")
    # 发送响应体内容
    server.send(response)


def get_request_method(request):
    """获取HTTP请求方法（GET、POST等）

    参数:
        request: HTTP请求字符串

    返回:
        HTTP请求方法，如"GET"、"POST"等
    """
    # 将请求按行分割
    lines = request.split("\r\n")
    # 使用正则表达式匹配第一行中的请求方法（第一个单词）
    return re.search("^([A-Z]+)", lines[0]).group(1)


def get_request_query_string(request):
    """获取HTTP请求中的查询字符串部分

    参数:
        request: HTTP请求字符串

    返回:
        查询字符串，即URL中?后面的部分
    """
    # 将请求按行分割
    lines = request.split("\r\n")
    # 使用正则表达式匹配第一行中URL的查询字符串部分（?和空格之间的内容）
    match = re.search("\\?(.+)\\s", lines[0])
    # 如果没有匹配到查询字符串，则返回空字符串
    if match is None:
        return ""
    else:
        # 返回匹配到的查询字符串
        return match.group(1)


def parse_query_string(query_string):
    """解析查询字符串，将其转换为参数字典

    参数:
        query_string: 查询字符串，例如 "name=john&age=25"

    返回:
        包含查询参数的字典，键值对形式
    """
    # 如果查询字符串为空，则返回空字典
    if len(query_string) == 0:
        return {}
    # 将查询字符串按&分割成参数列表
    query_params_string = query_string.split("&")
    # 初始化参数字典
    query_params = {}
    # 遍历每个参数字符串
    for param_string in query_params_string:
        # 将参数按=分割成键和值
        param = param_string.split("=")
        key = param[0]
        # 如果参数没有值，则值为空字符串
        if len(param) == 1:
            value = ""
        else:
            value = param[1]
        # 对值进行URL解码并存入字典
        query_params[key] = unquote(value)
    return query_params


def get_request_query_params(request):
    """获取HTTP请求中的查询参数

    参数:
        request: HTTP请求字符串

    返回:
        包含查询参数的字典
    """
    # 获取查询字符串
    query_string = get_request_query_string(request)
    # 解析查询字符串并返回参数字典
    return parse_query_string(query_string)


def get_request_post_params(request):
    """获取POST请求中的参数

    参数:
        request: HTTP请求字符串

    返回:
        包含POST参数的字典，如果不是POST请求则返回None
    """
    # 获取请求方法
    request_method = get_request_method(request)
    # 如果不是POST请求，则返回None
    if request_method != "POST":
        return None
    # 使用正则表达式匹配请求体中的参数（两个换行符后的所有内容）
    match = re.search("\r\n\r\n(.+)", request)
    # 如果没有匹配到请求体，则返回空字典
    if match is None:
        return {}
    # 获取查询字符串部分
    query_string = match.group(1)
    # 解析查询字符串并返回参数字典
    return parse_query_string(query_string)


def unquote(string):
    """URL解码函数，将%编码的字符转换回原始字符

    参数:
        string: 需要解码的字符串

    返回:
        解码后的字符串
    """
    # 如果字符串为空，则返回空字符串
    if not string:
        return ""

    # 如果是字符串类型，则先编码为字节
    if isinstance(string, str):
        string = string.encode("utf-8")

    # 按%分割字符串
    bits = string.split(b"%")
    # 如果没有%分割符，说明没有需要解码的内容，直接返回原字符串
    if len(bits) == 1:
        return string.decode("utf-8")

    # 初始化结果字节数组
    res = bytearray(bits[0])
    append = res.append
    extend = res.extend

    # 遍历分割后的每一块内容
    for item in bits[1:]:
        try:
            # 将前两个字符解析为十六进制数（即%后面的编码），并添加到结果中
            append(int(item[:2], 16))
            # 将剩余部分添加到结果中
            extend(item[2:])
        except KeyError:
            # 如果解析出错，则按原样添加
            append(b"%")
            extend(item)

    # 将结果字节解码为字符串并返回
    return bytes(res).decode("utf-8")


def get_cookies(request):
    """从HTTP请求中获取Cookie信息

    参数:
        request: HTTP请求字符串

    返回:
        包含Cookie键值对的字典
    """
    # 将请求按行分割
    lines = request.split("\r\n")
    cookie_string = None
    # 遍历每一行，查找Cookie头部
    for line in lines:
        # 如果行中包含冒号，说明是HTTP头部
        if line.find(":") is not -1:
            header, value = line.split(":", 1)
            # 如果是Cookie头部，则保存Cookie字符串
            if header.lower() == "cookie":
                cookie_string = value
    # 初始化Cookie字典
    cookies = {}
    # 如果找到了Cookie字符串
    if cookie_string:
        # 按分号和空格分割每个Cookie项
        for cookie in cookie_string.split("; "):
            # 按等号分割Cookie的键和值
            name, value = cookie.strip().split("=", 1)
            # 存入Cookie字典
            cookies[name] = value

    return cookies


def create_cookie(name, value, path="/", domain=None, expires=None):
    """创建Cookie头部信息

    参数:
        name: Cookie名称
        value: Cookie值
        path: Cookie的有效路径，默认为根路径"/"
        domain: Cookie的有效域名，默认为None
        expires: Cookie的过期时间，默认为None

    返回:
        格式化的Cookie头部字符串
    """
    # 构建基础Cookie字符串
    cookie = "Set-Cookie: " + str(name) + "=" + str(value)
    # 如果指定了路径，则添加路径信息
    if path:
        cookie = cookie + "; path=" + path
    # 如果指定了域名，则添加域名信息
    if domain:
        cookie = cookie + "; domain=" + domain
    # 如果指定了过期时间，则添加过期时间信息
    if expires:
        cookie = cookie + "; expires=" + expires

    return cookie
