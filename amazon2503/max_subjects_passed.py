answered = [2,4]
needed = [4,5]
q = 1
n=len(needed)
gap=[max(0, needed[i]-answered[i]) for i in range(n)]
gap.sort()
res=0
i=0
for x in gap:
    if q>=x:
        res+=1
        q-=x
    else:
        break
print(res)