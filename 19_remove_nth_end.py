head = [1,2,3,4,5]
k=int(input())

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
def nums2list(nums):
    root=ListNode(nums[0])
    dummy=ListNode(next=root)
    for i in range(1, len(nums)):
        root.next=ListNode(nums[i])
        root=root.next
    return dummy.next

def copy(head):
    cur=nums2list(head)
    slow=cur
    a=cur
    isFirst=False
    for i in range(k+1):
        if not cur:
            isFirst=True
            break
        cur=cur.next
    if isFirst:
        return slow.next
    while cur:
        slow=slow.next
        cur=cur.next
    slow.next=slow.next.next
    return a

res=copy(head)
while res:
    print(res.val)
    res=res.next
