# 第６回
## ゲーム製作(ex06/game.py)
### ゲーム概要
- ex06/game.pyを実行すると、1920x1060のスクリーンが表示され、キャラクターをスペースキーでジャンプさせて障害物を避けながら進む横スクロールゲーム
- キャラクターが障害物に接触or穴に落下するとゲーム終了
- クリア条件は現在は設定していない。スコアを競うタイプのゲーム。
### 操作方法
- スペースキーでジャンプ
### 追加機能
- 背景の横スクロール
- ステージの障害物をリストで管理して表示する
- リストの値によって穴を描画
- 障害物（飛んでよける）の岩を描画
- 走るキャラクターを描画
- スペースキーでキャラクターがジャンプ
- 障害物（穴）の上でジャンプしていない（地面に接触している）状態で死亡判定となり、キャラクターが穴の底に落ちて背景スクロールが停止する。
- 障害物（岩）の上でジャンプしていない（岩に接触している）状態で死亡判定となり、背景スクロールが停止する。
### ToDO（実装しようと思ったけどできなかった）
- アイテム
- 障害物（スライディング）
### メモ
- 120×120を１つのマスとし、リストで障害物を管理する
- もっとなめらかなジャンプができるようにコードを組みたい。
- 衝突判定はもっと綺麗なコードが書けると思うので、次回そこを見直したい。
- 穴に落ちる時に、なぜかキャラクターの残像が残ってしまう。今後の課題としたい