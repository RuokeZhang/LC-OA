'''
In a restaurant, there are n customers waiting in line, and each customer requires a certain amount of service time. 
The service time required for the i-th customer is given as t[i]. The restaurant has k waiters available, and each waiter must serve a contiguous block of customers (i.e., a waiter cannot serve non-consecutive customers). 
Your task is to assign customers to the waiters such that the workload is balanced. 
Specifically, you want to minimize the maximum total service time among all waiters. In other words, if the assignment divides the queue into k consecutive segments, with the i-th segment having a total service time Sᵢ, your goal is to minimize max(S₁, S₂, …, Sₖ).
Input:
An integer array t, where t[i] represents the dining time of the i-th customer.
An integer k, representing the number of waiters.
Output:
An integer representing the minimized max(S₁, S₂, …, Sₖ).
'''
#如何划分，使得每个waiter的工作量最小
from functools import cache, lru_cache

def dpSol(t,k):
    #一比一翻译回溯为动态规划
    n=len(t)
    if n<=k:
        return max(t)
    dp=[[float('inf')]*(k+1) for _ in range(n+1)]
    dp[0][0]=0
    prefix_sum=[0]*(n+1)
    for i in range(1, n+1):
        prefix_sum[i]=prefix_sum[i-1]+t[i-1]
    for i in range(1, n+1):
        for j in range(1, k+1):
            for p in range(i):
                dp[i][j]=min(dp[i][j], max(dp[p][j-1], prefix_sum[i]-prefix_sum[p]))
    return dp[n][k]


def minMaxServiceTime(t, k: int) -> int:

    n=len(t)
    if n<=k:
        return max(t)
    res=float('inf')
    #对于每两个顾客中的分界线，选或者不选，回溯
    def dfs(i, k,path):
        nonlocal res
        print(i, k, path)
        if i==n and sum(path)==sum(t):
            
            res=min(res, max(path))
            return

        #选

        path[-1]+=t[i]

        dfs(i+1, k, path)
        path[-1]-=t[i]
        #不选
        if k>0:

            path.append(t[i])
            
            dfs(i+1, k-1, path)
            path.pop()

    path=[]
    path.append(t[0])
    dfs(1, k-1, path)
    return res

        
        
t=[7, 2, 5, 10, 8]
k=2




    


print(dpSol(t,k))
