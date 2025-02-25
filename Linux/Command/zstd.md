# zstd

- [github](https://github.com/facebook/zstd)

## 省流

```sh
# 压缩
zstd  --ultra --long -T0 -9 file
tar cavf data.tar.zst directory

# 解压
zstd -d file.zst
tar xvf data.tar.zst
```

## 压缩

```sh
# 将一个文件压缩到一个 .zst 后缀的压缩文件中
zstd file

# 压缩后保留源文件(默认)
zstd -k file

# 压缩后删除源文件
zstd --rm file

# 使用指定的压缩等级来压缩一个文件. 0最差 19最好 (默认等级 3)
zstd -3 file

# 使用更多的内存(压缩和解压时)以达到更高的压缩比
zstd --ultra -3 file

# 使用多线程加速(4线程)(默认值1)
zstd -T4 file

# 自动检测 CPU 线程数
zstd -T0 file

# 使用更多的 windowLog 和内存(默认27)
zstd --long file

# tar 打包时使用 zstd (打包目录并压缩)
tar --zstd -cf data.tar.zst directory

# 通过 -a 选项可以让 tar 根据扩展名来自动推断压缩格式
tar caf data.tar.zst directory
```

## 查看

```sh
# 查看zst压缩包
zstd -l file.zst
zstdcat file.zst
```

## 解压

```sh
# 解压缩一个文件
zstd -d file.zst

# 将文件解压缩到标准输出(stdout)
zstd -dc file.zst

# 解压目录
tar --zstd -xf data.tar.zst

# 也可以让 tar 根据扩展名 .zst 来自动推断压缩格式
tar -xf data.tar.zst
```
