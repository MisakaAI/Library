# Aagent2

- [使用手册](https://www.zabbix.com/documentation/6.0/zh/manual/concepts/agent2)
- [下载](https://www.zabbix.com/cn/download_agents?version=6.0+LTS&release=6.0.13&os=Windows&os_version=Any&hardware=amd64&encryption+=OpenSSL&packaging=Archive&show_legacy=0&encryption=No+encryption)


1. 修改 `zabbix_agent2.conf`

```conf
# 服务器IP
Server=127.0.0.1
ServerActive=127.0.0.1

# 本机主机名（唯一）
Hostname=Windows host
```

2. 将 Zabbix agent 安装为 Windows 服务

```powershell
.\zabbix_agent2.exe -c zabbix_agent2.conf -i

## 参数
# -c --config <config-file> 配置文件的绝对路径。
# -p --print 输出已知的监控项并退出。
# -t --test <item key> 测试指定的监控项并退出。
# -h --help 显示帮助信息
# -V --version 显示版本信息

## 仅 Windows agent
# -i --install 以服务的形式安装 Zabbix Windows agent。
# -d --uninstall 卸载 Zabbix Windows agent 服务。
# -s --start 启动 Zabbix Windows agent 服务。
# -x --stop 停止 Zabbix Windows agent 服务。
```

3. `Win+R` 运行 `services.msc`

4. 启动 `Zabbix Agent 2`

5. 防火墙放行端口 `10050`

```txt
(1) 防火墙和网络保护
(2) 高级设置
(3) 入站规则
(4) 新建规则
(5) 端口
(6) TCP - 10050
(7) 允许连接
```
