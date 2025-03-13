
nums=[int(x) for x in input().split()] #[3,4,-1,1]
n=len(nums)

def firstMissingPositive(nums) -> int:
    for i, x in enumerate(nums):
        while 1<=nums[i]<=n and nums[nums[i]-1] !=nums[i]:
            nums[nums[i]-1], nums[i]=nums[i], nums[nums[i]-1]

    for i in range(n):
        if nums[i]!=i+1:
            return i+1
    return n+1        

    
print(firstMissingPositive(nums))