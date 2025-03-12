'''
Input:  x = "AERB", y = "ATRC", z = "AGCB"
Output: "[ABCDEFGHJKLMNOPQRSTUVWXYZ][ABCDEFGHJKLMNOPQRSTUVWXYZ][ABDEFGHJKLMNOPQRSTUVWXYZ][ABCDEFGHJKLMNOPQRSTUVWXYZ]
'''
x = "A"
y = "C"
z = "D"
def sol(x,y,z):
    res=""
    baseRegex = "[ABCDEFGHIJKLMNOPQRSTUVWXYZ]"
    n=len(x)
    for j in range(n-1, -2, -1):
        if x[j]!=z[j] and y[j]!=z[j]:
            break
    if j==-1:
        return "-1"
    for _ in range(j):
        res+=baseRegex
    miss=z[j]
    missIndex=ord(z[j])-ord('A')+1
    res+=baseRegex[:missIndex]+baseRegex[missIndex+1:]
    for _ in range(n-1-j):
        res+=baseRegex
    return res
print(sol(x, y, z))


    


