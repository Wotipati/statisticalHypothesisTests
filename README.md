# statisticalHypothesisTests
統計的仮説検定&信頼区間推定用スクリプト(Python)  

### 統計的仮説検定 (Statistical Hypothesis Tests)
|            | パラメトリック検定<br>(Parametric test) | ノンパラメトリック検定<br>(Non-parametric test) |
|:-----------|:------------|:------------|
|**対応なし2群<br>(Compare two unpaired groups)**| [対応なしt検定<br>(Unpaired t test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Unpaired-t-test) | [マン・ホイットニーのU検定<br>(Mann-Whitney U test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Mann-Whitney-U-test)|
|**対応あり2群<br>(Compare two paired groups)**| [対応ありt検定<br>(Paired t test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Paired-t-test) | [ウィルコクソンの符号付き順位検定<br>(Wilcoxon Signed-rank test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Wilcoxon-Signed-rank-test)|
|**対応なし他群<br>(Compare more than two unpaired groups)**| [分散分析<br>(ANOVA)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/ANOVA#one-way-anova) | [クラスカル・ウォリス検定<br>(Kruskal-Wallis test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Kruskal-Wallis-test) |
|**対応あり他群<br>(Compare more than two paired groups)**| [反復測定分散分析<br>(Repeated-measures ANOVA)](https://github.com/Wotipati/statisticalHypothesisTests/blob/master/Notes/What_is_ANOVA%3F.md#%E5%AF%BE%E5%BF%9C%E3%81%82%E3%82%8A%E4%B8%80%E5%85%83%E9%85%8D%E7%BD%AE%E5%88%86%E6%95%A3%E5%88%86%E6%9E%90) | [フリードマン検定<br>(Friedman test)](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Friedman-test) |


### 信頼区間の推定 (Confidence Interval Estimation)
- [母平均の信頼区間推定](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Confidence-Interval-Estimation-for-the-Mean)
- [母分散の信頼区間推定](https://github.com/Wotipati/statisticalHypothesisTests/tree/master/Confidence-Interval-Estimation-for-the-Varians)


### その他(Notes)
- [仮説検定の基本的な流れについて](https://github.com/Wotipati/statisticalHypothesisTests/blob/master/Notes/What_is_Statistical_Hypothesis_Test%3F.md)
- ["対応あり"と"対応なし"について](https://github.com/Wotipati/statisticalHypothesisTests/blob/master/Notes/paired_and_unpaired.md)
- [分散分析(ANOVA)について](https://github.com/Wotipati/statisticalHypothesisTests/blob/master/Notes/What_is_ANOVA%3F.md)
- [パラメトリック検定"と"ノンパラメトリック検定](https://github.com/Wotipati/statisticalHypothesisTests/blob/master/Notes/parametric_and_nonparametric.md)
- 等分散の検定(Levene's test)


### Requirement
- python3
- scipy 0.19.1
- pandas 0.20.3


#### References
- [Statistical Methods for HCI Research by Koji Yatani](http://yatani.jp/teaching/doku.php?id=hcistats:start)
- [入門 統計学 −検定から多変量解析・実験計画法まで−](http://shop.ohmsha.co.jp/shopdetail/000000001900/)
