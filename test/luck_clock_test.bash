#!/bin/bash
# SPDX-FileCopyrightText: 2025 Haruto Yamamoto
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# ノードの実行とログの保存
timeout 10 bash -c "source $dir/.bashrc && ros2 run fifty_fifty luck_clock" &
sleep 5

timeout 10 bash -c "ros2 topic echo /luck_clock_topic" > /tmp/fifty_fifty.log

echo "Log file content:"
cat /tmp/fifty_fifty.log
if grep -q 'Starting trials' /tmp/fifty_fifty.log; then
    echo "Starting trials found in log"
    exit 0
else
    echo "Starting trials not found in log"
    exit 1
fi

