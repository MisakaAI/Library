# WebDAV

Windows 自带的共享功能只能在局域网内网使用，而 WebDAV 既可以内网也可以外网使用，并可以使用习惯的 Windows 自带的资源管理器来管理文件。

## 启用 WebClient 服务

运行 `services.msc` - WebClient 设为自动

## 停止 WebClient 服务

```sh
net stop webclient
```

## 修改注册表

保存为 `.reg` 文件，并执行。

```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameters]
"BasicAuthLevel"=dword:00000002
"FileSizeLimitInBytes"=dword:ffffffff
```

## 重新启动 WebClient 服务

```sh
net start webclient
```

## 映射磁盘

1. 在 Windows 资源管理器空白处右键，选添加一个网络位置
2. 填写正确的连接地址、端口号及目录（如果有目录的话）
3. 在之后的对话框填写用户名密码（建议勾选保存密码凭据）
