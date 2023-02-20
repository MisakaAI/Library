#!/bin/bash

source /etc/os-release

if [ "$ID" != "ubuntu" ]
then
	echo Error, $ID not is ubuntu.
    exit 0
fi

if [ ! -f /etc/apt/sources.list.bak ]
then
    sudo cp -a /etc/apt/sources.list /etc/apt/sources.list.bak
else
    sudo cp -a /etc/apt/sources.list.bak /etc/apt/sources.list
fi

mirrors() {
    echo "Please set source."
    echo '0. Ubuntu - cn.archive.ubuntu.com'
    echo '1. TUNA - mirrors.tuna.tsinghua.edu.cn'
    echo '2. Aliyun - mirrors.aliyun.com'
    echo '3. Huawei - repo.huaweicloud.com'
    read mode
}

mirrors

while [ $mode != 0 ] && [ $mode != 1 ] && [ $mode != 2 ] && [ $mode != 3 ]
do
    mirrors
done

if [ $mode == 1 ]
then
    sudo sed -i "s@http://.*archive.ubuntu.com@https://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list
    sudo sed -i "s@http://.*security.ubuntu.com@https://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list
elif [ $mode == 2 ]
then
    sudo sed -i "s@http://.*archive.ubuntu.com@https://mirrors.aliyun.com@g" /etc/apt/sources.list
    sudo sed -i "s@http://.*security.ubuntu.com@https://mirrors.aliyun.com@g" /etc/apt/sources.list
elif [ $mode == 3 ]
then
    sudo sed -i "s@http://.*archive.ubuntu.com@http://repo.huaweicloud.com@g" /etc/apt/sources.list
    sudo sed -i "s@http://.*security.ubuntu.com@http://repo.huaweicloud.com@g" /etc/apt/sources.list
fi

sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y