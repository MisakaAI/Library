# tar

tar（英文全拼：Tape Archive / 磁带归档）命令用于备份文件。
tar 是用来建立，还原备份文件的工具程序，它可以加入，解开备份文件内的文件。

## 打包

-c 创建新的tar文件
-f 使用文件名(必填)
-C 先进入指定的目录，再释放
-p 打包时保留原始文件及目录的权限
-P 用于保持原始文件的绝对路径
-r 附加新的文件到tar文件中
-v 显示所有进程
-k 不覆盖已有的文件

```bash
# tar 打包 file 文件/目录 到 name.tar
tar -cvf name.tar file

# 使用 -C 指定目录后 打包时不包含多余路径
tar cvf /data/backup/test.tar.gz -C /data/a/b directory
```

## 解包

-x 解开tar文件
-t 列出tar文件中包含的文件的信息
-C 先进入指定的目录，再释放

```bash
tar -xvf 2.tar.xz -C /var/file
```

## 压缩

-z,--gzip 使用 gzip 格式
-j,--bzip2 使用 bz2 格式
-J,--xz 使用 xz 格式
-[0-9] 压缩比

```bash
tar -cvJf -9 1.tar.xz file
```

## 参考文献

[菜鸟教程](https://www.runoob.com/linux/linux-comm-tar.html)
[鸟哥的Linux私房菜](https://linux.vbird.org/linux_basic/centos7/0240tarcompress.php#pack)