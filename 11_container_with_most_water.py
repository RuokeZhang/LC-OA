nums=[1,8,6,2,5,4,8,3,7]
n=len(nums)
l, r=0, n-1
res=0
while l<r:
    res=max(res, (r-l)*min(nums[r], nums[l]))
    if nums[l]<nums[r]:
        l+=1
    else:
        r-=1
print(res)
