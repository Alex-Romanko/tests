import scipy.stats as stats
oddsratio, pvalue = stats.fisher_exact([[7, 0], [96, 91]])
print(pvalue, oddsratio)
