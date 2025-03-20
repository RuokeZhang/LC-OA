'''
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
'''
candidates = [2,3,6,7]
target = 7

def sol(candidates, target):
    n=len(candidates)
    res=[]
    path=[]
    def dfs(i, target):
        if target==0:
            res.append(path.copy())
        if target<0:
            return
        for j in range(i, n):
            path.append(candidates[j])
            dfs(j, target-candidates[j])
            path.pop()
    dfs(0, target)
    return res
#print(sol(candidates, target))

def sol2(candidates, target):
    res=[]
    path=[]
    n=len(candidates)
    def dfs(i, target):
        if i==n:
            if target==0:
                res.append(path.copy())
            return
        if target<0:
            return
        path.append(candidates[i])
        dfs(i, target-candidates[i])
        path.pop()
        dfs(i+1, target)
    dfs(0, target)
    return res
print(sol(candidates, target))
            
