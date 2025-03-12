'''
https://www.fastprep.io/problems/1.amazon-get-min-total-distance
'''
distribution_center_locations = [1, 2, 3]
def computeMinimumTotalDistance(distribution_center_locations):
    x = sorted(distribution_center_locations)
    n = len(x)
    if n <= 1:
        return 0  # 题目要求两个仓库，但n<=1时无法覆盖，可能返回0或处理特殊情况，根据题意调整
    
    # 计算前缀和数组
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + x[i]
    
    # 预处理left_cost，left_cost[k]表示前k个元素的总距离
    left_cost = [0] * (n + 1)
    for k in range(1, n+1):
        start = 0
        m = k
        mid = (m - 1) // 2
        pos = start + mid
        sum_left_part = x[pos] * (mid + 1) - (prefix_sum[pos + 1] - prefix_sum[start])
        sum_right_part = (prefix_sum[start + m] - prefix_sum[pos + 1]) - x[pos] * (m - (mid + 1))
        left_cost[k] = sum_left_part + sum_right_part
    
    # 预处理right_cost，right_cost[m]表示后m个元素的总距离
    right_cost = [0] * (n + 1)
    for m in range(1, n+1):
        start = n - m
        mid = (m - 1) // 2
        pos = start + mid
        sum_left_part = x[pos] * (mid + 1) - (prefix_sum[pos + 1] - prefix_sum[start])
        sum_right_part = (prefix_sum[start + m] - prefix_sum[pos + 1]) - x[pos] * (m - (mid + 1))
        right_cost[m] = sum_left_part + sum_right_part
    
    # 遍历所有可能的分割点k，找到最小的left_cost[k] + right_cost[n-k]
    min_total = float('inf')
    for k in range(1, n):
        total = left_cost[k] + right_cost[n - k]
        if total < min_total:
            min_total = total
    
    return min_total
print(computeMinimumTotalDistance(distribution_center_locations))