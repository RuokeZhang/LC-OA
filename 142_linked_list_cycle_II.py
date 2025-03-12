'''
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
'''
head = [3,2,0,-4]
pos = 1
class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
def constructList(head, pos):
    dummy=Node(0)
    cur=dummy
    cycleNode=Node()
    for i, x in enumerate(head):
        if i==pos:
            cycleNode=Node(val=x)
            cur.next=cycleNode
        else:
            cur.next=Node(val=x)
        cur=cur.next

    cur.next=cycleNode
    return dummy.next

head=constructList(head,  pos)

def detectCycle(head):
    fast=head
    slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:
            break
    if not fast or not fast.next:
        return None
    fast=head
    while fast!=slow:
        fast=fast.next
        slow=slow.next
    return slow
print(detectCycle(head).val)