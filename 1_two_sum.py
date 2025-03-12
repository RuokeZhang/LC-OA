'''
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
'''
myMap={}
nums = [2,7,11,15]
target = 9
def sol(nums, target):
    for i, x in enumerate(nums):
        if target-x in myMap:
            return [myMap[target-x], i]
        myMap[x]=i
print(sol(nums, target))
