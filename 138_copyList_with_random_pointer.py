'''
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
'''
class Node:
    def __init__(self, x=0, next=None, random=None) -> None:
        self.val=x
        self.next=next
        self.random=next
    
def nums2list(head):
    nodeList=[Node(x[0]) for x in head]
    for i, node in enumerate(nodeList):
        if i<len(nodeList)-1:
            node.next=nodeList[i+1]
        else:
            node.next=None
    for i, node in enumerate(nodeList):
        randomIndex=head[i][1]
        if randomIndex is not None:
            node.random=nodeList[randomIndex]
    return nodeList[0]
        
head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
root=nums2list(head)

# step 1: duplicate
cur=root
while cur:
    nxt=cur.next
    cur.next=Node(cur.val)
    cur=cur.next
    cur.next=nxt
    cur=nxt

# step 2: iterate original node to connect duplicate nodes' random
cur=root
while cur:
    if cur.random:
        cur.next.random=cur.random.next
    cur=cur.next.next
    
# step 3: split it into two list
cur=root
newHead=cur.next
while cur.next.next:
    duCur=cur.next
    cur.next=duCur.next
    duCur.next=duCur.next.next
    cur=cur.next
    

    


