# OpenSSH 安装

## 安装 OpenSSH

[安装](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse)

### 使用 Windows 设置来安装 OpenSSH

可以使用 Windows Server 2019 和 Windows 10 设备上的 Windows 设置安装这两个 OpenSSH 组件。

若要安装 OpenSSH 组件：

1. 打开“设置”，选择“应用”>“应用和功能”，然后选择“可选功能” 。

2. 扫描列表，查看是否已安装 OpenSSH。 如果未安装，请在页面顶部选择“添加功能”，然后：
    - 查找“OpenSSH 客户端”，再单击“安装”
    - 查找“OpenSSH 服务器”，再单击“安装”

设置完成后，回到“应用”>“应用和功能”和“可选功能”，你应会看到已列出 OpenSSH 。

### 使用 PowerShell 安装 OpenSSH

```PowerShell
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```

如果两者均尚未安装，则此操作应返回以下输出：

```PowerShell
Name  : OpenSSH.Client~~~~0.0.1.0
State : NotPresent

Name  : OpenSSH.Server~~~~0.0.1.0
State : NotPresent
```

然后，根据需要安装服务器或客户端组件：

```PowerShell
# Install the OpenSSH Client
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

## 启动并配置 OpenSSH 服务器

若要启动并配置 OpenSSH 服务器来开启使用，请以管理员身份打开 PowerShell，然后运行以下命令来启动 `sshd service`：

```PowerShell
# Start the sshd service
Start-Service sshd

# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
    Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
} else {
    Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
}
```

## 连接到 OpenSSH 服务器

安装后，可从使用 PowerShell 安装了 OpenSSH 客户端的 Windows 10 或 Windows Server 2019 设备连接到 OpenSSH 服务器，如下所示。 请务必以管理员身份运行 PowerShell：

```PowerShell
ssh username@servername
```

## 卸载

### 使用 Windows 设置来卸载 OpenSSH

若要使用 Windows 设置来卸载 OpenSSH：

1. 打开“设置”，然后转到“应用”>“应用和功能” 。
2. 转到“可选功能”。
3. 在列表中，选择“OpenSSH 客户端”或“OpenSSH 服务器” 。
4. 选择“卸载”。

### 使用 PowerShell 卸载 OpenSSH

若要使用 PowerShell 卸载 OpenSSH 组件，请使用以下命令：

```PowerShell
# Uninstall the OpenSSH Client
Remove-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Uninstall the OpenSSH Server
Remove-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

如果在卸载时服务正在使用中，稍后可能需要重启 Windows。
