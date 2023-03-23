# Embed

一种Python程序的打包方式。

## 下载 Python Embed 版本

- [downloads](https://www.python.org/downloads/)

下载，文件名类似`python-3.11.0-embed-amd64.zip`

## 使用模块

~~删除 `pythonXX._pth`，`XX` 取决于 `Python` 版本。~~
~~该文件会导致 Python 无法正常导入第三方库。~~

修改 `pythonXX._pth` 文件，在文件中增加

```txt
Lib\site-packages
```

- [finding-modules](https://docs.python.org/zh-cn/3/using/windows.html#finding-modules)

## 安装第三方库

创建目录 `Lib/site-packages`

## 使用 pipreqs 提取项目的依赖

### 安装 pipreqs

```bash
pip install pipreqs
```

### 执行 pipreqs

```bash
pipreqs . --encoding=utf-8
```

### 安装依赖到 embed

```bash
pip install -r requirements.txt -t python-3.10.4-embed-amd64/Lib/site-packages
# -t : 将依赖安装到指定目录
```

## 执行程序

创建文件 `start.bat`

```bat
@echo off
python-3.10.4-embed-amd64\python.exe main.py
```

打开文件执行程序

```cmd
.\start.bat
```

## 参考文献

- [知乎](https://zhuanlan.zhihu.com/p/557884165)