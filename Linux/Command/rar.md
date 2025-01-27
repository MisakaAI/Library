# RAR

## 安装

```bash
apt install unrar
```

## 解压

```bash
unrar x name.rar

## 参数

# -x 使用完整路径提取文件
# -e 统一将文件解压到一个目录下，不按文件的完整路径解压
# -t 检测压缩文件
# -l 列出压缩文档信息
```

## 爆破

```bash
# 安装
apt install rarcrack

# 使用
rarcrack name.rar --threads 2 --type rar

## 参数

# --threads n 使用线程数
# --type 类型，可以是 7z、zip、rar
```

运行一次会在文件名旁边出现一个 .xml 文件

`<abc>`是字典
`<current>`是指从什么位数开始
