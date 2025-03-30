'''
输入：head = [4,2,1,3]
输出：[1,2,3,4]
'''
head = [4,2,1,3]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
def buildLinkedList(head):
    dummy=ListNode(0)
    cur=dummy
    for i, x in enumerate(head):
        cur.next=ListNode(x)
        cur=cur.next
    return dummy.next
head=buildLinkedList(head)

def sortList(head):
    fast=slow=head
    fast=fast.head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

    mid=slow.next
    slow.next=None

    l=sortList(head)
    r=sortList(mid)

    lp, rp=l, r

    res=ListNode(0)
    cur=res
    while lp and rp:
        if lp.val<rp.val:
            cur.next=ListNode(lp.val)
            lp=lp.next
        else:
            cur.next=ListNode(rp.val)
            rp=rp.next
        cur=cur.next
    while lp:
        cur.next=ListNode(lp.val)
        lp=lp.next
        cur=cur.next
    while rp:
        cur.next=ListNode(rp.val)
        rp=rp.next
        cur=cur.next
    return res.next












    

