#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Haruto Yamamoto
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

rclpy.init()
node = Node('luck_clock_node')
pub = node.create_publisher(String, 'luck_clock_topic', 10)
n = 0
x = 0
z = 1
random_trials = 0
current_trial = 0
timer_handle = None

# exerciseリスト
exercise_list = [
    "10回のジャンプ",
    "1分間のプランク",
    "5回のスクワット",
    "10回の腕立て伏せ",
    "10回の腹筋",
    "10回の背筋",
    "アームグリップ15回",
    "ダンベル上げ10回ずつ"
]

# relaxリスト
relax_list = [
    "深呼吸を3回する",
    "目を1分間閉じる",
    "首をゆっくり1回まわす",
    "肩を5回上げ下げする",
    "1分間の休憩を取る",
    "1分間手のマッサージ",
    "1分間耳のマッサージ"
]

def true_or_false():
    return random.choice([True, False])

def timemsg():
    global n, x, z, random_trials, current_trial, timer_handle
    now = datetime.now()
    year_month_day_hour_minute_second = now.strftime("%Y-%m-%d %H:%M:%S")
    msg = String()

    random_trials = random.randint(1, 7)
    msg.data = f"Starting trials: {random_trials}  Now: {year_month_day_hour_minute_second}"
    pub.publish(msg)
    x = 0
    n = 0
    z = 1
    current_trial = 0  # 試行回数をリセット

    timer_handle = node.create_timer(1, list)

def list():
    global n, x, z, random_trials, current_trial, timer_handle
    msg = String()
    if current_trial < random_trials:
        if true_or_false():
            relax = random.choice(relax_list)
            x += 1
            z = z / 2
            msg.data = f"Time to chill!!     Relax: {relax}"
            pub.publish(msg)

            if z <= 0.0625 and x == random_trials:
                msg.data = f"Wow all relax time!!       Probability: {z}"
                pub.publish(msg)

        else:
            exercise = random.choice(exercise_list)
            n += 1
            z = z / 2
            msg.data = f"Keep moving!!       Exercise: {exercise}"
            pub.publish(msg)

            if z <= 0.0625 and n == random_trials:
                msg.data = f"Wow all exercise time!!    Probability: {z}"
                pub.publish(msg)

        current_trial += 1
    else:
        msg.data = "All trials completed."
        pub.publish(msg)
        if timer_handle is not None:
            timer_handle.cancel()  # タイマーを停止

def main():
    node.create_timer(10, timemsg)
    rclpy.spin(node)

if __name__ == "__main__":
    main()

