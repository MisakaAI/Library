# 子模块

子模块允许您将一个Git存储库保存为另一个Git存储库的子目录。
这允许您将另一个存储库克隆到您的项目中，并保持您的提交是分开的。

## 添加子模块

使用 `git submodule add` 命令和您想要开始跟踪的项目的绝对或相对URL
添加 `https://github.com/mineraltown/saikai` 到本地 `saikai` 目录

```bash
git submodule add https://github.com/mineraltown/saikai.git saikai
```

## 查看子模块

```bash
# 查看子模块
git submodule
```

## 更新子模块

```bash
# 克隆父项目
git clone https://github.com/mineraltown/wiki

# 初始化子模块
git submodule init

# 更新子模块
git submodule update

# 更新子模块为远程项目的最新版本
git submodule update --remote
```

### 递归克隆整个项目

递归克隆整个项目，同时更新子模块。

```bash
git clone --recurse-submodules https://github.com/mineraltown/wiki
git clone https://github.com/mineraltown/wiki --recursive
```

## 删除子模块

删除子模块目录

```bash
git rm --cached saikai
```

删除 `.gitmodules` 文件中相关子模块信息

```ini
[submodule "saikai"]
  path = saikai
  url = https://github.com/mineraltown/saikai.git
```

删除 `git/config` 中的相关子模块信息

```ini
[submodule "saikai"]
  url = https://github.com/mineraltown/saikai.git
```

删除 `.git` 文件夹中的相关子模块文件

```bash
rm -rf .git/modules/saikai
```

## 参考文献

- [Git-Tools-Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
- [git-submodule](https://www.atlassian.com/git/tutorials/git-submodule)
- [Git submodule 子模块的管理和使用](https://www.jianshu.com/p/9000cd49822c)
