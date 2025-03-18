'''
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
'''
from math import inf


word1 = "horse"
word2 = "ros"
m,n=len(word1),len(word2)
dp=[[inf]*(n+1) for _ in range(m+1)]

dp[0]=[j for j in range(n+1)]

for i in range(m):
    dp[i+1][0]=i+1
    for j in range(n):
        if word1[i]==word2[j]:
            dp[i+1][j+1]=dp[i][j]
        else:
            dp[i+1][j+1]=min(dp[i][j+1], dp[i+1][j],dp[i][j])+1
print(dp[m][n])