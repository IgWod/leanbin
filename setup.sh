#!/bin/bash

# Copyright 2024 Igor Wodiany
# Licensed under the Apache License, Version 2.0 (the "License")

sudo apt update && sudo apt upgrade
sudo apt install build-essential libelf-dev ruby cmake pkg-config python3-dev libcapstone-dev python3-pip texinfo

# Build Unicorn

cd unicorn; mkdir build; cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j
cd ../../

# Build MAMBO Trace

cp -r mambo-trace/plugins/trace/ mambo/plugins/
cp mambo-trace/mambo.patch mambo/
cd mambo/
git apply mambo.patch
make
cd ../

# Build MAMBO Lift

cd mambo-lift/
git submodule update --init --recursive
make
cd ../

# Install ropper

pip3 install ropper

# Install binutils 2.38

wget https://sourceware.org/pub/binutils/releases/binutils-2.38.tar.gz
tar xf binutils-2.38.tar.gz
rm binutils-2.38.tar.gz
cd binutils-2.38/
./configure
make -j
cd ..

