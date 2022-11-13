# Windows

GVLK KEY 由微软官方提供的批量激活密钥。

[GVLK en-us](https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys)
[GVLK zh-cn](https://learn.microsoft.com/zh-cn/windows-server/get-started/kms-client-activation-keys)

## 下载

[Windows 10](https://www.microsoft.com/zh-cn/software-download/windows10)
[Windows 11](https://www.microsoft.com/zh-cn/software-download/windows11)

## 查看系统版本

```PowerShell
wmic os get caption
```

## 卸载秘钥

```PowerShell
slmgr -upk
```

## 使用管理员权限运行PowerShell执行安装key

```PowerShell
# Windows 10 & Windows 11 Pro 专业版
slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX

# Windows 10 & Windows 11 Pro for Workstations 专业版工作站
slmgr /ipk NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J

# Windows 10 & Windows 11 Enterprise 企业版
slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43

# Windows Server 2022 Datacenter
slmgr /ipk WX4NM-KYWYW-QJJR4-XV3QB-6VM33

# Windows Server 2022 Standard
slmgr /ipk VDYBN-27WPP-V4HQT-9VMD4-VMK7H
```

## 设置KMS并激活

```PowerShell
slmgr /skms kms.03k.org
slmgr /ato
```

## 查看KMS信息

```PowerShell
slmgr -dlv
```
