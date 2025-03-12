from collections import deque
nums = [1,2,2,3,4,4,3]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    # 创建根节点
    root = TreeNode(arr[0])
    q = deque([root])  # 使用队列存储待处理的节点
    idx = 1  # 数组索引，从第二个元素开始
    
    while q and idx < len(arr):
        node = q.popleft()  # 取出当前节点
        
        # 处理左子节点
        if idx < len(arr) and arr[idx] is not None:
            node.left = TreeNode(arr[idx])
            q.append(node.left)
        idx += 1
        
        # 处理右子节点
        if idx < len(arr) and arr[idx] is not None:
            node.right = TreeNode(arr[idx])
            q.append(node.right)
        idx += 1
    
    return root
tree=build_tree(nums)

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    q = deque([root])
    
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    
    return result
#print(level_order_traversal(tree))  # 输出: [1, 2, 3, 4, 5, None, 7]
def isSymmetric(root):
    return areSym(root.left, root.right)

def areSym(l, r):
    if not l or not r:
        return l==r
    return l.val==r.val and areSym(l.left, r.right) and areSym(l.right, r.left)

print(isSymmetric(tree))