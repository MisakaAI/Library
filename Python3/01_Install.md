# 安装

## 类 Unix

[在类 Unix 环境下使用 Python](https://docs.python.org/zh-cn/3.10/using/unix.html)

### Linux

开箱即用：Python 预装在大多数 Linux 发行版上，并作为一个包提供给所有其他用户。

```bash
# Debian / Ubuntu
apt update python3

# Red Hat / CentOS / Fedora
dnf install python3
```

## Windows

下一步*N，最后点完成。

[在 Windows 上使用 Python](https://docs.python.org/zh-cn/3.10/using/windows.html)

- [完整安装程序](https://www.python.org/downloads/windows/)
- [Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)
- [华为云](https://mirrors.huaweicloud.com/python/)
- [阿里云](https://mirrors.aliyun.com/python-release/windows/)

> 关于 Windows 7
>
> 最后一个支持 `Windows7` 的 `Python3` 版本是 `3.8.10`
> 需要安装 `vc_redist` 才可以使用。
> 或安装 Windows更新补丁 `Windows6.1-KB2999226-x64` 和 `Windows6.1-KB3063858-x64`

## MacOS

啊……我没有 Mac。

### FreeBSD & OpenBSD

没用过，这里摘抄一下官网的说明。

```bash
# FreeBSD
pkg install python3

# OpenBSD
pkg_add -r python
pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/<insert your architecture here>/python-<version>.tgz
```

### 编译安装

最硬核的 Python 安装方法。

1. 获取 [源代码](https://www.python.org/downloads/source/)
2. 编译安装

#### 在 Linux 上编译 Python

```bash
# 在 Linux 上编译 Python
./configure --enable-optimizations --with-lto
make -j $(nproc)
make install
```

#### 在 Windows 上编译 Python (MSVC)

```powershell
# Developer PowerShell for VS 2022
.\PCbuild\build.bat -c Debug
.\PCbuild\build.bat
# .\rt.bat -q
```

## 参考文献

- [Setup and building](https://devguide.python.org/getting-started/setup-building/index.html)
- [编译参数](https://docs.python.org/zh-cn/3.10/using/configure.html)