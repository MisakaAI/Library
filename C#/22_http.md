# 网络操作

- `WebClient`：用于处理简单的 HTTP 请求，常用于下载文件或发送数据。
- `HttpClient`：用于处理复杂的 HTTP 请求，包括发送和接收 JSON、XML 等格式的数据。

如果你正在开发现代C#应用程序，建议使用 `HttpClient`。

## 发送 GET 请求

```cs
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
         // 确保控制台输出支持 UTF-8 编码
        Console.OutputEncoding = System.Text.Encoding.UTF8;

        // 启用 Gzip 自动解压缩
        var handler = new HttpClientHandler()
        {
            AutomaticDecompression = System.Net.DecompressionMethods.GZip
        };

        // 创建 HttpClient 实例
        using (HttpClient client = new HttpClient(handler))
        {
            // 定义请求 URL
            string url = "https://devapi.qweather.com/v7/weather/now?lang=en&location=118.12,24.43&key=YOUR_KEY";

            // 发送 GET 请求并获取响应
            HttpResponseMessage response = await client.GetAsync(url);

            // 确保请求成功
            if (response.IsSuccessStatusCode)
            {
                // 确认编码
                var charset = response.Content.Headers.ContentType?.CharSet;
                Console.WriteLine(charset);

                // 读取响应内容
                var r = await response.Content.ReadAsStringAsync();
                Console.WriteLine(r);
            }
            else
            {
                Console.WriteLine($"请求失败: {response.StatusCode}");
            }
        }
    }
}
```

## 发送 POST 请求

```cs
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // 创建 HttpClient 实例
        using (HttpClient client = new HttpClient())
        {
            // 定义请求 URL 和请求数据
            string url = "https://api.example.com/submit";
            string jsonData = "{\"name\":\"John\",\"age\":30}";

            // 创建请求内容（设置为 JSON 格式）
            StringContent content = new StringContent(jsonData, Encoding.UTF8, "application/json");

            // 发送 POST 请求
            HttpResponseMessage response = await client.PostAsync(url, content);

            // 确保请求成功
            if (response.IsSuccessStatusCode)
            {
                // 读取响应内容
                string responseData = await response.Content.ReadAsStringAsync();
                Console.WriteLine(responseData);
            }
            else
            {
                Console.WriteLine($"请求失败: {response.StatusCode}");
            }
        }
    }
}
```
