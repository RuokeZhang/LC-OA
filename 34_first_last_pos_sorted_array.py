nums = [5,7,7,8,8,10]
target = 8

def lower_bound(nums, target):
    n=len(nums)
    r=n
    l=0
    while l<r:
        mid=(l+r)//2
        if nums[mid]>target:
            r=mid
        elif nums[mid]==target:
            r=mid
        elif nums[mid]<target:
            l=mid+1
    return l

def searchRange(nums, target):
    left=lower_bound(nums, target)
    if left==len(nums) or nums[left]!=target:
        return [-1, -1]
    right=lower_bound(nums, target+1)-1
    return [left, right]

print(searchRange(nums, target))