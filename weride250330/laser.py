'''
你是一名激光炮手，任务是消灭一群形态各异的怪兽，每个怪兽都有一个被攻击的范围，只有在该范围内发射的激光才能消灭它，你的激光只能在水平方向使用，目标范围内的怪兽能被同一束激光消灭。给定每个怪兽的受攻击范围（用区间数组regions表示，其中regions[i] = [i_min, i_max]表示在i_min和i_max之间（闭区间）的激光能够消灭第i个怪兽），返回消灭所有怪兽的所需要的最少激光数。

'''
#ranges=[[10,30],[3,8],[1,6],[7,12]]
ranges=[(10,30),(30,32),(12,15),(7,12)]
#可以用2束激光来消灭怪兽：
#- 在坐标6处发射激光，消灭怪兽[3,8]和[1,6]。
#- 在坐标11处发射激光，消灭怪兽[10,30]和[7,12]。
def minLaser(ranges):
    #按照左端点排序
    ranges.sort(key=lambda x:x[0])
    #记录当前右边界
    right=ranges[0][1]
    cnt=0
    for range in ranges:
        if range[0]<=right:
            continue
        else:
            cnt+=1
            right=range[1]
    return cnt+1
    
print(minLaser(ranges))