# luck_clock

"luck_clock_node"は, ROS 2を使用して１秒毎ランダムに「Dead」または「Alive」のメッセージをトピック"luck_clock_topic"にパブリッシュするノードです.「Alive」と連続でパブリッシュしている時間が長いほど正確に現在時刻も表示されます.

## 必要条件

- ROS 2 Humble
- Python 3.10

## 使用方法

### クローン
このリポジトリをクローンします.
```Bash
git clone https://github.com/0Haruto/fifty-fifty.git
```

### 実行
1. "luck_clock"ノードを実行します.
```Bash
ros2 run fifty_fifty luck_clock
```

2. 別のターミナルを開き, トピック"luck_clock_topic"からメッセージを受信します.
```Bash
ros2 topic echo /luck_clock_topic
```

## コードの説明
"luck_clock.py"
このスクリプトは, ランダムに「Dead」または「Alive」のメッセージをパブリッシュするROS 2ノードを実装しています.
- "dead_or_alive()"関数は, ランダムに"True"または"False"を返します.
- timemsg()関数は, "dead_or_alive()"関数が"True"の時に「Dead」の文字とそれまでに「Dead」が出た回数（試行回数）を含んだメッセージ, "dead_or_alive()"関数が"False"の時に「Alive」の文字とその時の確率, 現在の日時を含んだメッセージを作成し パブリッシュします.
- "main()"関数は, ノードを初期化し, タイマーを作成して"timemsg()"関数を1秒毎に呼び出します.

## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for details.


