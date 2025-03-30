'''
输入：nums = [1,1,1], k = 2
输出：2
'''
from collections import Counter
from itertools import accumulate


nums = [1,1,1]
k = 2
def sol(nums, k):
    cnt=Counter()
    res=0
    s=accumulate(nums, initial=0)
    for i, x in enumerate(s):
        res+=cnt[x-k]
        cnt[x]+=1
    return res
print(sol(nums, k))
        
        