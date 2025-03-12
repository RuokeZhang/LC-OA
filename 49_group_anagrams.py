'''
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sDict={}
for s in strs:
    s1="".join(sorted(s))
    if s1 not in sDict:
        sDict[s1]=[]
    sDict[s1].append(s)
print(list(sDict.values()))