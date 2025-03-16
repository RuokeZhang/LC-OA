'''
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
'''
def canFinish(numCourses, prerequisites):
    n=len(prerequisites)
    g=[[] for _ in range(numCourses)]
    for pair in prerequisites:
        g[pair[1]].append(pair[0])
    color=[0]*numCourses
    def dfs(i):
        color[i]=1
        for neighbor in g[i]:
            if color[neighbor]==1 or (color[neighbor]==0 and dfs(neighbor)):
                return True #有环
        color[i]=2
        return False
    
    
    for i in range(numCourses):
        print(color[i])
        if color[i]==0 and dfs(i):
            return False
    
    return True

numCourses = 2
prerequisites =  [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))