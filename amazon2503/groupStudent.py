levels=[1,3,4,4,5,7]
# (1 3) (4 4) (7), ans=3
# 1 2 3 3 4 5
# 1 4 5 9 13
# 1 k k+1 k+2 ... 2k
maxSpread=1
res=0
levels.sort()
start=levels[0]
n=len(levels)
for i in range(1, n):
    if levels[i]<=start+maxSpread:
        continue
    res+=1
    start=levels[i]
print(res+1)

