# Windows 10 无法休眠

## 查看支持的模式

```PowerShell
powercfg -a
```

- S0 正常。
- S1 CPU停止工作。唤醒时间：0秒。
- S2 CPU关闭。唤醒时间：0.1秒。
- S3 除了内存外的部件都停止工作。唤醒时间：0.5秒。
- S4 内存信息写入硬盘，所有部件停止工作。唤醒时间：30秒。（休眠状态）
- S5 关闭。

注册表选择AwayModeEnabled值，右键删除或修改其数值数据为0即可。

```regedit
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power
```
