'''
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''
nums = [100,4,200,1,3,2]
res=0
numSet=set(nums)
length=0
for i, x in enumerate(nums):
    if x-1 in numSet:
        continue
    length=0
    while x in numSet:
        length+=1
        x+=1
    res=max(length, res)
print(res)