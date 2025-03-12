
nums=[int(x) for x in input().split()] #[3,4,-1,1]
n=len(nums)

def firstMissingPositive(nums) -> int:
    def swap(i, j):
        nums[i], nums[j]=nums[j], nums[i]
    for i, x in enumerate(nums):
        while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
            swap(i, nums[i]-1)
    
    for i, x in enumerate(nums):
        if x!=i+1:
            return i+1
    
    return n+1
    
print(firstMissingPositive(nums))