'''
WR公司的员工很喜欢玩机器人，于是他们在办公室摆了一个机器人。假设办公室是一个无边无际的格子场，最初，机器人位于坐标为 (0,0) 的格子里。它将执行一串由大写字母 'L'、'R'、'D'、'U' 组成的命令。每当执行一个命令时，机器人会按照对应的方向移动：

'L'：向左移动一格（当前格子的 x 坐标减 1）；
'R'：向右移动一格（当前格子的 x 坐标加 1）；
'D'：向下移动一格（当前格子的 y 坐标减 1）；
'U'：向上移动一格（当前格子的 y 坐标加 1）。
你的老板突然给你一个任务，让你在格子场上放置一个障碍物，使得在执行完所有命令后，机器人能够回到起始位置 (0,0)。当然，障碍物不能放在起始位置 (0,0)。任务保证如果没有障碍物，机器人将无法回到起始位置。

障碍物会影响机器人的移动：如果机器人尝试向某个方向移动，但该方向有障碍物，机器人将保持原地不动（障碍物也不会消失）。

找到工作中第一个遇到可以放置障碍物的格子（除 (0,0) 以外），使得在执行完所有命令后，机器人会回到起始位置 (0,0)。如果没有解决方法，则输出0 0。
'''

s="RUUDL"
def findObstacle(s):
    path=[(0,0)]
    action=[]
    #获得机器人每一步的移动和坐标
    for c in s:
        x,y=path[-1]
        if c=='L':
            path.append((x-1, y))
            action.append((-1, 0))
        elif c=='R':
            path.append((x+1, y))
            action.append((1, 0))
        elif c=='D':
            path.append((x, y-1))
            action.append((0, -1))
        else:
            path.append((x, y+1))
            action.append((0, 1))
    #print(path)
    #遍历每一步的坐标，看往哪里放障碍物，最后能回到原点
    for i in range(1, len(path)):
        #模拟放障碍物
        x, y=path[i]
        curX, curY=0,0
        #模拟从头开始遍历
        for j in range(len(action)):
            dx, dy=action[j]
            nextX, nextY=curX+dx, curY+dy
            if nextX==x and nextY==y:
                continue
            else:
                curX, curY=nextX, nextY
        if curX==0 and curY==0:
            return x, y
    return 0, 0


x,y=findObstacle(s)
print(x, y)