'''
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''
digits = "23"
def generate(digits):
    n=len(digits)
    res=[]
    path=['']*n
    dic=["1", "2", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def dfs(i):
        if i==n:
            res.append("".join(path))
            return
        digit=int(digits[i])
        for c in dic[digit]:
            path[i]=c
            dfs(i+1)
    dfs(0)
    return res
print(generate(digits))

