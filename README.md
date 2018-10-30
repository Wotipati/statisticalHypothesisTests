# statisticalHypothesisTests
統計的仮説検定&信頼区間推定用スクリプト(Python)  

### 統計的仮説検定 (Statistical Hypothesis Tests)
|            | パラメトリック検定<br>(Parametric test) | ノンパラメトリック検定<br>(Non-parametric test) |
|:-----------|:------------|:------------|
|対応なし2群<br>(Compare two unpaired groups)| [対応なしt検定<br>(Unpaired t test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Unpaired-t-test) | [マン・ホイットニーのU検定<br>(Mann-Whitney U test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Mann-Whitney-U-test)|
|対応あり2群<br>(Compare two paired groups)| [対応ありt検定<br>(Paired t test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Paired-t-test) | [ウィルコクソンの符号付き順位検定<br>(Wilcoxon Signed-rank test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Wilcoxon-Signed-rank-test)|
|対応なし他群<br>(Compare more than two unpaired groups)| 分散分析<br>(ANOVA) | [クラスカル・ウォリス検定<br>(Kruskal-Wallis test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Kruskal-Wallis-test) |
|対応あり他群<br>(Compare more than two paired groups)| 反復測定分散分析<br>(Repeated-measures ANOVA) | [フリードマン検定<br>(Friedman test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Friedman-test) |


### 信頼区間の推定 (Confidence Interval Estimation)
- [母平均の信頼区間推定](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/t-Stats-Confidence-Interval)
- 母分散の信頼区間推定(予定)


### Notes
- 仮説検定の基本的な流れ(予定)
- "対応あり"と"対応なし"(予定)
- 分散分析(ANOVA)について(予定)
- "パラメトリック検定"と"ノンパラメトリック検定"(予定)


### Requirement
- python3
- scipy 0.19.1
- pandas 0.20.3


#### References
- [Statistical Methods for HCI Research by Koji Yatani](http://yatani.jp/teaching/doku.php?id=hcistats:start)
- [入門 統計学 −検定から多変量解析・実験計画法まで−](http://shop.ohmsha.co.jp/shopdetail/000000001900/)
