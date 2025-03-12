
m=int(input())
n=int(input())
matrix=[]
for _ in range(m):
    row=[int(x) for x in input().split()]
    matrix.append(row)
print(matrix)
    
        
DIRS=(0, 1), (1, 0), (0, -1), (-1, 0)
dirCnt=0
res=[]
size=m*n
i,j=0, -1
while len(res)<size:
    dx, dy=DIRS[dirCnt]
    for _ in range(n):
        i+=dx
        j+=dy
        res.append(matrix[i][j])
    n, m=m-1, n
    dirCnt=(dirCnt+1)%4
print(res)


