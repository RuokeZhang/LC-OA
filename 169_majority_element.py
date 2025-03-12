'''给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。'''
nums = [2,2,1,1,1,2,2]
count=0
for i, x in enumerate(nums):
    if count==0:
        candidate=x
    if x==candidate:
        count+=1
    else:
        count-=1
print(candidate)