# Confidence-Interval-Estimation-for-the-Mean
t分布を用いた母平均の信頼区間推定
- 95%信頼区間 = 「母平均が信頼区間に95%の確率で含まれる」


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
python confidence-interval-estimation-for-the-mean.py
```
- 有意水準を設定したい場合(例:99%信頼区間の推定)
```
python confidence-interval-estimation-for-the-mean.py --confidence 0.99
```

- 別にデータを用意している場合
```
python confidence-interval-estimation-for-the-mean.py --input "csvファイルへのパス"
```

##### 結果
標本の平均(mean), 標準偏差(SD), 信頼区間(confidence interval)が出力される
```
$ python confidence-interval-estimation-for-the-mean.py

GroupA
mean: 2.4, SD: 0.9165151389911681
95% confidence interval: (1.7088995711901913, 3.0911004288098085)

GroupB
mean: 3.6, SD: 1.1135528725660044
95% confidence interval: (2.7603227977446689, 4.4396772022553312)
```
