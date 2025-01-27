# 启动流程

## BIOS 引导

### Legacy/传统启动

1. 系统开机 - 上电自检(Power On Self Test 或 POST)。
2. POST过后初始化用于启动的硬件(磁盘、键盘控制器等)。
3. BIOS会运行BIOS磁盘启动顺序中第一个磁盘的首440bytes(MBR启动代码区域)内的代码。
4. 启动引导代码从BIOS获得控制权，然后引导启动下一阶段的代码(如果有的话)(一般是系统的启动引导代码)。
5. 再次被启动的代码(二阶段代码)(即启动引导)会查阅支持和配置文件。
6. 根据配置文件中的信息，启动引导程序会将内核和initramfs文件载入系统的RAM中，然后开始启动内核。 

### UEFI

1. 系统开机 - 上电自检(Power On Self Test 或 POST)。
2. UEFI 固件被加载，并由它初始化启动要用的硬件。
3. 固件读取其引导管理器以确定从何处(比如，从哪个硬盘及分区)加载哪个 UEFI 应用。
4. 固件按照引导管理器中的启动项目，加载UEFI 应用。
5. 已启动的 UEFI 应用还可以启动其他应用(对应于 UEFI shell 或 rEFInd 之类的引导管理器的情况)或者启动内核及initramfs(对应于GRUB之类引导器的情况)，这取决于 UEFI 应用的配置。

## 主引导记录

- Master boot record（MBR）主引导记录，同时也记录硬盘分区信息。（Legacy+MBR）
- GUID Partition Table（GPT）GUID分区表。（UEFI+GPT）

## 硬盘启动

引导加载程序（如GRUB）负责处理文件系统，查找内核映像（比如Linux的vmlinuz）
讲计算机的控制权转交给硬盘的某个分区。

## 操作系统

将内核映像载入内存，再将控制权转交给操作系统内核，内核会继续启动系统的其他部分。

## 其他参考文献

- [UEFI 引导与 BIOS 引导在原理上有什么区别？](https://www.zhihu.com/question/21672895/answer/45616136) 张旭
- [计算机是如何启动的？](https://ruanyifeng.com/blog/2013/02/booting.html) 阮一峰
