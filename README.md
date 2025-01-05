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

## ノード
`luck_clock_node`
- 説明: ランダムに「Dead」または「Alive」のメッセージをパブリッシュするノードです。
- トピック: `/luck_clock_topic` (パブリッシュ)

## 最後に
- このトピック用のサブスクライバノードは作成しておりません. ご了承ください.

## ライセンス

このプログラムはBSD-3-Clauseライセンスの下で配布されています。詳細なライセンス情報については,  [LICENSE](LICENSE)ファイルを参照してください.
