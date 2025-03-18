'''
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
'''
from functools import cache


nums = [1,2,3,5]
def equal(nums):
    s=sum(nums)
    if s%2!=0:
        return False
    target=s/2
    n=len(nums)
    #每个数字选或者不选，判断和能否为target
    #dp[i][j]表示遍历到第i个数字，可以获得总和 target
    dp=[[False]*(target+1) for _ in range(n+1)]
    dp[0][0]=True
    for i in range(n):
         for j in range(target+1):
            #不能选
            if nums[i]>target:        
                dp[i+1][j]=dp[i][j]
            #能选
            else:
                dp[i+1][j]=dp[i][j] or dp[i][j-nums[i]]
    return dp[n][target]
            


def equalDfs(nums):
    s=sum(nums)
    if s%2!=0:
        return False
    target=s/2
    n=len(nums)
    @cache
    def dfs(i, target):
            if i<0:
                 if target==0:
                      return True
                 else:
                      return False
            #选
            return dfs(i-1, target-nums[i]) or dfs(i-1, target)
    return dfs(n-1, target)
print(equal(nums))