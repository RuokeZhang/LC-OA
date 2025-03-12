class MinStack:
    def __init__(self):
        self.stack=[]
        self.mStack=[] #降序
    def push(self, val):
        self.stack.append(val)
        # ATTENTION!!!
        if not self.mStack or (self.mStack and self.mStack[-1]>=val):
            self.mStack.append(val)
    def pop(self):
        if self.stack:
            s=self.stack.pop()
            if s==self.mStack[-1]:
                self.mStack.pop()
    def top(self):
        if self.stack:
            return self.stack[-1]
        return None
    def getMin(self):
        if self.stack:
            return self.mStack[-1]
        return None
    

stk=MinStack()
stk.push(3)
stk.push(4)
stk.push(2)
print(stk.getMin())
stk.push(4)
print(stk.top())
print(stk.getMin())
stk.pop()
print(stk.getMin())
stk.pop()
print(stk.getMin())