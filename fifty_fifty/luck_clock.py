import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

rclpy.init()
node = Node("luck_clock")
pub = node.create_publisher(String, "luck_clock", 10)
n = 1
x = 1
def dead_or_alive():
    return random.choice([True, False])
def cb():
    global n, x
    now = datetime.now()
    year = now.strftime("%Y")
    year_month = now.strftime("%Y-%m")
    year_month_day = now.strftime("%Y-%m-%d")
    year_month_day_hour = now.strftime("%Y-%m-%d %H")
    year_month_day_hour_minute = now.strftime("%Y-%m-%d %H:%M")
    year_month_day_hour_minute_second = now.strftime("%Y-%m-%d %H:%M:%S")
    msg = String()
    if dead_or_alive():
        msg.data = f"Dead  Game Over    Published: {x} trials"
        x += 1
        n = 1

    else:
        n = n / 2
        if n <= 0.015625:
            msg.data = f"Alive  One more time!    Probability: {n}  Now: {year_month_day_hour_minute_second}"
        elif n == 0.03125:
            msg.data = f"Alive  One more time!    Probability: {n}  Now: {year_month_day_hour_minute}"
        elif n == 0.0625:
            msg.data = f"Alive  One more time!    Probability: {n}  Now: {year_month_day_hour}"
        elif n == 0.125:
            msg.data = f"Alive  One more time!    Probability: {n}  Now: {year_month_day}"
        elif n == 0.25:
            msg.data = f"Alive  One more time!    Probability: {n}  Now: {year_month}"
        elif n == 0.5:
            msg.data = f"Alive  One more time!    Probability: {n}  Now: {year}"

    pub.publish(msg)

def main():
    node.create_timer(1, cb)
    rclpy.spin(node)

if __name__ == "__main__":
    main()
