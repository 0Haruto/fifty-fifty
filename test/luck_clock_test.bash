#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colconbuild
source $dir/.bashrc
timeout 10 ros2 run fifty_fifty luck_clock > /tmp/fifty_fifty.log

cat /tmp/fifty_fifty.log |
	grep 'Listen: 10'
