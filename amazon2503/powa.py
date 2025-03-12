powa = [3, 3, 2, 3]
n = len(powa)

# 构建差分数组
diff = [powa[0]]
for i in range(1, n):
    diff.append(powa[i] - powa[i - 1])

# 累加差分数组中负数的绝对值
res = 0
for num in diff:
    if num < 0:
        res += abs(num)

print(res)