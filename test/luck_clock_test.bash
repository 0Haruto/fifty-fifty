#!/bin/bash

# ディレクトリの設定
dir=~
[ "$1" != "" ] && dir="$1"

# ROS 2ワークスペースに移動
cd $dir/ros2_ws

# colcon buildの実行
colcon build

# .bashrcのソース
source $dir/.bashrc

# ノードの実行とログの保存
timeout 5 ros2 run fifty_fifty luck_clock > /tmp/fifty_fifty.log

# ログファイルから特定の文字列を検索して表示
grep 'Dead' /tmp/fifty_fifty.log || grep 'Alive' /tmp/fifty_fifty.log

