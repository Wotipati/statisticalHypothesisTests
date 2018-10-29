# statisticalHypothesisTests
統計的仮説検定用スクリプト(Python)  


|            | パラメトリック検定 | ノンパラメトリック検定 |
|:-----------|:------------|:------------|
|対応なし2群| Unpaired t test| [Mann-Whitney U test](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Mann-Whitney-U-test)|
|対応あり2群| Paired t test | Wilcoxon test|
|対応なし他群| ANOVA | Kruskal-Wallis test |
|対応あり他群| Repeated-measures ANOVA | [Friedman test](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Friedman-test) |


### Requirement
- python3
- scipy 0.19.1
- pandas 0.20.3

#### References
- [Statistical Methods for HCI Research by Koji Yatani](http://yatani.jp/teaching/doku.php?id=hcistats:start)
