'''
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true
'''
from ast import List


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m,n=len(matrix), len(matrix[0])
    i, j=0, n-1
    while m>i>=0 and 0<=j<n:
        if matrix[i][j]==target:
            return True
        if matrix[i][j]<target:
            i+=1
        else:
            j-=1
    return False