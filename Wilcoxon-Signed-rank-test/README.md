# Wilcoxon-Signed-rank-test
ウィルコクソンの符号付き順位検定
- 対応あり二群の有意差検定
- 対立仮説は「2標本の間に差がある」
- 対応ありt検定に対するノンパラメトリック検定


### 使い方
##### データの準備
- `testData.csv`に比較したい標本を`,`で区切りながら貼り付ける  
- 各行の先頭に群の名前を書く
- 群間で対応しているデータが同じ列に並ぶように貼る
- 二群以上のデータを用意しても可(その場合は全ての組み合わせに対して検定を行う)
```
GroupA,1,3,2,4,3,2,1,1,3,2
GroupB,3,5,6,4,2,4,7,6,3,5
GroupC,2,1,1,1,2,3,2,2,2,3
GroupD,3,4,5,2,3,3,5,2,3,5
```

##### 実行
- 有意水準0.05で実行
```
python wilcoxon-signed-rank-test.py
```
- 有意水準を設定したい場合
```
python wilcoxon-signed-rank-test.py --level 0.01
```

- 別にデータを用意している場合
```
python wilcoxon-signed-rank-test.py --input "csvファイルへのパス"
```

##### 結果
p値(p-value)が出力される  
有意差が観測されたペアには`*`がつく
```
$ python wilcoxon-signed-rank-test.py

       GroupA            GroupB             GroupC            GroupD
GroupA      -  *0.0202398344143     0.626999552028     0.06666904726
GroupB      -                 -  *0.00878880387468    0.057831277342
GroupC      -                 -                  -  *0.0129840292564
GroupD      -                 -                  -                 -
```
