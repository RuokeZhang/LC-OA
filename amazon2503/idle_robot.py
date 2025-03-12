from collections import defaultdict

x=[1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
y=[1, 2, 3, 1, 2, 3, 5, 1, 2, 3]

class Solution:
    def countIdleRobots(self, x_coords, y_coords):
        # 使用defaultdict来简化初始化步骤
        horizontal_bounds = defaultdict(lambda: [float('inf'), float('-inf')])
        vertical_bounds = defaultdict(lambda: [float('inf'), float('-inf')])
        
        # 更新每个坐标点对应的行和列的边界值
        for x, y in zip(x_coords, y_coords):
            horizontal_bounds[y][0] = min(horizontal_bounds[y][0], x)
            horizontal_bounds[y][1] = max(horizontal_bounds[y][1], x)
            vertical_bounds[x][0] = min(vertical_bounds[x][0], y)
            vertical_bounds[x][1] = max(vertical_bounds[x][1], y)
        
        idle_robot_count = 0
        
        # 检查每个机器人是否为闲置状态
        for x, y in zip(x_coords, y_coords):
            if (horizontal_bounds[y][0] < x < horizontal_bounds[y][1]) and \
               (vertical_bounds[x][0] < y < vertical_bounds[x][1]):
                idle_robot_count += 1
                
        return idle_robot_count

sol=Solution()
print(sol.countIdleRobots(x, y))