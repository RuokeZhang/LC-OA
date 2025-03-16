'''
示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
'''
s = "aab"
def partition(s):
    n=len(s)
    res=[]
    path=[]
    def valid(i, j):
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    def dfs(i):
        if i==n:
            res.append(path.copy())
            return
        for j in range(i+1, n+1):
            if valid(i, j-1):
                
                path.append(s[i:j])

                dfs(j)
                path.pop()
    dfs(0)
    return res
print(partition(s))


        
        
