'''
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
'''
from cmath import inf


grid = [[1,3,1],[1,5,1],[4,2,1]]
m,n=len(grid), len(grid[0])
dp=[[inf]*(n+1) for _ in range(m+1)]
dp[1][0]=0
for i in range(m):
    for j in range(n):
        dp[i+1][j+1]=min(dp[i][j+1], dp[i+1][j])+grid[i][j]
print(dp)