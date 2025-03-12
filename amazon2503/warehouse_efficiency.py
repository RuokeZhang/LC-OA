'''
https://www.fastprep.io/problems/amazon-calculate-warehouse-efficiency
The supply chain manager at one of Amazon's warehouses wants to measure the efficiency of the way parcels are shipped. The volume of each parcel is represented in the array parcelWeights. Each day, the first and last parcels in the array parcelWeights are shipped until all of them are dispatched.

The manager comes up with metrics to calculate warehouse efficiency. Each day before shipping, any parcel in the warehouse is chosen and its volume is added to the sum of total efficiency. A parcel can only be chosen once.

Given the array parcelWeights, find the maximum possible efficiency of the warehouse.

Example 1:

Input:  parcelWeights = [4, 4, 8, 5, 3, 2]
Output: 17 
'''
import heapq

class Solution:
    def calculateWarehouseEfficiency(self, parcelWeights):
        N = len(parcelWeights)
        left = 0
        right = N - 1
        # Python 中的 heapq 默认是小顶堆
        pq = []
        day = 1
        while left <= right:
            if left == right:
                heapq.heappush(pq, parcelWeights[left])
            else:
                heapq.heappush(pq, parcelWeights[left])
                heapq.heappush(pq, parcelWeights[right])
            while len(pq) > day:
                heapq.heappop(pq)
            left += 1
            right -= 1
            day += 1

        res = 0
        while pq:
            res += heapq.heappop(pq)
        return res
solution = Solution()
parcelWeights = [2,1,8,5,6,2,4]
print(solution.calculateWarehouseEfficiency(parcelWeights))