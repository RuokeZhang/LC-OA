'''
示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
'''
from math import inf


nums1 = []
nums2 = [2, 3]

def search(nums1, nums2):
    if len(nums1)>len(nums2):
        nums1,nums2=nums2,nums1

    m,n=len(nums1), len(nums2)

    l, r=0, m+1
    leftTotal=(m+n+1)//2
    targetI=0
    #左闭右开
    while l<r:
        i=(l+r)//2
        j=leftTotal-i
        if i>0 and j<n and nums1[i-1]>nums2[j]:
            r=i #下一轮搜索[l,i)
        elif j>0 and i<m and nums1[i]<nums2[j-1]:
            l=i+1
        else:
            targetI=i
            break
    print(targetI, leftTotal-targetI)
    nums1LeftMax=nums1[targetI-1] if targetI>0 else -inf
    nums1RightMin=nums1[targetI] if targetI<m else inf
    nums2LeftMax=nums2[leftTotal-targetI-1] if leftTotal-targetI>0 else -inf
    nums2RightMin=nums2[leftTotal-targetI] if leftTotal-targetI<n else inf
    if (m+n)%2==0:
        return (max(nums1LeftMax, nums2LeftMax)+min(nums1RightMin, nums2RightMin))/2
    return max(nums1LeftMax, nums2LeftMax)
print(search(nums1, nums2))



        