'''
输入：head = [1,2,3,4,5,6,7], k = 3
输出：
'''
head = [1,2,3,4,5,6,7]
k=3
class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
def buildList(head):
    dummy=Node(0)
    cur=dummy
    for x in head:
        cur.next=Node(x)
        cur=cur.next
    return dummy.next

myList=buildList(head)

def reverseK(myList, k):
    cur=myList
    cnt=0
    while cur:
        cnt+=1
        cur=cur.next
    dummy=Node(next=myList)
    pre=None
    p0=dummy
    cur=myList
    while cnt>=k:
        for _ in range(k):
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        newP0=p0.next
        p0.next.next=cur
        p0.next=pre
        p0=newP0
        pre=newP0
        cnt-=k

    return dummy.next
res=reverseK(myList, k)
cur=res
while cur:
    print(cur.val)
    cur=cur.next

