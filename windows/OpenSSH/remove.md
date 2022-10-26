# 使用 Windows 设置来卸载 OpenSSH

## 若要使用 Windows 设置来卸载 OpenSSH：

1. 打开“设置”，然后转到“应用” > “应用和功能” 。
2. 转到“可选功能”。
3. 在列表中，选择“OpenSSH 客户端”或“OpenSSH 服务器” 。
4. 选择“卸载”。

## 使用 PowerShell 卸载 OpenSSH

```PowerShell
# Uninstall the OpenSSH Client
Remove-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Uninstall the OpenSSH Server
Remove-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```
