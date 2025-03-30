height = [0,1,0,2,1,0,1,3,2,1,2,1]
stack=[]
res=0
for i, x in enumerate(height):
    while stack and height[stack[-1]]<x:
        bottom=height[stack.pop()]
        #看到了升序，有更新答案的可能
        if len(stack)>0:
            leftIndex=stack[-1]
            res+=(min(height[leftIndex], x)-bottom)*(i-leftIndex-1)
    stack.append(i)
print(res)

        
print(trap(height))