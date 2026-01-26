# OpenDroneMap

无人机影像摄影测量与三维重建

- [OpenDroneMap](https://opendronemap.org/)
- [Github](https://github.com/OpenDroneMap/ODM)
- [OpenDroneMap](https://docs.opendronemap.org/zh/)

## 安装

```sh
docker pull opendronemap/odm
```

## 使用

### DJI 文件说明

- `DJI_*.JPG` 航拍照片
- `DJI_*_PPKNAV.nav` 航线数据文件
- `DJI_*_PPKOBS.obs` 是实时转码出的Rinex观测值文件
- `DJI_*_PPKRAW.bin` RTCM3.2 MSM5格式的移动端卫星观测值数据及星历数据
- `DJI_*_Timestamp.MRK` 是ASCII格式的明码曝光时间戳记录文件

#### MRK 文件说明

第一列：照片的编号
第二列：每张照片曝光时刻的UTC时间，以GPS时间格式表示时的周内秒部分。
第三列：每张照片曝光时刻的UTC时间，以GPS时间格式表示时的GPS周部分。
第四列：每张照片曝光时刻瞬间天线相位中心到相机CMOS传感器中心的在北方向（N）的偏差，单位为毫米，CMOS中心在天线相位中心偏北方向为正，偏南方向为负。
第五列：每张照片曝光时刻瞬间天线相位中心到相机CMOS传感器中心的在东方向（E）的偏差，单位为毫米，CMOS中心在天线相位中心偏东方向为正，偏西方向为负。
第六列：每张照片曝光时刻瞬间天线相位中心到相机CMOS传感器中心的在垂直方向（V）的偏差，单位为毫米，CMOS中心在天线相位中心偏下为正，偏上为负。
第七列：曝光时刻获取的CMOS中心的实时位置纬度（Lat），单位为度。当飞机定位处于RTK模式下时，此时的位置为RTK位置加上曝光时刻天线相位中心到CMOS中心的位置，精度为RTK精度（厘米级）；当飞机定位处于GPS模式下时，此时的位置为GPS单点定位位置加上曝光时刻天线相位中心到CMOS中心的位置，精度为GPS单点定位的精度（米级）
第八列：曝光时刻获取的CMOS中心的实时位置经度（Lon），单位为度。
第九列：曝光时刻获取的CMOS中心的实时高度，单位为米。该高度为大地高（俗称椭球高），（用户自行定义其椭球模型，默认为WGS84，用户可以通过接入不同的CORS站系统/基准，设定其为其他椭球，如CGCS2000）表面的高度。注意，此高度并非基于国家85高程基准或56高程基准（正常高），也并非基于全球范围内比较通用的EGM96/2008高程基准（正高）。
第十至十二列：北、东、天三个方向定位结果的标准差，表征在三个方向上定位的相对精度。单位为米
第十三列：RTK状态位，0-无定位，16-单点定位模式，34-RTK浮点解，50-RTK固定解。当某张照片标志位不为50的时候，不推荐使用此照片直接进行建图。

### 预处理

使用 [generate_geo.py](generate_geo.py)，从 DJI MRK 文件生成 ODM `geo.txt` 坐标文件

```txt
EPSG:4326
DJI_20260113143425_0001.JPG 119.94303658 35.85436725 26.296 0.0030 0.0030 0.0076
```

- `EPSG:4326` 坐标参考系声明：WGS84
- `图像文件名` 必须与 `images/` 目录中的文件名 **完全一致**
- `Longitude`（相机曝光瞬间的 **经度**，单位：度（WGS84））*（小数 8 位 ≈ 毫米级表达精度）*
- `Latitude`（相机曝光瞬间的 **纬度**，单位：度（WGS84））
- `Ellipsoidal Height`（相机曝光瞬间的 **高程**（单位：米）*通常是 **椭球高**，不是正高（海拔）*
- `σX` 经度方向标准差，X 方向不确定度（单位：米）
- `σY` 纬度方向标准差，Y 方向不确定度（单位：米）
- `σZ` 高程标准差，垂直方向不确定度（单位：米）

ODM 会自动检测项目目录中的 `geo.txt` 文件并使用它。
只需要确保 `geo.txt` 文件放在照片同一目录下，挂载整个目录到 Docker 容器。

### 生成 GeoTIFF 图片

mv ./DJI_202601131429 ./project/images

```sh
docker run -it --rm \
    -v /mnt/d/Data/DJI_Test/datasets:/datasets \
    opendronemap/odm \
    --project-path /datasets \
    project \
    --dsm \
    --dtm \
    --cog \
    --orthophoto-resolution 2 \
    --feature-quality ultra \
    --pc-quality ultra \
    --gps-accuracy 0.01
```

- `docker run` 启动一个新的容器
- `-it` 交互式终端
- `--rm` 容器退出后自动删除
- `-v` 数据挂载 宿主机目录:容器内目录
- `opendronemap/odm` 容器镜像
- `--project-path /datasets` 指定 ODM 项目的根目录
- `project`
- `--dsm` 生成 DSM（Digital Surface Model），数字表面模型，包含建筑、树木、车辆等所有表面
- `--dtm` 生成 DTM（Digital Terrain Model），数字地形模型，尝试去除建筑、植被，只保留地形
- `--cog` 将输出 GeoTIFF 转为 COG（Cloud Optimized GeoTIFF）云优化 GeoTIFF
- `--orthophoto-resolution 2` 正射影像地面分辨率（单位：厘米/像素）
- `--feature-quality ultra`: 特征提取质量
- `--pc-quality ultra`: 点云质量
- `--use-3dmesh`: 使用3D网格
- `--gps-accuracy 0.01`: GPS精度（PPK约1cm）

### GPU加速

需要使用 `opendronemap/odm:gpu` 镜像并且需要传递 `--gpus all` 标志

```sh
docker run --gpus all opendronemap/odm:gpu
```

测试 Docker 是否识别 GPU

```sh
docker run --rm --gpus all nvidia/cuda:10.0-base nvidia-smi
```

### 生成文件

处理完成后，输出会在 `/datasets/project/` 下生成：

```txt
  /datasets/project/
    ├── images/
    ├── odm_orthophoto/← 正射影像
    ├── odm_dem/           ← DEM数据
    └── odm_report/        ← 处理报告
```

## WebODM

- [WebODM](https://docs.webodm.org/)

```sh
git clone https://github.com/OpenDroneMap/WebODM --config core.autocrlf=input --depth 1
cd WebODM

# 启动
./webodm.sh start
# 停止
./webodm.sh stop
# 更新
./webodm.sh update
```

打开浏览器访问 [http://localhost:8000](http://localhost:8000)
