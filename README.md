# eurekaインターン前半課題

## 目次

- テーマ設定
- 各種ワードの説明
- 方法
- 計測条件
- デフォルト結果
- チューニング
- 改善点
- 次にやりたいこと

## テーマ設定

各文庫の50行のデータを特徴量として、出版社を分類する。
今回は、岩波書店か、ちくま文庫の分類問題である。

出版社によって、作家を採用する基準が異なるのではないかと考えた。
よって、分類問題を解くことによって基準があるかどうかを判断することができると考えテーマを設定した。

自分が本を購入するか選ぶときは、最初の数ページを見てから判断するため、全文章からではなく、一定の行数を特徴量として捉えればいいのではないかと考えてたため、50行のデータをとった

## Stopword

役に立たない情報

ex.助動詞、助詞

## Bag of Words

文章に単語が含まれているかどうかのみを考え、単語の並び方を考慮しないモデル

## TF-IDF

文書中に含まれる単語の重要度を評価する手法

## LSI(潜在的意味インデキシング)

高次元の行列データを次元圧縮するための手法

LSIの特徴として、出現頻度の低いものから指定した次元数基づき次元を圧縮する。

テーマに関して、出版社によって関連ワードがあると思ったためLSIを選定した。

[潜在的意味インデキシング（LSI）徹底入門](https://abicky.net/2012/03/24/211818/)

## 方法

### データ整形

各種シェルコマンドを駆使し、大量のデータから各出版社ごとのファイルを作成

```
aozora_word_list_utf8.csv(11819行) > tikuma.txt(965行)  1 / 10ぐらい
utf8_all.csv(87701673行) >  utf8_iwanami.txt(1145929行) 1 / 75ぐらい
```

Stopwordを用いて、学習に邪魔な単語を除去

結果として、データ数が1710となった。

### モデル

三種類の学習モデルを公式ドキュメントを見て、一般的な形にして精度を計測した結果SVMがよかった

その後、SVMのチューニングを試した

## 計測条件

bag of wordsとTF-IDF組み合わせ文章の分散表現を得る

LSIで次元の圧縮を行い、200次元にする

データの標準化を行う

訓練データ: テストデータ = 8 : 2

100回の平均値をとる

全ての学習モデルはパラメータは公式のサイトのサンプルコードとする

## シンプルな結果

### サポートベクターマシン

データ数 814
```
正解率 0.853086419753
精度 0.827951029892
検出率 0.889742940214
F値 0.856738459335
```

データ数 1710
```
正解率 0.894017595308
精度 0.898894259526
検出率 0.911991241483
F値 0.905122037767
```

### ランダムフォレスト

データ数 814
```
正解率 0.764320987654
精度 0.797706546766
検出率 0.700258606916
F値 0.743572530543
```

データ数 1710
```
正解率 0.753460410557
精度 0.74482934547
検出率 0.838209324053
F値 0.787985012345
```

## SVMチューニング結果

```
linear
------------------
正解率 0.866568914956
精度 0.887514073488
検出率 0.866718675909
F値 0.876694894379
------------------
poly
------------------
正解率 0.791700879765
精度 0.940843856684
検出率 0.673149892024
F値 0.775105811495
------------------
rbf
------------------
正解率 0.898885630499
精度 0.90469428534
検出率 0.912423391024
F値 0.908262177742
------------------
sigmoid
------------------
正解率 0.851260997067
精度 0.867847000912
検出率 0.861240922296
F値 0.86410664437
------------------
```

[sklearn.svm.SVC](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)

## 改善点

現在、データのカット処理は出現回数が4以下、全データのうち30%以上を含むを条件として行っている。
各データの単語の出現回数を調べ、共通して出現する単語が出現頻度が高い場合はStopwordに含めると、よりデータ間の違いが際立つのではないかと考える。

## 次にやりたいこと

- word2vecなど単語の位置情報を考慮した方法を試し、精度の差をみる

- 多値分類の結果をみる

- 各種パラーメータ変更によってなぜ、精度が変化したのか調べる

- GPUを使いたいので、DeepLearningをやりたい

## 感想

データを整形するのに最も、時間がかかるのを体感した。


## データを試した方
```
increase.all.zipを展開し
increase_data/increase.allという構成になるようにする

python main.py
```

## tips

[StopWordの除去](http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt)

complete.corpus*で削除した文字
```
\u3000
```

```
cat utf8_delete_over50.txt | grep -f iwanami.url
cat test.txt | rev | cut  -f 1 -d "," | rev
cat utf8_delete_over50.txt | grep -f iwanami.url >> utf8_iwanami.txt
```
