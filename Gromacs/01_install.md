# 安装 Gromacs

## 下载

- [gromacs manual](https://manual.gromacs.org/)
- [CUDA](https://developer.nvidia.com/cuda-downloads)

## 安装 CUDA

```sh
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-ubuntu2404.pin
sudo mv cuda-ubuntu2404.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/13.0.2/local_installers/cuda-repo-ubuntu2404-13-0-local_13.0.2-580.95.05-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2404-13-0-local_13.0.2-580.95.05-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2404-13-0-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda-toolkit-13-0

sudo apt-get install -y nvidia-open
sudo apt-get install -y cuda-drivers
```

## 编译 && 安装 Gromacs

要求 `cmake ≥ 3.28`

```sh
wget ftp://ftp.gromacs.org/gromacs/gromacs-2025.4.tar.gz
tar xvf gromacs-2025.4.tar.gz
cd gromacs-2025.4

mkdir build
cd build

cmake .. \
  -DGMX_GPU=CUDA \
  -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda \
  -DCMAKE_CUDA_COMPILER=/usr/local/cuda/bin/nvcc \
  -DGMX_BUILD_OWN_FFTW=ON \
  -DREGRESSIONTEST_DOWNLOAD=ON \
  -DGMX_SIMD=AVX_512

make -j$(nproc)
make check
sudo make install
source /usr/local/gromacs/bin/GMXRC
```
