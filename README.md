# luck-clock [![Build Status](https://github.com/0Haruto/fifty-fifty/actions/workflows/test.yml/badge.svg)](https://github.com/0Haruto/fifty-fifty/actions/workflows/test.yml)

`luck_clock_node`は, ROS 2上で動作するノードです. このノードからトピック`luck_clock_topic`にパブリッシュされる運動またはリラックスできる行動が記されたメッセージを実行することで, 短時間で気分転換をすることができます.

## 必要な環境

- ROS 2 Humble

## 使用方法

### 実行

1. `luck_clock`ノードを実行します.

```Bash
ros2 run fifty_fifty luck_clock
```

2. 別のターミナルを開き, トピック`luck_clock_topic`からメッセージを受信します.

```Bash
ros2 topic echo /luck_clock_topic
```

### 実行結果]

- 例として次のような実行結果が得られます.

```
data: 'Starting trials: 7  Now: [現在時刻]'
---
data: 'Time to chill!!     Relax: 目を1分間閉じる'
---
data: 'Keep moving!!       Exercise: 10回のジャンプ'
---
data: 'Time to chill!!     Relax: 首をゆっくり1回まわす'
---
data: 'Time to chill!!     Relax: 目を1分間閉じる'
---
data: 'Keep moving!!       Exercise: 5回のスクワット'
---
data: 'Time to chill!!     Relax: 首をゆっくり1回まわす'
---
data: 'Keep moving!!       Exercise: 1分間のプランク'
---
data: All trials completed.
---
data: 'Starting trials: 1  Now: [現在時刻]'
---
data: 'Keep moving!!       Exercise: 10回のジャンプ'
---
data: All trials completed.
```

## ノード

`luck_clock_node`
- 説明: 最初に試行回数の決定と現在時刻が表示され, 各試行ごとに「Exercise」とexerciseリストまたは「Relax」とrelaxリストのメッセージをランダムでパブリッシュするノードです.
- トピック: `/luck_clock_topic` (パブリッシュ)

## オプション

- それぞれのリスト内容は変更することができます.

```luck_clock_py
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
```

- 以上からリストの内容を追加, 削除することでカスタマイズが可能です.

## 最後に

- パブリッシャノードを実行するスクリプト`luck_clock.py`は10秒毎にノード実行します. また自動的には終了しませんので手動で停止させる必要があります.

- 本パッケージではトピック`/luck_clock_topic`用のサブスクライバノードは作成しておりません. ご了承ください.

## ライセンス

このプログラムはBSD-3-Clauseライセンスの下で配布されています。詳細なライセンス情報については,  [LICENSE](LICENSE)ファイルを参照してください.
