'''
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。
'''
text1 = "abcde"
text2 = "ace"

m,n=len(text1), len(text2)
#dp[i][j]表示遍历到text1[i-1], text2[j-1]时能获得的最长公共子序列长度
dp=[[0]*(n+1) for _ in range(m+1)]
for i in range(m):
    for j in range(n):
        if text1[i]==text2[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j])
print(dp[m][n])