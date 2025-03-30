'''In the magical Kingdom of Numbers, every citizen is represented by a unique natural number, and they are arranged in a strict order. 
One day, the wise king decides to hold a grand celebration. 
However, before the festivities can begin, all the citizens must be divided into several squads. 
Each squad must consist of consecutive numbers and have at least 3 members. 
Only when all citizens are successfully grouped into these qualifying squads can the celebration proceed. 
As the kingdom's renowned strategist, your task is to determine whether a given sorted array of natural numbers can be split into such consecutive subsequences. 
Return true if the array can be split successfully, and false otherwise. Input:
A sorted array of natural numbers.
Output:
true or false
[1, 2, 3, 3, 4, 4, 5, 6] => true

'''

#LC 659 贪心+哈希表

from collections import Counter


nums=[1, 2, 3, 3, 4, 4, 5, 6]
# 3,4是重复出现的元素。需要从这里拆分，得到[1,2,3,4]和[3,4,5,6]两个子数组


    
        
def isPossible(self, nums: List[int]) -> bool:
    n=len(nums)
    cnt=Counter(nums)
    last=defaultdict(int)
    #last[i]表示以i结尾的序列个数，此时如果遍历到i+1,则可把新数放在序列后面
    #尽可能多地划分
    for c in nums:
        if cnt[c]==0:
            continue
        cnt[c]-=1
        if last[c-1]>0:
            last[c-1]-=1
            last[c]+=1
        else:
            if cnt[c+1]>0 and cnt[c+2]>0:
                cnt[c+1]-=1
                cnt[c+2]-=1
                last[c+2]+=1
            else:
                return False
    return True
