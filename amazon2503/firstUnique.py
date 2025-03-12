s = "statistics"
from collections import Counter
def sol(s):
    cnt=Counter()
    for x in s:
        cnt[x]+=1
    for i,x in enumerate(s):
        if cnt[x]==1:
            return i+1
    return -1
print(sol(s))



