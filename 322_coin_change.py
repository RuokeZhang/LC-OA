'''
输入：coins = [1, 2, 5], amount = 11
输出：3, 可以凑成总金额所需的最少的硬币个数
如果没有任何一种硬币组合能组成总金额，返回 -1 。
'''
import math
coins=[1,2,5]
coins.sort(reverse=True)
amount=11
dp=[math.inf]*(amount+1)
dp[0]=0
for i in range(1, amount+1):
    for c in coins:
        dp[i]=min(dp[i], dp[i-c]+1)
print(dp[amount])