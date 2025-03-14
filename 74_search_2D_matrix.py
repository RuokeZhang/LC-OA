matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3

def search(matrix, target):
    m,n=len(matrix), len(matrix[0])
    #matrix[i][j]的 index 为n*i+j
    #从 index=mid可以得到它的行、列坐标。n*i+j=mid
    #i=mid//n, j=mid-n*i
    l, r=0, m*n
    while l<r:
        mid=(l+r)//2
        i=mid//n
        j=mid-n*i
        if matrix[i][j]<target:
            l=mid+1
        elif matrix[i][j]==target:
            return True
        else:
            r=mid
    return False