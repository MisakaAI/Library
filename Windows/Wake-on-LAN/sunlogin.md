# 网络唤醒开机则启动向日葵

## 设置方式

1. PowerShell  更改执行策略

```Powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. 创建开机启动脚本

```Powershell
# 如果开机方式等于网络唤醒，则启动向日葵
if ($(Get-WmiObject -class win32_computersystem).wakeuptype -eq 5) { Start-Process -FilePath "C:\Program Files\Oray\SunLogin\SunloginClient\SunloginClient.exe" }
```

把上面这句命令保存到成一个`.ps1`格式的Powershell脚本

3. 设置计划任务

Win+R 打开启动，输入`taskschd.msc`，打开计划任务程序。
创建任务
常规 - 不管用户是否登录都要运行
常规 - 使用最高权限运行
触发器 - 在系统启动时
操作 - 启用程序 - 程序或脚本 - 添加参数（可选）

```PowerShell
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -file "%HOMEPATH%\Sunlogin.ps1"
```

条件 - 唤醒计算机运行此任务
条件 - 只有在以下网络连接可用时才启动 - 任何连接

## 参考

### [Set-ExecutionPolicy](https://learn.microsoft.com/zh-CN/previous-versions//dd347628(v=technet.10)?redirectedfrom=MSDN)

#### 说明

更改 Windows PowerShell 执行策略的用户首选项。

Set-ExecutionPolicy 可更改 Windows PowerShell 执行策略的用户首选项。
要在 Windows Vista、Windows Server 2008 和 Windows 的更高版本上运行此命令，必须使用“以管理员身份运行”选项启动 Windows PowerShell，即使您是计算机上 Administrators 组的成员。
执行策略是 Windows PowerShell 安全策略的一部分。它确定是否可以加载配置文件（包括 Windows PowerShell 配置文件）和运行脚本，并且确定哪些脚本（如果有）在运行之前必须进行数字签名。
有关详细信息，请参阅 about_Execution_Policies。

#### 参数

```
-ExecutionPolicy <ExecutionPolicy>
为 shell 指定新的执行策略。参数名（“Name”）为可选项。

有效值包括：

-- Restricted：不加载配置文件或运行脚本。默认值为“Restricted”。
-- AllSigned：要求所有脚本和配置文件由可信发布者签名，包括在本地计算机编写的脚本。
-- RemoteSigned：要求从 Internet 下载的所有脚本和配置文件均由可信发布者签名。
-- Unrestricted：加载所有配置文件并运行所有脚本。如果运行从 Internet 下载的未签名脚本，则系统将提示您需要相关权限才能运行该脚本。
-- Bypass：不阻止任何执行项，不显示警告和提示。
-- Undefined：从当前作用域删除当前分配的执行策略。此参数将不会删除在组策略作用域中设置的执行策略。

-Force
禁止显示所有提示。默认情况下，Set-ExecutionPolicy 会在您每次更改执行策略时显示警告。

-Scope <ExecutionPolicyScope>
指定执行策略的作用域。默认值为 LocalMachine。

有效值包括：

-- Process：执行策略仅对当前的 Windows PowerShell 进程起作用。
-- CurrentUser：执行策略仅对当前用户起作用。
-- LocalMachine：执行策略对计算机上的所有用户均起作用。

-Confirm
在执行命令之前提示您进行确认。


-WhatIf
描述如果执行该命令会发生什么情况（无需实际执行该命令）。
```

### [Get-WmiObject](https://learn.microsoft.com/zh-cn/previous-versions/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.0)

#### 说明 

Get-WmiObject 可获取 Windows Management Instrumentation (WMI) 类的实例或可用类的相关信息。

从 PowerShell 3.0 开始，此 cmdlet 已被取代 Get-CimInstance。
该 Get-WmiObject cmdlet 获取 WMI 类的实例或有关可用 WMI 类的信息。 若要指定远程计算机，请使用 ComputerName 参数。 如果指定了 List 参数，则 cmdlet 将获取有关指定的命名空间中可用的 WMI 类的信息。 如果指定了 Query 参数，则 cmdlet 将运行 WMI 查询语言 (WQL) 语句。
该 Get-WmiObject cmdlet 不使用Windows PowerShell远程处理来执行远程操作。 即使计算机不符合Windows PowerShell远程处理的要求，或者未在 Windows PowerShell 中为远程处理配置，也可以使用 cmdlet 的 Get-WmiObjectComputerName 参数。
从 Windows PowerShell 3.0 开始，返回的对象Get-WmiObject__Server属性具有 PSComputerName 别名。 从而可以更轻松地在输出和报告中包含源计算机名称。

#### 参考

```Powershell
# 获取唤醒类型
$(Get-WmiObject -class win32_computersystem).wakeuptype
```

```
唤醒类型

数据类型：uint16
访问类型：Read-only
限定符：MappingStrings（“ SMBIOS|Type 1|System Information|Wake-up Type”）

导致系统启动的事件。

此值来自SMBIOS信息中“系统信息”结构的“唤醒类型”成员。

- Reserved (0) 保留
- Other (1) 其他
- Unknown (2) 未知
- APM Timer (3) APM计时器
- Modem Ring (4) 调制解调器环
- LAN Remote (5) LAN远程
- Power Switch (6) 电源开关
- PCI PME# (7) PCI设备
- AC Power Restored (8) 交流电源已恢复
```

```Powershell
# 获取本地计算机上的进程
Get-WmiObject -Class Win32_Process

# 获取远程计算机上的服务
Get-WmiObject -Class Win32_Service -ComputerName 10.1.4.62

# 获取本地计算机的根命名空间或默认命名空间中的 WMI 类
Get-WmiObject -Namespace "root/default" -List

# 停止远程计算机上的服务
(Get-WmiObject -Class Win32_Service -Filter "name='WinRM'" -ComputerName Server01).StopService()

# 在本地计算机上获取 BIOS
Get-WmiObject -Class Win32_Bios | Format-List -Property *

# 获取远程计算机上的服务
Get-WmiObject Win32_Service -Credential FABRIKAM\administrator -ComputerName Fabrikam
```

### [Start-Process](https://learn.microsoft.com/zh-cn/powershell/module/microsoft.powershell.management/start-process?view=powershell-7.3)

#### 说明

启动本地计算机上的一个或多个进程。

cmdlet Start-Process 在本地计算机上启动一个或多个进程。 默认情况下， Start-Process 会创建一个新进程，该进程继承当前进程中定义的所有环境变量。
若要指定进程中运行的程序，请输入可执行文件或脚本文件，或者可以使用计算机上的程序打开的文件。 如果指定非可执行文件， Start-Process 则启动与该文件关联的程序，类似于 Invoke-Item cmdlet。
可以使用 的参数 Start-Process 指定选项，例如加载用户配置文件、在新窗口中启动进程或使用备用凭据。

#### 参考

```Poewershell
# 启动使用默认值的进程
Start-Process -FilePath "sort.exe"

# 打印文本文件
Start-Process -FilePath "myfile.txt" -WorkingDirectory "C:\PS-Test" -Verb Print

# 启动一个进程，以对项进行排序并返回到新文件
$processOptions = @{
    FilePath = "sort.exe"
    RedirectStandardInput = "TestSort.txt"
    RedirectStandardOutput = "Sorted.txt"
    RedirectStandardError = "SortError.txt"
    UseNewEnvironment = $true
}
Start-Process @processOptions

# 在最大化窗口中启动进程
Start-Process -FilePath "notepad" -Wait -WindowStyle Maximized

# 以管理员身份启动 PowerShell
Start-Process -FilePath "powershell" -Verb RunAs
```

