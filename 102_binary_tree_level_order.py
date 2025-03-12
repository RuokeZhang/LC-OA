from collections import deque


root = [-10,9,20,None,None,15,7]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=None
        self.right=None
def build_tree(nums, i):
    if i>=len(nums):
        return None
    l=build_tree(nums, 2*i+1)
    r=build_tree(nums, 2*i+2)
    if not nums[i]:
        return None
    root=TreeNode(nums[i])
    root.left=l
    root.right=r
    return root

root=build_tree(root, 0)

def levelOrder(root):
    res=[]
    dq=deque([root])
    while dq:
        length=len(dq)
        level=[]
        for _ in range(length):
            cur=dq.popleft()
            level.append(cur.val)
            if cur.left:
                dq.append(cur.left)
            if cur.right:
                dq.append(cur.right)
        res.append(level)
    return res

levelList=levelOrder(root)
print(levelList)