'''
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
'''
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
def numIslands(grid):
    m=len(grid)
    n=len(grid[0])
    def dfs(i, j):
        if i<0 or j<0 or i==m or j==n or grid[i][j]!='1':
            return
        grid[i][j]='2'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    res=0
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='1':
                dfs(i, j)
                res+=1
    return res
'''
grid=[]
m=4
n=5
for _ in range(m):
    row=[int(x) for x in input().split()]
    grid.append(row)'''
print(numIslands(grid))