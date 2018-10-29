# statisticalHypothesisTests
統計的仮説検定用スクリプト(Python)  


|            | パラメトリック検定 | ノンパラメトリック検定 |
|:-----------|:------------|:------------|
|対応なし2群| 対応なしt検定(Unpaired t test) | [マン・ホイットニーのU検定(Mann-Whitney U test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Mann-Whitney-U-test)|
|対応あり2群| 対応ありt検定(Paired t test) | [ウィルコクソンの符号付き順位検定(Wilcoxon Signed-rank test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Wilcoxon-Signed-rank-test)|
|対応なし他群| 分散分析(ANOVA) | [クラスカル・ウォリス検定(Kruskal-Wallis test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Kruskal-Wallis-test) |
|対応あり他群| 反復測定分散分析(Repeated-measures ANOVA) | [フリードマン検定(Friedman test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Friedman-test) |


### Requirement
- python3
- scipy 0.19.1
- pandas 0.20.3

#### References
- [Statistical Methods for HCI Research by Koji Yatani](http://yatani.jp/teaching/doku.php?id=hcistats:start)
- [入門 統計学 −検定から多変量解析・実験計画法まで−](http://shop.ohmsha.co.jp/shopdetail/000000001900/)
