# 基本登录认证

## 安装

`htpasswd` 是一个Apache HTTP Server提供的工具，用于创建和管理基于HTTP身份验证的用户密码文件。

## 安装

```bash
dnf install httpd-tools
```

## 语法

```sh
htpasswd -c <path> <username>

# -c 创建加密文件
# -n 不更新文件，在标准输出上显示结果
# -b 在命令行中一并输入用户名和密码而不是根据提示输入密码。
# -p 不对密码进行加密，即明文密码
# -m 默认采用 MD5 算法进行加密
# -d 采用 CRYPT 算法对密码进行加密
# -s 采用 SHA算法对密码进行加密
# -D 删除指定的用户
```
## 使用

### 创建一个新的密码文件

```bash
htpasswd -c /path/to/password/file username
```

这将创建一个新的密码文件，并将用户名和密码添加到该文件中。如果该文件已经存在，将会覆盖该文件。

### 添加一个新的用户到密码文件

```bash
htpasswd /path/to/password/file username
```
这将添加一个新的用户名和密码到密码文件中。如果该文件不存在，将会创建该文件。

### 删除密码文件中的用户

```bash
htpasswd -D /path/to/password/file username
```
这将从密码文件中删除指定的用户名和密码。

### 更改现有用户的密码

```bash
htpasswd /path/to/password/file username
```

这将提示您输入一个新的密码，并将该密码存储在密码文件中。
注意：为了安全起见，请不要将密码文件放在公共可访问的目录中，并确保其权限正确设置为只有管理员可以读取。

### 使用 bcrypt 算法

另外，请注意htpasswd默认使用的加密算法是MD5，这已经被证明不够安全。
您可以通过在命令行中使用`-B`选项来将加密算法更改为`bcrypt`，例如：

```bash
htpasswd -B /path/to/password/file username
```

这将使用bcrypt算法加密密码。

## Nginx

```conf
location /file {
    auth_basic "Restricted";
    auth_basic_user_file /etc/nginx/htpasswd;
}
```