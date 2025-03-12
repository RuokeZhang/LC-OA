nums=[int(x) for x in input().split()]
#[3,2,5,4,1]
#从后往前，找第一个升序的 pair
n=len(nums)
start=-1
for i in range(n-2, -1, -1):
    if nums[i]<nums[i+1]:
        start=i
        break
if start>=0:
    #在 start 的后面，从后往前找第一个比它大的
    newhead=0
    for i in range(n-1, start, -1):
        if nums[i]>nums[start]:
            newhead=i
            break
    print(newhead)
    nums[start], nums[newhead]=nums[newhead], nums[start]
#[3,4,5,2,1]
#start index后面按升序排列
left=start+1
right=n-1
while left<=right:
    nums[left], nums[right]=nums[right], nums[left]
    left+=1
    right-=1
print(nums)