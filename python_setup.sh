#!/bin/bash

sudo apt update -y
sudo apt install python3
python3 --version
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
cd /tmp
wget https://www.python.org/ftp/python/3.12.1/Python-3.12.1.tgz
tar -xf Python-3.12.1.tgz
./configure --enable-optimizations
sudo make install
python3 --version
