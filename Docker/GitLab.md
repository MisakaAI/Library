# GitLab

[GitLab Docker映像](https://docs.gitlab.com/ee/install/docker.html)

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
docker run --detach \
  --hostname gitlab.example.com \
  --publish 443:443 --publish 80:80 --publish 22:22 \
  --name gitlab \
  --restart always \
  --volume $GITLAB_HOME/config:/etc/gitlab \
  --volume $GITLAB_HOME/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/data:/var/opt/gitlab \
  --shm-size 256m \
  gitlab/gitlab-ee:latest
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
