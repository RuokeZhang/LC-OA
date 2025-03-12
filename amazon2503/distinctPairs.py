'''
stocksProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3], target = 12
'''
from collections import defaultdict


stocksProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3]
target = 12
stocksProfit.sort()
res=0
memo=defaultdict(int)
for i, x in enumerate(stocksProfit):
    if memo[target-x]>0:
        res+=1
        memo[target-x]-=1
    else:
        memo[x]+=1
print(res)