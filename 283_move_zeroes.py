'''
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
l=0
nums = [int(x) for x in input().split()]
for i, x in enumerate(nums):
    if x!=0:
        nums[i], nums[l]=nums[l], nums[i]
        l+=1
print(nums)