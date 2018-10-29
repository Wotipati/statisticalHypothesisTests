# Unpaired-t-test
対応なしt検定
- 対立仮説は「2標本の間に差がある」
- ウェルチのt検定 (Welch's t test)を実装
  - 必ずしも等分散性を全知にしないt検定
  - `equal_var=False`を`equal_var=True`と書き換えると標準のt検定に


### 使い方
##### データの準備
- `testData.csv`に比較したい標本を`,`で区切りながら貼り付ける  
- 各行の先頭に群の名前を書く
- 二群以上のデータを用意しても可(その場合は全ての組み合わせに対して検定を行う)
```
GroupA,1,1,2,3,1,3,2,4,1,2
GroupB,6,5,1,3,5,1,2,3,4,4
GroupC,2,1,1,1,2,3,2,2,2,3
GroupD,3,4,5,2,3,3,5,2,3,5
```

##### 実行
- 有意水準0.05で実行
```
python unpaired-t-test.py
```
- 有意水準を設定したい場合
```
python unpaired-t-test.py --level 0.01
```

- 別にデータを用意している場合
```
python unpaired-t-test.py --input "csvファイルへのパス"
```

##### 結果
p値(p-value)が出力される  
有意差が観測されたペアには`*`がつく
```
$ python unpaired-t-test.py

       GroupA            GroupB           GroupC             GroupD
GroupA      -  *0.0438205465809     0.80896388793  *0.00776226171432
GroupB      -                 -  *0.0254552725162      0.88100929832
GroupC      -                 -                 -  *0.00239755147089
GroupD      -                 -                 -                  -
```
