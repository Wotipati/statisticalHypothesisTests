# Kruskal-Wallis-test
クラスカル・ウォリス検定
- 対応なし多群(3群以上)の検定
- 対立仮説は「少なくとも１つの水準の母集団平均が他の水準の平均とは異なる」
- 一元配置分散分析(One-way ANOVA)に対するノンパラメトリックの代替方法

### 使い方
##### データの準備
- `testData.csv`に比較したい標本を`,`で区切りながら貼り付ける  
- 各行の先頭に群の名前を書く
- 必ず3群以上必要

```
GroupA,2,4,3,1,2,3,3,2,3,1
GroupB,3,5,4,2,4,3,5,5,3,2
GroupC,2,1,1,1,2,3,2,2,2,3
```

##### 実行
- 有意水準0.05で実行
```
python kruskal-wallis-test.py
```
- 有意水準を設定したい場合
```
python kruskal-wallis-test.py --level 0.01
```

- 別にデータを用意している場合
```
python kruskal-wallis-test.py --input "csvファイルへのパス"
```

##### 結果
p値(p-value)が出力される  
有意差が観測された場合は`*`がつく
```
$ python kruskal-wallis-test.py

p-value = 0.00107257796923*
```
