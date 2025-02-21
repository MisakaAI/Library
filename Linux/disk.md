# 磁盘与文件系统

## 磁盘分区

### MBR

主引导记录(Master Boot Record)，是传统的分区机制。
不支持超过2TB的硬盘。
至少有1个，最多4个主分区，扩展分区可以没有，最多1个。
且主分区 + 扩展分区总共不能超过四个。
扩展分区可以分为若干逻辑分区，他们的关系是包含的关系，所有的逻辑分区都是扩展分区的一部分。
MBR分区表储存在磁盘的首440bytes内。

### GPT

全局唯一标识分区表(GUID Partition Table)，是一个较新的分区机制，解决了MBR很多缺点。
支持2TB以上的硬盘，分区大小几乎没有限制。
磁盘的分区没有限制，Windows系统中最多只允许划分128个分区。
分区表自带备份，在磁盘的首尾部分分别保存了一份相同的分区表。

## 文件系统

### Windows

- FAT16
MS-DOS和最早期的Win 95操作系统中最常见的磁盘分区格式。
- FAT32
突破了FAT16对每一个分区的容量只有2GB的限制，用于在Win 2000 & XP系统。
- exFAT
适合U盘的文件系统，为了解决FAT32等不支持4G及其更大的文件。
- NTFS
NTFS (New Technology File System)，是 WindowsNT 环境的文件系统。
- ReFS
ReFS 是一个高容错性、可扩展性强的文件系统，特别适用于企业级存储解决方案、云存储以及需要高数据完整性保障的场合。
但它并不是完全取代 NTFS 的设计，是针对特定使用场景进行了优化。

### Linux

- EXT2 / ETX3 / EXT4
Ext是 GNU/Linux 系统中标准的文件系统。
Ext3是一种日志式文件系统，是对ext2系统的扩展。
Ext4 是 Ext3 的改进版，修改了 Ext3 中部分重要的数据结构。
- Btrfs
Oracle于2007年宣布并进行中的copy-on-write文件系统，目标是取代Linux目前的ext3文件系统。
- XFS
Sun Microsystems为Solaris操作系统开发的文件系统。ZFS是一个具有高存储容量、文件系统与卷管理概念整合、崭新的磁盘逻辑结构的轻量级文件系统，同时也是一个便捷的存储池管理系统。

### Mac OS

- HFS / HFS+
分层文件系统(Hierarchical File System，HFS)是一种由苹果电脑开发，并使用在Mac OS上的文件系统。
（ macOS 10.12 或之前版本的 Mac）
- APFS
Apple 文件系统 (APFS) 是运行 macOS 10.13 或后续版本的 Mac 电脑所使用的默认文件系统。
它具有强加密、空间共享、磁盘快照、快速目录大小统计等特性，以及改进的文件系统基础。

### Other

- ESP分区
EFI，是Extensible Firmware Interface的词头缩写，直译为可扩展固件接口。
U为是Unified(统一的)，即Unified Extensible Firmware Interface(UEFI)
EFI系统分区(EFI system partition)，简写为 ESP。
支持 EFI 模式的电脑需要从 ESP 启动系统，EFI 固件可从 ESP 加载 EFI 启动程序和应用程序。
通常应该把ESP分区挂在/boot/efi上。
\
推荐 ESP 大小为 512 MiB， 不过大一点小一点都没问题。
根据微软的说明，最少应为100Mib。但是为了4k对齐，至少应该为256Mib。
**fdisk/gdisk**：创建类型为 EFI System `EFI System` (在 fdisk 中) 或 `ef00` (在 gdisk 中)的分区。
然后运行 `mkfs.fat -F32 /dev/<THAT_PARTITION>` 格式化为 FAT32 格式。

- SWAP
Linux中Swap（即：交换分区），类似于Windows的虚拟内存。
就是当内存不足的时候，把一部分硬盘空间虚拟成内存使用。
\
交换分区可以用大多数 GNU/Linux 分区工具(例如 fdisk, cfdisk)创建。交换分区被分配为类型 82。
尽管可以使用任何分区类型作为交换分区，但是在大多数情况下，建议使用 82，因为 systemd 会自动检测并挂载它。
\
*[我需要多大的交换空间？](https://help.ubuntu.com/community/SwapFaq)*

RAM大小|不开启休眠|开启休眠|最大值
-|-|-|-
1|1|2|2
2|1|3|4
3|2|5|6
4|2|6|8
5|2|7|10
6|2|8|12
8|3|11|16
12|3|15|24
16|4|20|32
24|5|29|48
32|6|38|64
64|8|72|128
128|11|139|256
