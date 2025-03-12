'''
boxes = [5, 5, 8, 7]
[5,6,7,7]
[6,6,6,7]
'''
boxes = [3,3,7]
# 小于ave的。每个都加上！
s=sum(boxes)

n=len(boxes)
ave=s//n
boxes.sort()
res=0
for x in boxes:
    if x<ave:
        res+=ave-x
print(res)
