def createArrayGeneratorService(arr, state, m):
    result = []
    state_array = list(state)
    n = len(arr)

    for _ in range(m):
        # 找到最大的可用元素
        max_available = float('-inf')
        for i in range(n):
            if state_array[i] == '1':
                max_available = max(max_available, arr[i])

        # 将最大的可用元素添加到结果列表中
        result.append(max_available)

        # 更新状态数组
        list_idx = []
        for i in range(1, n):
            if state_array[i] == '0' and state_array[i - 1] == '1':
                list_idx.append(i)
        for idx in list_idx:
            state_array[idx] = '1'

    return result

elements = [5,3,4,6]
availability = "1100"
operations = 5
print(createArrayGeneratorService(elements, availability, operations))