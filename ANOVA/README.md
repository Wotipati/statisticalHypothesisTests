# ANOVA
分散分析(<u>An</u>alysis <u>o</u>f <u>va</u>riance, ANOVA)用スクリプト
- スクリプトはscipyに実装されている[一元配置分散分析 (One-way ANOVA)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/ANOVA/One-way-Anova)のみ
- ANOVAについての詳細な説明は[分散分析(ANOVA)について](https://github.com/Wotipati/statisticalHypothesisTests/blob/master/Notes/What_is_ANOVA%3F.md)を参照


## One-way-ANOVA
- 対応なし一元配置分散分析  

### 使い方
##### データの準備
- `testData.csv`に比較したい標本を`,`で区切りながら貼り付ける  
- 各行の先頭に群の名前を書く
- 必ず3群以上必要
- 今回は[分散分析(ANOVA)について](https://github.com/Wotipati/statisticalHypothesisTests/blob/master/Notes/What_is_ANOVA%3F.md)の説明で使用したデータを用意
```
GroupA(0kg),9,11,10
GroupB(10kg),13,12,14
GroupC(20kg),17,16,15
GroupD(30kg),16,17,18
```

##### 実行
- 有意水準0.05で実行
```
python python one-way-ANOVA.py
```
- 有意水準を設定したい場合
```
python python one-way-ANOVA.py --level 0.01
```

- 別にデータを用意している場合
```
python python one-way-ANOVA.py --input "csvファイルへのパス"
```

##### 結果
p値(p-value)が出力される  
有意差が観測された場合は`*`がつく
```
$ python python one-way-ANOVA.py

p-value = 0.000105652545787*
```
