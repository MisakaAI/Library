# 套接字

使用 `Socket` 类来进行 TCP/IP 通信。

- **服务器端**：监听特定的IP和端口，等待客户端连接。接收到客户端消息后，发送响应。
- **客户端**：连接服务器并发送消息，接收到服务器响应后显示。

## 流程

1. 启动服务器端，等待客户端连接。
2. 客户端连接到服务器并发送消息。
3. 服务器接收消息并发送响应。
4. 客户端接收服务器的响应。

## 服务器端

```cs
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class TCPServer
{
    static void Main()
    {
        // 定义服务器IP和端口
        IPAddress ipAddress = IPAddress.Parse("127.0.0.1");
        int port = 8080;

        // 创建一个监听的套接字 (Socket)
        Socket listener = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

        // 绑定IP地址和端口
        listener.Bind(new IPEndPoint(ipAddress, port));

        // 开始监听，最多允许10个连接排队
        listener.Listen(10);

        Console.WriteLine("等待客户端连接...");

        // 接受连接
        Socket handler = listener.Accept();

        // 接收数据
        byte[] buffer = new byte[1024];
        int bytesReceived = handler.Receive(buffer);
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesReceived);

        Console.WriteLine("接收到的数据: " + dataReceived);

        // 发送响应
        string response = "Hello from server!";
        byte[] responseBytes = Encoding.UTF8.GetBytes(response);
        handler.Send(responseBytes);

        // 关闭连接
        handler.Shutdown(SocketShutdown.Both);
        handler.Close();
    }
}
```

## 客户端

```cs
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class TCPClient
{
    static void Main()
    {
        // 定义服务器的IP和端口
        IPAddress ipAddress = IPAddress.Parse("127.0.0.1");
        int port = 8080;

        // 创建一个客户端套接字 (Socket)
        Socket sender = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

        try
        {
            // 连接到服务器
            sender.Connect(new IPEndPoint(ipAddress, port));

            Console.WriteLine("连接到服务器...");

            // 发送数据
            string message = "Hello from client!";
            byte[] messageBytes = Encoding.UTF8.GetBytes(message);
            sender.Send(messageBytes);

            // 接收服务器的响应
            byte[] buffer = new byte[1024];
            int bytesReceived = sender.Receive(buffer);
            string response = Encoding.UTF8.GetString(buffer, 0, bytesReceived);

            Console.WriteLine("服务器响应: " + response);

            // 关闭连接
            sender.Shutdown(SocketShutdown.Both);
            sender.Close();
        }
        catch (Exception e)
        {
            Console.WriteLine("异常: " + e.ToString());
        }
    }
}
```
