#!/bin/bash
# SPDX-FileCopyrightText: 2025 Haruto Yamamoto
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

source $dir/.bashrc

if [ -d "$dir/ros2_ws" ]; then
    cd $dir/ros2_ws
else
    echo "Directory $dir/ros2_ws does not exist."
    exit 1
fi

colcon build

# ノードの実行とログの保存
timeout 20 bash -c "source $dir/.bashrc && ros2 run fifty_fifty luck_clock" &

timeout 20 bash -c "ros2 topic echo /luck_clock_topic" > /tmp/fifty_fifty.log

sleep 20
echo "Log file content:"
cat /tmp/fifty_fifty.log
if grep -q 'Starting trials' /tmp/fifty_fifty.log; then
    echo "Starting trials found in log"
    exit 0
else
    echo "Starting trials not found in log"
    exit 1
fi

