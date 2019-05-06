import scipy.stats as stats
oddsratio, pvalue = stats.fisher_exact([[15, 1], [96, 91]])
print(pvalue)
print("*******")
print(oddsratio)
