# Confidence-Interval-Estimation-for-the-Variance
χ<sup>2</sup>分布を用いた母分散の信頼区間推定
- 95%信頼区間 = 「母分散が信頼区間に95%の確率で含まれる」


### 使い方
##### データの準備
- `testData.csv`に信頼区間を求めたい標本を`,`で区切りながら貼り付ける  
- 各行の先頭に群の名前を書く
- 複数群のデータを用意しても可
```
GroupA,2,4,3,1,2,3,3,2,3,1
GroupB,3,5,4,2,4,3,5,5,3,2
```

##### 実行
- 95%信頼区間の推定
```
python confidence-interval-estimation-for-the-variance.py
```
- 有意水準を設定したい場合(例:99%信頼区間の推定)
```
python confidence-interval-estimation-for-the-variance.py --confidence 0.99
```

- 別にデータを用意している場合
```
python confidence-interval-estimation-for-the-variance.py --input "csvファイルへのパス"
```

##### 結果
標本の平均(mean), 分散(variance), 標準偏差(SD), 信頼区間(confidence interval)が出力される
```
$ python confidence-interval-estimation-for-the-variance.py

GroupA
mean: 2.4, variance: 0.8400000000000002, SD: 0.9165151389911681
95% confidence interval: (0.39741850818048896, 2.7995961323560885)

GroupB
mean: 3.6, variance: 1.2400000000000002, SD: 1.1135528725660044
95% confidence interval: (0.5866654168378647, 4.132737147763749)
```
