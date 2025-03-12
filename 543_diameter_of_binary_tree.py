from collections import deque


root = [1,2,3,4,5]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
def buildTree(root, i):
    if i>=len(root):
        return None
    tree=TreeNode(root[i])
    l=buildTree(root, 2*i+1)
    r=buildTree(root, 2*i+2)
    tree.left=l
    tree.right=r
    return tree
root=buildTree(root,  0)
def diameter(root):
    res=0
    def dfs(root):
        nonlocal res
        if not root:
            return -1
        l=dfs(root.left)
        r=dfs(root.right)
        res=max(res, l+2+r)
        return max(l,r)+1
    dfs(root)
    return res

print(diameter(root))

        