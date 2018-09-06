# eureka_one

# 計測条件

bag of wordsとTF-IDF組み合わせ文章の分散表現を得る

LSI(潜在的意味インデキシング)で次元の圧縮を行い、200次元にする

データの標準化を行う

訓練データ: テストデータ = 8 : 2

100回の平均値をとる

全ての学習モデルはパラメータは公式のサイトのサンプルコードとする

## サポートベクターマシン
```
正解率 0.853086419753
精度 0.827951029892
検出率 0.889742940214
F値 0.856738459335
```

## ランダムフォレスト
```
正解率 0.764320987654
精度 0.797706546766
検出率 0.700258606916
F値 0.743572530543
```

## 確率的勾配降下法
```
正解率 0.850740740741
精度 0.85359337175
検出率 0.842762287573
F値 0.847312487853
```

# tips

[StopWordの除去](http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt)

complete.corpus*で削除した文字
\u3000

cat utf8_delete_over50.txt | grep -f iwanami.url
cat test.txt | rev | cut  -f 1 -d "," | rev
cat utf8_delete_over50.txt | grep -f iwanami.url >> utf8_iwanami.txt