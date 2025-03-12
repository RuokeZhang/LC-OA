'''https://www.fastprep.io/problems/amazon-how-many-games-did-the-team-win
Input:  n = 3, firstTeam = [1, 2, 3], secondTeam = [3, 2, 1]
Output: 1 
Explanation:
As shown on the iamge above, group1 wins one match so the answer is 1.
'''
firstTeam = [1, 2, 3]
secondTeam = [3, 2, 1]
n = 3
diff=[firstTeam[i]-secondTeam[i] for i in range(n)]
diff.sort()
print(diff)
#找有多少对i，j，使得 diff[i]+diff[j]>0
[-2,-1,-1,0,1,2,2,3,3]
l,r=0,n-1
res=0
while l<r:
    if diff[l]+diff[r]>0:
        res=(r-l+res)%(10**9+7)
        r-=1
    else:
        l+=1
print(res)

