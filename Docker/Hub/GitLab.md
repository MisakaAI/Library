# GitLab

[GitLab Docker](https://docs.gitlab.com/ee/install/docker/installation.html)

## 下载镜像

```sh
docker pull gitlab/gitlab-ce:latest
```

## 设置卷位置

配置一个新的环境变量 `$GITLAB_HOME` 指向配置、日志和数据文件将驻留的目录。
确保目录存在并且已授予适当的权限。
将路径设置为 `/srv/gitlab`

```sh
export GITLAB_HOME=/srv/gitlab
```

GitLab容器使用主机挂载卷来存储持久数据：

本地位置 | 容器位置 | 用途
-|-|-
$GITLAB_HOME/data | /var/opt/gitlab | 用于存储应用程序数据。
$GITLAB_HOME/logs | /var/log/gitlab | 用于存储日志。
$GITLAB_HOME/config | /etc/gitlab | 用于存储GitLab配置文件。

## 安装

```sh
sudo docker run --detach \
  --hostname gitlab.example.com \
  --publish 8929:8929 --publish 2289:22 \
  --name gitlab \
  --restart always \
  --volume $GITLAB_HOME/config:/etc/gitlab \
  --volume $GITLAB_HOME/ssl:/etc/gitlab/ssl \
  --volume $GITLAB_HOME/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/data:/var/opt/gitlab \
  --shm-size 256m \
  gitlab/gitlab-ce:latest

# --publish 443:443 --publish 80:80 --publish 22:22 \
```

## 修改默认的配置文件

### 进入到容器中

```sh
sudo docker exec -it gitlab /bin/bash
```

### 设置 external_url

使用编辑器打开`/etc/gitlab/gitlab.rb`

```rb

#配置http协议所使用的访问地址,不加端口号默认为80
external_url "https://gitlab.example.com:8929"

# 配置ssh协议所使用的访问地址和端口
gitlab_rails['gitlab_ssh_host'] = 'gitlab.example.com'

# 此端口是容器运行时，22端口所映射的2289端口
gitlab_rails['gitlab_shell_ssh_port'] = 2289
```

### 容器中 > 重新配置GitLab

```sh
gitlab-ctl reconfigure
```

#### SMTP设置

QQ exmail (腾讯企业邮箱)

```rb
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.exmail.qq.com"
gitlab_rails['smtp_port'] = 465
gitlab_rails['smtp_user_name'] = "xxxx@xx.com"
gitlab_rails['smtp_password'] = "password"
gitlab_rails['smtp_authentication'] = "login"
gitlab_rails['smtp_enable_starttls_auto'] = false
gitlab_rails['smtp_tls'] = true
gitlab_rails['gitlab_email_from'] = 'xxxx@xx.com'
gitlab_rails['smtp_domain'] = "exmail.qq.com"
```

#### 手动配置HTTPS

禁用 Let's Encrypt 集成

```rb
letsencrypt['enable'] = false
```

创建`/etc/gitlab/ssl`目录并将密钥和证书复制到该目录

```sh
sudo mkdir -p /etc/gitlab/ssl
sudo chmod 755 /etc/gitlab/ssl
sudo cp gitlab.example.com.key gitlab.example.com.crt /etc/gitlab/ssl/
```

重定向 HTTP 请求 HTTPS

```sh
nginx['redirect_http_to_https'] = true
```

##### 更改默认SSL证书位置

如果您的主机名是`gitlab.example.com`，则Linux软件包安装查找名为`/etc/gitlab/ssl/gitlab.example.com.key`的私钥
和一个名为`/etc/gitlab/ssl/gitlab.example.com.crt`的公共证书
在默认情况下，要设置SSL证书的其他位置，请执行以下操作

创建一个目录，给予适当的权限，并将 目录中的`.crt`和`.key`文件：

```sh
sudo mkdir -p /mnt/gitlab/ssl
sudo chmod 755 /mnt/gitlab/ssl
sudo cp gitlab.key gitlab.crt /mnt/gitlab/ssl/
```

编辑`/etc/gitlab/gitlab.rb`

```rb
nginx['ssl_certificate'] = "/mnt/gitlab/ssl/gitlab.crt"
nginx['ssl_certificate_key'] = "/mnt/gitlab/ssl/gitlab.key"
```

### 容器中 > 重启服务

```sh
gitlab-ctl restart
```

## 登录

使用用户名 `root` 和以下命令中的密码进行登录：

```sh
docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
```

## 解决内网无法修改及验证电子邮件的问题

```bash
# 进入 容器内部
# 打开 psql
gitlab-psql

# 查询用户ID
SELECT id, username, email FROM users WHERE username='root';

# 通过ID 修改邮箱
UPDATE users SET email='admin@example.com' WHERE id=1;

# 退出
\q

# 重启 gitlab 服务
gitlab-ctl restart
```
