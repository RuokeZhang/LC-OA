from math import inf


#root = [2,-1]
root = [3]
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

def max_pathSum(root):
    res=-inf
    def dfs(root):
        nonlocal res
        if not root:
            return 0
        l=dfs(root.left)
        r=dfs(root.right)
        res=max(res, root.val+max(l, 0)+max(r, 0))
        return max(l, r, 0)+root.val
    dfs(root)
    return res

print(max_pathSum(root))


