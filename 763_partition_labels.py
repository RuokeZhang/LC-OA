s = "ababcbacadefegdehijhklij"
res=[]
#每个字母最多出现在一个片段中,划分成尽可能多的片段
lastApp={x:i for i, x in enumerate(s)}
#babadsk
#s=abc

reach=lastApp[s[0]] #7
i=1
res=[]
start=0
for i in range(len(s)):
    if lastApp[s[i]]>reach:
        reach=lastApp[s[i]]
    if i==reach:
        res.append(i-start+1)
        start=i+1

print(res)