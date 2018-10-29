# Mann-Whitney-U-test
マン・ホイットニーのU検定
- 対応なし二群の有意差検定
- 対立仮説は「2標本の間に差がある」
- 対応なしt検定に対するノンパラメトリック検定
- ウィルコクソンの順位和検定(Wilcoxon rank-sum test)とも呼ばれる


### 使い方
##### データの準備
- `testData.csv`に比較したい標本を`,`で区切りながら貼り付ける  
- 各行の先頭に群の名前を書く
- 二群以上のデータを用意しても可(その場合は全ての組み合わせに対して検定を行う)
```
GroupA,2,4,3,1,2,3,3,2,3,1
GroupB,3,5,4,2,4,3,5,5,3,2
GroupC,2,1,1,1,2,3,2,2,2,3
GroupD,3,4,5,2,3,3,5,2,3,5
```

##### 実行
- 有意水準0.05で実行
```
python mann-whitney-u-test.py
```
- 有意水準を設定したい場合
```
python mann-whitney-u-test.py --level 0.01
```

- 別にデータを用意している場合
```
python mann-whitney-u-test.py --input "csvファイルへのパス"
```

##### 結果
p値(p-value)が出力される  
有意差が観測されたペアには`*`がつく
```
$ python mann-whitney-u-test.py

       GroupA            GroupB           GroupC             GroupD
GroupA      -  *0.0192043876643    0.11541267853   *0.0290956779717
GroupB      -                 -  *0.001695333779     0.437412800807
GroupC      -                 -                -  *0.00206574468142
GroupD      -                 -                -                  -
```
