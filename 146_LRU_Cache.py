class Node:
    __slots__='pre', 'next', 'val', 'key'
    def __init__(self, key=0, val=0):
        self.key=key
        self.val=val
class LRUCache:
    def __init__(self, capacity):
        self.dummy=Node(0, 0)
        self.capacity=capacity
        self.dummy.next=self.dummy
        self.dummy.pre=self.dummy
        self.key_to_node={}
    def pushFront(self, node):
        nxt=self.dummy.next
        self.dummy.next=node
        nxt.pre=node
        node.pre=self.dummy
        node.next=nxt
        self.key_to_node[node.key]=node
    def getNode(self, key)->Node:
        if key not in self.key_to_node:
            return None
        node=self.key_to_node[key]
        self.remove(node)
        self.pushFront(node)
        return node
    def remove(self, node):
        node.pre.next=node.next
        node.next.pre=node.pre
    def get(self, key)->int:
        node=self.getNode(key)
        if not node:
            return -1
        return node.val
    def put(self, key, value):
        node=self.getNode(key)
        if node:
            # if already exists
            node.val=value
            return
        node=Node(key, value)
        self.pushFront(node)
        if len(self.key_to_node)>self.capacity:
            #delete the last node
            del self.key_to_node[self.dummy.pre.key]
            self.remove(self.dummy.pre)

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(2))
lRUCache.put(3, 1)
print(lRUCache.get(1))