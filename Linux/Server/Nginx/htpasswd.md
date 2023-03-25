# 基本登录认证

## 安装

`htpasswd` 是开源 http 服务器 `apache httpd` 的一个命令工具，用于生成 http 基本认证的密码文件。

```bash
# 安装
dnf install httpd-tools

# 使用

# -c 创建加密文件
# -n 不更新文件，在标准输出上显示结果
# -b 在命令行中一并输入用户名和密码而不是根据提示输入密码。
# -p 不对密码进行加密，即明文密码
# -m 默认采用 MD5 算法进行加密
# -d 采用 CRYPT 算法对密码进行加密
# -s 采用 SHA算法对密码进行加密
# -D 删除指定的用户

htpasswd -cm .passwd <username>
```
