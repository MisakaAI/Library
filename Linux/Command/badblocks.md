# badblocks

`badblocks` 是一个用于在Linux系统上检测磁盘坏块的命令行工具。
它可以扫描指定的块范围，检查磁盘上的物理坏块，并报告检测到的问题。

```sh
# badblocks -b 4096 -s -v /dev/sda > badsectors.txt
badblocks -b 4096 -s -v /dev/sda
```

- `-b` 4096: 指定块大小为 4096 字节（4KB）。
这表示 badblocks 在检查过程中将以 4KB 为单位进行块的检测。
- `-s`: 显示扫描进度。
这个选项会让 badblocks 在运行时显示进度条，以便你可以看到检测进度。
- `-v`: 显示详细输出。
当这个选项被指定时，badblocks 将输出更详细的信息，包括每个检测到的坏块的位置和状态。
