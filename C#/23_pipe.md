# 管道

管道（Pipes）通常指的是一种用于在进程之间或线程之间传递数据的通信机制。
它可以在两个进程或线程之间建立连接，以便它们可以同步传递信息。

- 服务器端：`NamedPipeServerStream`
- 客户端：`NamedPipeClientStream`

## 匿名管道

匿名管道适用于同一个父进程的两个子进程之间的通信。
简单轻量，但有局限性，无法跨网络或不同的父进程使用。

使用匿名管道的步骤：

- 创建管道：
使用 `AnonymousPipeServerStream` 和 `AnonymousPipeClientStream` 类创建服务器和客户端的管道。
- 传输数据：
通过 `PipeStream` 的 `Write()` 和 `Read()` 方法进行数据传输。

下面的示例展示了如何使用匿名管道将字符串从父进程发送到子进程。
本示例在父进程中创建一个 `AnonymousPipeServerStream` 对象，其 `PipeDirection` 值为 `Out`。
然后，父进程通过使用客户端句柄创建 `AnonymousPipeClientStream` 对象来创建子进程。
子进程的 `PipeDirection` 值为 `In`。

接下来，父进程将用户提供的字符串发送给子进程。
字符串在子进程的控制台中显示。

### 编译顺序

创建服务端程序 `dotnet new console -n PipeServer`
创建客户端程序 `dotnet new console -n pipeClient`

先在 `pipeClient` 中，使用 `dotnet publish -c Release -r win-x64 --self-contained -p:PublishSingleFile=true` 编译客户端程序。
先在 `PipeServer` 中，使用 `dotnet publish -c Release -r win-x64 --self-contained -p:PublishSingleFile=true` 编译服务端程序。

然后将 `pipeClient\bin\Release\net8.0\win-x64\publish` 中生成的 `pipeClient.exe`
与 `PipeServer\bin\Release\net8.0\win-x64\publish` 中生成的 `PipeServer.exe`
放在同一个目录下。

```sh
$ ./PipeServer.exe
[SERVER] Current TransmissionMode: Byte.
[CLIENT] Current TransmissionMode: Byte.
[CLIENT] Wait for sync...
[SERVER] Enter text: 123
[CLIENT] Echo: 123
[CLIENT] Press Enter to continue...
[SERVER] Client quit. Server terminating.
```

### PipeServer

```cs
using System;
using System.IO;
using System.IO.Pipes;
using System.Diagnostics;

class PipeServer
{
    static void Main()
    {
        Process pipeClient = new Process();

        pipeClient.StartInfo.FileName = "pipeClient.exe";

        using (AnonymousPipeServerStream pipeServer =
            new AnonymousPipeServerStream(PipeDirection.Out,
            HandleInheritability.Inheritable))
        {
            Console.WriteLine("[SERVER] Current TransmissionMode: {0}.",
                pipeServer.TransmissionMode);

            // Pass the client process a handle to the server.
            pipeClient.StartInfo.Arguments =
                pipeServer.GetClientHandleAsString();
            pipeClient.StartInfo.UseShellExecute = false;
            pipeClient.Start();

            pipeServer.DisposeLocalCopyOfClientHandle();

            try
            {
                // Read user input and send that to the client process.
                using (StreamWriter sw = new StreamWriter(pipeServer))
                {
                    sw.AutoFlush = true;
                    // Send a 'sync message' and wait for client to receive it.
                    sw.WriteLine("SYNC");
                    pipeServer.WaitForPipeDrain();
                    // Send the console input to the client process.
                    Console.Write("[SERVER] Enter text: ");
                    sw.WriteLine(Console.ReadLine());
                }
            }
            // Catch the IOException that is raised if the pipe is broken
            // or disconnected.
            catch (IOException e)
            {
                Console.WriteLine("[SERVER] Error: {0}", e.Message);
            }
        }

        pipeClient.WaitForExit();
        pipeClient.Close();
        Console.WriteLine("[SERVER] Client quit. Server terminating.");
    }
}
```

### PipeClient

下面的示例展示了客户端进程。
服务器进程启动客户端进程，并为此进程提供客户端句柄。
客户端代码生成的可执行文件应命名为 `pipeClient.exe`，并在运行服务器进程前复制到服务器可执行文件所在的相同目录中。

```cs
using System;
using System.IO;
using System.IO.Pipes;

class PipeClient
{
    static void Main(string[] args)
    {
        if (args.Length > 0)
        {
            using (PipeStream pipeClient =
                new AnonymousPipeClientStream(PipeDirection.In, args[0]))
            {
                Console.WriteLine("[CLIENT] Current TransmissionMode: {0}.",
                   pipeClient.TransmissionMode);

                using (StreamReader sr = new StreamReader(pipeClient))
                {
                    // Display the read text to the console
                    string temp;

                    // Wait for 'sync message' from the server.
                    do
                    {
                        Console.WriteLine("[CLIENT] Wait for sync...");
                        temp = sr.ReadLine();
                    }
                    while (!temp.StartsWith("SYNC"));

                    // Read the server data and echo to the console.
                    while ((temp = sr.ReadLine()) != null)
                    {
                        Console.WriteLine("[CLIENT] Echo: " + temp);
                    }
                }
            }
        }
        Console.Write("[CLIENT] Press Enter to continue...");
        Console.ReadLine();
    }
}
```

## 命名管道

命名管道可以在不同的进程之间、甚至跨网络使用。
与匿名管道不同，它们有一个唯一的名称，便于多个客户端连接。

使用命名管道的步骤：

- 创建管道：
使用 `NamedPipeServerStream` 和 `NamedPipeClientStream` 类创建服务器和客户端的管道。
- 等待客户端连接：
服务器端调用 `WaitForConnection()` 来等待客户端连接。
- 传输数据：
和匿名管道类似，通过 `Write()` 和 `Read()` 进行数据传输。

### 服务端

```cs
using System;
using System.IO;
using System.IO.Pipes;

class NamedPipeServer
{
    static void Main()
    {
        using (var pipeServer = new NamedPipeServerStream("testpipe", PipeDirection.Out))
        {
            Console.WriteLine("Waiting for client connection...");
            pipeServer.WaitForConnection();
            using (var writer = new StreamWriter(pipeServer))
            {
                writer.AutoFlush = true;
                writer.WriteLine("Hello from the server");
            }
        }
    }
}
// Waiting for client connection...
```

### 客户端

```cs
using System;
using System.IO;
using System.IO.Pipes;

class NamedPipeClient
{
    static void Main()
    {
        using (var pipeClient = new NamedPipeClientStream(".", "testpipe", PipeDirection.In))
        {
            Console.WriteLine("Connecting to server...");
            pipeClient.Connect();
            using (var reader = new StreamReader(pipeClient))
            {
                string message = reader.ReadLine();
                Console.WriteLine($"Received from server: {message}");
            }
        }
    }
}
// Connecting to server...
// Received from server: Hello from the server
```
