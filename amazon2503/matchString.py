'''Input:  text = ["hackerrank", "hackerrnak"], pat = ["hac*rank", "hac*rank"]'''
text = ["hackerrank", "hackerrnak"]
pat = ["hac*rank", "hac*rank"]
n=len(text)
res=[]
for i in range(n):
    index=pat[i].index('*')
    prefix=pat[i][:index]
    suffix=pat[i][index+1:]

    if prefix==text[i][:index] and suffix==text[i][-(len(pat[i])-index-1):]:
        res.append("YES")
    else:
        res.append("NO")
print(res)
