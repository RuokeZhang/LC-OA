'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
'''
nums = [1,3,5,6]
target = 5
n=len(nums)
l,r=0, n
while l<r:
    mid=(l+r)//2
    if nums[mid]>target:
        r=mid
    elif nums[mid]==target:
        r=mid
    else:
        l=mid+1
print(l)