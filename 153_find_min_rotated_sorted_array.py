'''
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
'''
nums = [2, 1]
n=len(nums)
l,r=0, n-1
while l<r:
    mid=(l+r)//2
    if nums[mid]>nums[n-1]:
        l=mid+1
    else:
        r=mid
print(nums[l])
