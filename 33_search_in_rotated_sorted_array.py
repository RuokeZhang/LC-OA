'''
示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
'''
nums = [4,5,6,7,0,1,2]
target = 0
def search(nums, target):
    n=len(nums)
    l,r=0,n
    while l<r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        if nums[mid]>nums[l]:
            if nums[l]<=target<nums[mid]:
                r=mid
            else:
                l=mid+1
        else:
            if nums[mid]<target<=nums[r-1]:
                l=mid+1
            else:
                r=mid
    if l==r:
        return -1
    return l if nums[l]==target else  -1
print(search(nums, target))
