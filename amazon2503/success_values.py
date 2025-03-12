'''
https://www.fastprep.io/problems/get-success-value
Input:  num_viewers = [2, 5, 6, 3, 5], queries = [2, 3, 5]
Output: [11, 16, 21] 
'''
from itertools import accumulate


num_viewers = [2, 5, 6, 3, 5]
queries = [2, 3, 5]
num_viewers.sort(reverse=True)
s=list(accumulate(num_viewers, initial=0))
res=[]
for i,q in enumerate(queries):
    res.append(s[q])
print(res)