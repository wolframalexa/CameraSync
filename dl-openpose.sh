#!
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
cd openpose/
git submodule update --init --recursive --remote

#
mkdir build/
cd build/
cmake-gui ..

# do stuff manually with the GUI here

cd build/ 
make -j3

