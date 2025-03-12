head = [1,2,3,4]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
def convertToList(nums):
    dummy=ListNode(0)
    cur=dummy
    for x in nums:
        cur.next=ListNode(x)
        cur=cur.next
    return dummy.next

root=convertToList(head)
def swap(root):
    dummy=ListNode(next=root)
    pre=dummy
    p1=dummy.next
    p2=p1.next
    while p1 and p2:
        nxt=p2.next
        p2.next=p1
        p1.next=nxt
        pre.next=p2
        pre=p1
        p1=nxt
        if p1:
            p2=p1.next
    
    return dummy.next

res=swap(root)
while res:
    print(res.val)
    res=res.next

