'''
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
'''
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
def exist(board,word) -> bool:
        m,n=len(board),len(board[0])
        def dfs(i, j, k):
            if i<0 or j<0 or j>=n or i==m or board[i][j]!=word[k]:
                return False
            #进来必须满足这个元素等于当前轮到的字符
            if k==len(word)-1:
                return True
            res=False
            board[i][j]=''
            for x, y in [(0,-1), (0, 1), (1, 0), (-1, 0)]:
                res=res or dfs(x+i, y+j, k+1)
            board[i][j]=word[k]#恢复现场
            return res
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
        
    


print(exist(board, word))