'''
https://www.fastprep.io/problems/1.amazon-get-number-redundancy-free
'''
from collections import Counter


userPassword = "abcabcbb"
n=len(userPassword)
memo={}
i=0
res=0
while i<n:
    x=userPassword[i]
    if x in memo:
        lastIndex=memo[x]
        print(lastIndex)
        res+=1
        
    memo[x]=i
print(res+1)

