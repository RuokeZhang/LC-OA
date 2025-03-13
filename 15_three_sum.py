'''
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
'''
nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
n=len(nums)
res=[]
nums.sort()
print(nums)
for k in range(n-1, 1, -1):
    i,j=0,k-1
    if n-1>k>1 and nums[k]==nums[k+1]:
        continue
    while i<j:
        if nums[i]+nums[j]>-nums[k]:
            j-=1
        elif nums[i]+nums[j]==-nums[k]:
            res.append([nums[i], nums[j], nums[k]])
            i+=1
            j-=1
            while i<k and nums[i]==nums[i-1]:
                i+=1
            while j>i and nums[j]==nums[j+1]:
                j-=1
        else:
            i+=1
print(res)
