# luck-clock [![Build Status](https://github.com/0Haruto/fifty-fifty/actions/workflows/test.yml/badge.svg)](https://github.com/0Haruto/fifty-fifty/actions/workflows/test.yml)

`luck_clock_node`は, ROS 2を使用して１秒毎, ランダムに「Dead」または「Alive」のメッセージをトピック`luck_clock_topic`にパブリッシュするノードです.「Alive」と連続でパブリッシュしている時間が長いほど正確に現在時刻も表示されます.

## 必要条件

- ROS 2 Humble
- Python 3.10

## 使用方法

### クローン
- このリポジトリをクローンします.
```Bash
git clone https://github.com/0Haruto/fifty-fifty.git
```

### 実行
1. `luck_clock`ノードを実行します.
```Bash
ros2 run fifty_fifty luck_clock
```

2. 別のターミナルを開き, トピック`luck_clock_topic`からメッセージを受信します.
```Bash
ros2 topic echo /luck_clock_topic
```
### 実行結果
- 例として次のような実行結果が得られます.
```
data: 'Alive  One more time!    Probability: 0.5  Now: 2025'
---
data: 'Alive  One more time!    Probability: 0.25  Now: 2025-01'
---
data: 'Dead  Game Over    Published: 1 trials'
---
data: 'Alive  One more time!    Probability: 0.5  Now: 2025'
---
data: 'Dead  Game Over    Published: 2 trials'
---
```
- `Alive`が続けて表示されるほど現在時刻が詳細に見れるようになります. また, １度でも途切れると初期段階の情報に戻ります.

## ノードの説明
`luck_clock.py`
このスクリプトは, ランダムに「Dead」または「Alive」のメッセージをパブリッシュするROS 2ノードを実装しています.
- `dead_or_alive()`関数は, ランダムに`True`または`False`を返します.
- `timemsg()`関数は, `dead_or_alive()`関数が`True`の時に「Dead」の文字とそれまでに「Dead」が出た回数（試行回数）を含んだメッセージ, `dead_or_alive()`関数が`False`の時に「Alive」の文字とその時の確率, 現在の日時を含んだメッセージを作成し パブリッシュします.
- `main()`関数は, ノードを初期化し, タイマーを作成して`timemsg()`関数を1秒毎に呼び出します.

## ライセンス

このプログラムはBSD-3-Clauseライセンスの下で配布されています。詳細なライセンス情報については,  [LICENSE](LICENSE)ファイルを参照してください.
