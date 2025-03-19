'''
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
右括号个数为i-l
'''
def generate(n):
    res=[]
    def dfs(i, path, l):
        if i==2*n:
            res.append(path)
            return 
        if i-l>l:
            return
        if l<n:
            dfs(i+1, path+'(', l+1)
        dfs(i+1, path+')', l)
    dfs(0, "", 0)
    return res
    
print(generate(3))

