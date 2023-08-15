# Git 服务器

## 服务端

```bash
# 安装Git
apt install git

# 创建一个 git 用户
sudo adduser git

# 使用 git-shell ，可以禁用 shell 登录
chsh -s /usr/bin/git-shell git

# 一句话解决全部问题
useradd git -g git -r -m -s /usr/bin/git-shell
## -g 指定用户所属的起始群组

# 初始化 Git 仓库
# --bare 裸库，只保存 git 提交的版本信息。
# 即普通仓库中 .git 目录下的内容。
git init --bare sample.git

# 修改仓库权限
chown -R git:git sample.git
```

## 客户端

```bash
# 创建SSH Key
ssh-keygen -t rsa -b 4096 -C "youremail@example.com"

# id_rsa		私钥，不可泄漏
# id_rsa.pub	公钥
# 把 id_rsa.pub 添加到服务端 /home/git/.ssh/authorized_keys 中


# 克隆一个仓库
git clone git@server:/home/git/sample.git
```