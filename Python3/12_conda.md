# Conda

## 下载

- [官网下载](https://www.anaconda.com/download/success)
- [镜像下载](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=D)

## 软件源镜像站

- [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

### Windows

打开 Anaconda Prompt

```cmd
# 删除默认源
# conda config --remove channels defaults

# 生成配置文件
conda config --set show_channel_urls yes

# 添加源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2

# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/mro

# 显示 Conda 配置的所有来源文件及其内容
conda config --show-sources

# 显示当前 Conda 配置中所有的软件源（channels）
conda config --show channels

# 清除索引缓存
conda clean -i

# 测试创建虚拟环境及安装 numpy
conda create -n myenv numpy
```

## 创建指定版本虚拟环境

```sh
# create 创建虚拟环境
# —name 虚拟环境名称
# python=后面可以指定安装python版本
# conda create -n <环境名称> python=<Python版本>
conda create --name test python=3.10

# 创建时指定目录
# conda create --prefix <路径> python=<Python版本>

# 查看全部虚拟环境
conda env list

# 查看存储虚拟环境的目录
conda info --envs

# 进入虚拟环境
# conda activate <环境名称>
conda activate test

# 进入指定目录下虚拟环境
# conda activate <路径>

# 退出虚拟环境
conda deactivate

# 删除虚拟环境
# conda remove -n <环境名称> --all
conda remove -n test --all
```

## 包管理

```sh
# 查看当前环境中所有已安装的包
conda list

# 安装包
# conda install <包名>
conda install numpy

# 删除包
# conda remove <包名>
conda remove numpy

# 更新包
# conda update <包名>
conda update numpy
```

## Jupyter Lab

```sh
# 安装 Jupyter Lab
conda install jupyterlab

# 安装中文语言包
conda install jupyterlab-language-pack-zh-CN

# 启动
jupyter lab
```
