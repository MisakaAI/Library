# fdupes

## 安装

```sh
apt-get install fdupes
```

## 使用

```sh
# 扫描目录并列出所有重复文件，-r 递归
fdupes -r /path/to/your/files

# 添加 -d 参数，进入交互式删除模式
fdupes -d -r /path/to/your/files

# 无确认的删除（慎用！）
# 自动保留每组第一个文件，删除其他。
fdupes -d -N -r /path/to/files
```
