'''
输入：s = "3[a]2[bc]"
输出："aaabcbc"
'''
s = "3[a]2[bc]"
stack=[]
res=""
multi=0
for i, x in enumerate(s):
    if x=='[':
        stack.append([multi, res])
        multi=0
        res=""
    elif x==']':
        m, r=stack.pop()
        res=r+m*res
    elif '0'<=x<='9':
        multi=int(x)+multi*10
    else:
        res+=x
print(res)
