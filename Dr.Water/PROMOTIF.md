# PROMOTIF

PROMOTIF 是一个用于分析蛋白质结构特征的软件。
它通过读取 PDB 坐标文件，识别蛋白质中的各种结构模体。

可以分析以下结构特征：

- Secondary structure (二级结构)
- Disulphide bridges (二硫键)
- Beta turns (β 转角)
- Gamma turns (γ 转角)
- Helical geometry (螺旋几何结构)
- Helical interactions (螺旋之间的相互作用)
- Main chain hydrogen bonding patterns (主链氢键模式)
- Beta strands (β 链)
- Beta bulges (β 鼓包)
- Beta hairpins (β 发夹)
- Beta alpha beta units (β-α-β 单元)
- Psi loops (Ψ loops)
- Beta sheet topology (β 片层拓扑结构)

也可用于比较多个相关结构，例如 NMR 结构集合。

**该程序对学术用户免费开放；工业用户需直接联系作者。**

## 平台

本文使用 Windows 11 的 [适用于 Linux 的 Windows 子系统（WSL）](https://learn.microsoft.com/zh-cn/windows/wsl/install)
Linux 系统版本为 `Debian 13 (trixie)`

> 也可以用 [MSYS2](https://www.msys2.org/) 编译和运行
>
> ```sh
> # MSYS2 MINGW64
> pacman -S mingw-w64-x86_64-gcc-fortran
> pacman -S tcsh
> ```

## 编译

```sh
# 安装依赖 FORTRAN 编译器和 CSH 解释器
apt install gfortran tcsh

# 解压 promotif.tar.gz
tar xvf promotif.tar.gz

# 切换文件目录
cd promotif

# 编译程序
source gcompile.scr
```

根据编译器的不同，您可能会看到一些编译警告。
但只要以下可执行文件被成功创建，则一切正常：

```txt
p_bulge2
p_disulph2
p_hairpin2
p_helix3
p_hera2
p_sheet2
psplot2
psplot3
p_sssum3
p_sstruc2
p_turn2
```

## 使用

### 定义环境变量 promotifdir 和 promotif

其中 `directory` 是指可执行文件及脚本文件 `promotif.scr` 所在的位置。

C-shell:

```csh
setenv promotifdir directory
alias promotif $promotifdir/promotif.scr
```

Bash:

```bash
export promotifdir='directory'
alias promotif="$promotifdir/promotif.scr"
```

### 运行程序

切换到任意其他目录并输入 `promotif`。
如果一切设置正确，您将看到错误。
正确用法为：

```sh
promotif <文件名>
```

其中 `<文件名>` 是一个 PDB 格式的坐标文件，运行程序时，PDB 文件需位于当前目录。

### 运行结果

运行 `promotif 8s7z_monitor.pdb`

#### 主输出：整体结构的文本表格

- `8s7z_monitor.sum`       ← 最终汇总文件，每个 motif（螺旋、β链、β夹、β转角等）数量、范围、序号。
- `8s7z_monitor.str`       ← 更细节的结构列表，比 `.sum` 更“碎片化”。
- `8s7z_monitor.sst`       ← 二级结构表，是一种矩阵风格的表示方式，行是氨基酸序号，列是结构类型。

#### 针对特定结构类型的文本输出

每个文件通常包含结构段的起止残基号、类型、以及几何参数（倾斜角、氢键、扭曲度等）。

- `8s7z_monitor.hlx`       ← 各个螺旋（α-helix, 3-10 helix）
- `8s7z_monitor.hpin`      ← β-hairpins
- `8s7z_monitor.sht`       ← β-sheets
- `8s7z_monitor.bab`       ← βαβ motifs
- `8s7z_monitor.gturns`    ← γ-turns
- `8s7z_monitor.bturns`    ← β-turns
- `psi`                    ← φ/ψ 二维角度分析
- `phipsi.mat`             ← 一个角度矩阵文件（程序内部使用）
- `promotif2.prm`          ← 参数文件（判定 helix、turn 的阈值）

#### PostScript 图文件（.ps）

promotif 年代古老，它习惯把所有视图以 PostScript 输出。
这些图可以用 Ghostscript、evince、或 macOS 的预览打开。
如果在 Windows 侧操作，也可以靠：[GSview](https://www.ghostgum.com.au/software/gsview.htm)

- `8s7z_monitor_helix_diag01.ps` 关系图1
- `8s7z_monitor_helix_diag02.ps` 关系图2
- `8s7z_monitor_helix_geom01.ps` 几何分布
- `8s7z_monitor_helix_int01.ps` 氢键交互图
- `8s7z_monitor_helix_tab01.ps` 表格

类似的，hairpin、sheet、bulges、turns 都有对应的图

- `8s7z_monitor_hairpin_01.ps`
- `8s7z_monitor_hairpin_tab01.ps`
- `8s7z_monitor_bulges_01.ps`
- `8s7z_monitor_bulg_tab01.ps`
- `8s7z_monitor_sheets_tab01.ps`
- `8s7z_monitor_strands_tab01.ps`
- `8s7z_monitor_summary_01.ps`
- `8s7z_monitor_motifs_tab01.ps`

每一类 ps 文件都提供了这种结构的视觉化展示。

##### PostScript 转换为 PDF

```sh
# 安装依赖 Ghostscript
sudo apt install ghostscript

# 转换一个 .ps 文件
gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=output.pdf input.ps
```

将下面的 Shell 脚本保存到 `/usr/local/bin/ps2pdf`
之后可直接通过命令 `ps2pdf` 进行批量转换。

```bash
#!/bin/bash
for f in *.ps; do
    gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile="${f%.ps}.pdf" "$f"
done
```

#### β-bulges（β鼓包结构）数据

- `8s7z_monitor.blg` 原始数据
- `8s7z_monitor.blgplt` 绘图数据，中间文件，用于生成上面那些 .ps 图。

## 参考文献

- [PROMOTIF v 2.0](https://www.uoxray.uoregon.edu/local/manuals/promotif/document_2.html)
- [PDBsum Generate](https://www.ebi.ac.uk/thornton-srv/databases/pdbsum/Generate.html)
