from collections import Counter
from heapq import heappop, heappush


nums = [1,1,1,1,2,2,3]
k=2

# 1 2 4 
def sol(nums,k):
    cnt=Counter(nums)
    heap=[]
    for key, val in cnt.items():
        if len(heap)==k:
            heappush(heap, (val,key))
            heappop(heap)
        else:
            heappush(heap, (val,key))
    return [x[1] for x in heap]

print(sol(nums,k))