# Office

GVLK KEY 由微软官方提供的批量激活密钥。
[GVLK en-us](https://learn.microsoft.com/en-us/deployoffice/vlactivation/gvlks)
[GVLK zh-cn](https://learn.microsoft.com/en-us/deployoffice/vlactivation/gvlks)

## 部署

[概述](https://learn.microsoft.com/zh-cn/deployoffice/overview-office-deployment-tool)
[微软Office部署工具](https://www.microsoft.com/en-us/download/details.aspx?id=49117)
[微软Office配置工具](https://config.office.com/)

## 切换到安装目录

### x64

```PowerShell
cd "C:\Program Files\Microsoft Office\Office16"
```

### x86

```PowerShell
cd "C:\Program Files (x86)\Microsoft Office\Office16"
```

## 激活

### Office Professional Plus 2019

```PowerShell
cscript ospp.vbs /inpkey:NMMKJ-6RK4F-KMJVX-8D9MJ-6MWKP
```

### Office Professional Plus 2016

```PowerShell
cscript ospp.vbs /inpkey:XQNVK-8JYDB-WJ9W3-YJ8YR-WFG99
```

## 设置KMS并激活

```PowerShell
cscript ospp.vbs /sethst:kms.03k.org
cscript ospp.vbs /act
```
