from collections import deque
from heapq import heappop, heappush


nums=[3,2,3,1,2,4,5,5,6]
k=4
heap=[]
for x in nums:
    if len(heap)==k:
        heappush(heap, x)
        heappop(heap)
    else:
        heappush(heap, x)
print(heap[0])