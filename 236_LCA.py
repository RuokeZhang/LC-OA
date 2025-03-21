'''
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
'''
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
root = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1
def lca(root, p, q):
    