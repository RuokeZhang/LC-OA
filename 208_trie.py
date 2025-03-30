class Node:
    __slots__='son', 'end'
    def __init__(self):
        self.son={}
        self.end=False
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self, s):
        cur=self.root
        for c in s:
            if c not in cur.son:
                cur.son[c]=Node()
            cur=cur.son[c]
        cur.end=True
    def find(self, s):
        cur=self.root
        for c in s:
            if not c in cur.son:
                return 0
            cur=cur.son[c]
        return 2 if cur.end else 1
    def search(self, s):
        return True if self.find(s)==2 else False
    def startsWith(self, s):
        return True if self.find(s)>0 else False
        