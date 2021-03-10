#!/bin/bash
# This script installs all the dependencies necessary for running an OpenPose bodytracking algorithm
# on the Jetson Nano with a Microsoft Kinect camera.
# Alexa Jakob, Fall 2020

# install Microsoft Kinect SDK
# This step is not required, but is useful to troubleshoot by accessing the camera
# This part written by Andy Jeong and provides a low-cost bodytracking algorithm with the Kinect SDK;
# However it is not currently supported on ARM boards

# ====setting up environment====

# configure keys for Ubuntu 18.04
 curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
 sudo apt-add-repository https://packages.microsoft.com/ubuntu/18.04/prod
 sudo apt-get update

# install via (1) or (2)
# (1) ====install kinect sdk====
sudo apt install k4a-tools							# viewer, recorder, firmware tool
sudo apt install libk4a1.4 libk4a1.4-dev 

# (2) ====installing from source code====
git clone --recursive https://github.com/microsoft/Azure-Kinect-Sensor-SDK.git
cd Azure-Kinect-Sensor-SDK
git checkout release/1.4.x

# install necessary packages
sudo dpkg --add-architecture arm64
sudo apt update
sudo apt install -y \
    pkg-config \
    ninja-build \
    doxygen \
    clang \
    gcc-multilib \
    g++-multilib \
    python3 \
    python3-pip \
    nasm

sudo apt install -y \
    libgl1-mesa-dev \
    libsoundio-dev \
    libvulkan-dev \
    libx11-dev \
    libxcursor-dev \
    libxinerama-dev \
    libxrandr-dev \
    libusb-1.0-0-dev \
    libssl-dev \
    libudev-dev \
    mesa-common-dev \
    uuid-dev

# ninja-build
sudo apt-get install ninja-build

# openssl
sudo apt-get install libssl-dev

# x11
sudo apt-get install libx11-dev

#randr library
sudo apt-get install xorg-dev libglu1-mesa-dev

mkdir build && cd build
zzcmake .. -GNinja
ninja

# if depth engine (for depth camera) is missing, download this:
#depth engine file (backup): https://drive.google.com/open?id=1nryM1mghLDAp64F-RMdruirotcDH7U6c
#copy to Azure-Kinect-Sensor-SDK/build/bin

#copy rules so one can use without being 'root'
sudo cp Azure-Kinect-Sensor-SDK/scripts/99-k4a.rules /etc/udev/rules.d/

# ====increase USB bandwidth for multiple Kinects===
sudo sh -c 'echo 64 > /sys/module/usbcore/parameters/usbfs_memory_mb'

# ====run with viewer/recorder====
#cd Azure-Kinect-Sensor-SDK/build/bin
#k4aviewer
#k4abt_simple_3d_viewer



# install GStreamer1.0
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo apt-get update
sudo apt-get install gstreamer1.0-tools gstreamer1.0-alsa \
	 gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
	 gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
	 gstreamer1.0-libav
sudo apt-get install libgstreamer1.0-dev \
	 libgstreamer-plugins-base1.0-dev \
	 libgstreamer-plugins-good1.0-dev \
	 libgstreamer-plugins-bad1.0-dev
gst-inspect-1.0 --version # should be version 1.14

# install CMake
sudo apt-get install build-essential
wget https://github.com/Kitware/CMake/releases/download/v3.19.1/cmake-3.19.1.tar.gz
tar xf cmake-3.19.1.tar.gz
cd cmake-3.19.1
./configure — qt-gui
./bootstrap && sudo make -j$(nproc) && sudo make install -j$(nproc)

# ===== install OpenCV with GStreamer ====
sudo apt update
pip3 install numpy

git clone https://github.com/opencv/opencv.git
cd opencv/
git checkout 4.1.0

git clone https://github.com/opencv/opencv.git
cd opencv/
git checkout 4.1.0

mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D PYTHON_EXECUTABLE=$(which python3) \
-D BUILD_opencv_python2=OFF \
-D CMAKE_INSTALL_PREFIX=$(python3 -c “import sys; print(sys.prefix)”) \
-D PYTHON3_EXECUTABLE=$(which python3) \
-D PYTHON3_INCLUDE_DIR=$(python3 -c “from distutils.sysconfig import get_python_inc; print(get_python_inc())”) \
-D PYTHON3_PACKAGES_PATH=$(python3 -c “from distutils.sysconfig import get_python_lib; print(get_python_lib())”) \
-D WITH_GSTREAMER=ON \
-D BUILD_EXAMPLES=ON ..

sudo make -j$(nproc) # this will take a while, go get a coffee or something
sudo make install
sudo ldconfig


# ======= install OpenPose =========
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose

# install caffe dependencies
cd openpose
sudo bash ./scripts/ubuntu/install_cuda.sh
sudo bash ./scripts/ubuntu/install_cudnn.sh
sudo bash ./scripts/ubuntu/install_deps.sh

cd openpose/3rdparty
git clone https://github.com/CMU-Perceptual-Computing-Lab/caffe.git
cd openpose
mkdir build

# open GUI

cd openpose/build/
make -j`nproc`

cd openpose/build/
sudo make install

cd openpose/build/python/openpose
sudo make install
