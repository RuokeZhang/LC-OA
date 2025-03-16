'''
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
'''
listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]
skipA = 2
skipB = 3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
def buildList(listA, listB, skipA, skipB):
    m,n=len(listA), len(listB)
    dummyA=ListNode(0)
    dummyB=ListNode(0)
    cur=dummyA
    for i in range(skipA):
        cur.next=ListNode(listA[i])
        cur=cur.next
    curB=dummyB
    for i in range(skipB):
        curB.next=ListNode(listB[i])
        curB=curB.next
    intersect=ListNode(listA[skipA])
    cur.next=intersect
    curB.next=intersect
    cur=intersect
    for i in range(m-skipA-1):
        cur.next=ListNode(listA[i+1+skipA])
        cur=cur.next
    return dummyA.next, dummyB.next

listA, listB=buildList(listA, listB, skipA, skipB)


def getNode(listA, listB):
    curA=listA
    curB=listB
    while curA!=curB:
        curA=curA.next if curA else listB
        curB=curB.next if curB else listA
    return curA

print(getNode(listA, listB).val)

    