n = 5
'''
The data of the n = 13th day is dependent on [0, 1, 2, 3, 4, 6, 13] 
obtained for k = [14, 13, 6, 4, 3, 2, 1].
'''
s=0
k=1
while True:
    x=n//k
    s+=x
    print(x)
    if x==0:
        break
    upper=n//x
    k=upper+1
print(s)