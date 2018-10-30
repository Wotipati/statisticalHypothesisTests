# Parametric and Non-Parametric
パラメトリック検定とノンパラメトリック検定

## パラメトリック検定
- 正規分布など特定の分布を仮定できるデータに対して検定を行う手法
- (分布が仮定するために)データは比率尺度や間隔尺度である必要がある（順序尺度や名義尺度は不可能）
- t検定, F検定などは正規分布に従うこと(正規性)を前提としている
- 特にt検定では比較する群の分散が等しいこと(等分散性)を前提としている
- たとえ元データが正規分布にしたがっていない場合も、等分散性が満たしている場合は中心極限定理により、標本平均の差は近似的に正規分布するため、検定自体に大きな影響は与えない
- 等分散性はF検定や[ルビーン検定(Levene's-test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Levene's-test)を利用して検証することが可能

例)
- t検定([対応あり](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Paired-t-test)/[対応なし](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Unpaired-t-test))
- [分散分析](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/ANOVA)
- F検定
- [ルビーン検定(Levene's-test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Levene's-test)



## ノンパラメトリック検定
- 特定の分布を仮定できないデータに対しても検定できるように開発されたもの
- 標本サイズが小さい場合や外れ値がある場合に対しても比較的検定しやすい

例)
- [マン・ホイットニーのU検定(Mann-Whitney U test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Mann-Whitney-U-test)
- [ウィルコクソンの符号付き順位検定(Wilcoxon Signed-rank test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Wilcoxon-Signed-rank-test)
- [クラスカル・ウォリス検定(Kruskal-Wallis test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Kruskal-Wallis-test)
- [フリードマン検定(Friedman test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Friedman-test)
