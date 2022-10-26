# 适用于 Linux 的 Windows 子系统

[文档](https://learn.microsoft.com/zh-cn/windows/wsl/)

WSL 当前的默认版本为2，如果需要用到网卡相关功能，记得将WSL版本换成1。

## 安装

[安装](https://learn.microsoft.com/zh-cn/windows/wsl/install)

必须启用“适用于 Linux 的 Windows 子系统”可选功能并重启，然后才能在 Windows 上运行 Linux 发行版。

```PowerShell
# 以管理员身份打开 PowerShell 并运行
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

## 基本命令

[基本命令](https://learn.microsoft.com/zh-cn/windows/wsl/basic-commands)

```PowerShell
# 列出可用的 Linux 发行版
wsl -l -o

# 列出已安装的 Linux 发行版
wsl -l -v

# 指定发行版
wsl --install -d <Distribution Name>

# 将 WSL 版本设置为 1 或 2
wsl --set-version <distribution name> <versionNumber>

# 设置默认 WSL 版本
wsl --set-default-version <Version>

# 设置默认 Linux 发行版
wsl --set-default <Distribution Name>

# 将目录更改为主页
wsl ~

# 更新 WSL
wsl --update

# 检查 WSL 状态
wsl --status

# 关闭
wsl --shutdown

# 注销或卸载 Linux 发行版
wsl --unregister <DistributionName>

# 装载磁盘或设备
wsl --mount <DiskPath>
```
