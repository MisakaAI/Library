# 使用 vlmcsd 部署 KMS 服务器

- [vlmcsd](https://github.com/Wind4/vlmcsd)

## 下载文件

- [releases](https://github.com/Wind4/vlmcsd/releases)

下载的vlmcsd压缩包，找到intel目录下的所有文件解压到 `C:\KMS`

## 防火墙

防火墙放行1688端口的TCP协议的流量

## 安装服务

在 `C:\KMS` 目录下直接运行 `CMD`

```powershell
# 将 vlmcsd-Windows-x64.exe 设置为NT服务
vlmcsd-Windows-x64.exe -s -l C:\KMS\KMS_Service.log

# 查看系统多出一个名为Key Management Server服务
sc query state= inactive | findstr /c:"Key Management Server"

# 启动 Key Management Server 服务
net start "Key Management Server"
```

## 查看 Key Management Server 是否已经启动

打开 `services.msc` ，找到 `Key Management Server` 查看状态。

## 验证安装是否成功

在 `C:\KMS` 目录下直接运行 `CMD`

```cmd
vlmcs-Windows-x64.exe
```

出现回显 `successful` 说明安装成功

## 参考文献

- [使用 vlmcsd 部署 KMS 服务器](https://blog.csdn.net/qq_21453783/article/details/120389942)