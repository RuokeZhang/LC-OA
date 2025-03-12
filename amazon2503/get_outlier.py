'''
Some data analysts at Amazon are analyzing the outliers in data that contains two co-related features. The features are represented as two arrays of n integers each, feature1, and feature2. A data set is considered free of outliers if for any two indices i and j where 0 ≤ i < j < n, if feature1[i] > feature1[j], then feature2[i] > feature2[j] or if feature1[i] < feature1[j], then feature2[i] < feature2[j]. Note that if feature1[i] = feature1[j], then the data set is not considered to be free of outliers.

Given the arrays, feature1 and feature2, find the length of the largest array of indices i1, i2, i3 ... ik, such that data formed by these indices i.e. [feature1[i1], feature1[i2]....feature1[ik]] and [feature2[i1], feature2[i2]....feature2[ik]] is free of outliers.

Example

Suppose n=5, feature1=[4, 5, 3, 1, 2], and feature2=[2, 1, 3, 4, 5].

It is optimal to choose the indices [3, 4]. The data for feature1 is [1, 2] and for feature2 is [4, 5]. Here feature1[0] < feature1[1] and feature2[0] < feature2[1], therefore the condition holds true. Since it is not possible to select a larger subset without violating the conditions, the answer is 2 i.e. the size of the chosen subset.

Function Description

Complete the function getLargestIndexLen in the editor below.

getLargestIndexLen takes the following arguments:

int feature1[n]: the values of the first feature
int feature2[n]: the values of the second feature
中文解释
亚马逊的一些数据分析师正在分析包含两个相关特征的数据中的异常值。这些特征表示为两个整数数组，分别是feature1和feature2，每个数组的长度为n。如果对于任意两个索引i和j（其中0 ≤ i < j < n），当feature1[i]大于feature1[j]时，feature2[i]也必须大于feature2[j]；或者当feature1[i]小于feature1[j]时，feature2[i]也必须小于feature2[j]，则认为该数据集没有异常值。注意，如果feature1[i]等于feature1[j]，则认为该数据集存在异常值。

给定数组feature1和feature2，找到最长的索引数组i1, i2, i3...ik，使得由这些索引形成的子数组[feature1[i1], feature1[i2]....feature1[ik]]和[feature2[i1], feature2[i2]....feature2[ik]]没有异常值。

示例

假设n=5，feature1=[4, 5, 3, 1, 2]，feature2=[2, 1, 3, 4, 5]。

最优选择是索引[3, 4]。此时feature1的子数组为[1, 2]，feature2的子数组为[4, 5]。这里feature1[0]小于feature1[1]且feature2[0]小于feature2[1]，因此条件成立。由于无法选择更大的子集而不违反条件，所以答案是2，即所选子集的大小。

'''
def getLargestIndexLen(feature1, feature2):
    """
    计算最长的下标子序列，使得对于任意选中的下标 i 和 j (i < j)，
    如果 feature1[i] < feature1[j] 则 feature2[i] < feature2[j]；如果 feature1[i] > feature1[j] 则 feature2[i] > feature2[j]。
    注意：如果 feature1[i] == feature1[j]，则不符合要求。
    返回满足条件的最长子序列的长度。
    """
    n = len(feature1)
    
    # 计算严格递增的最长子序列
    dp_inc = [1] * n  # dp_inc[i] 表示以索引 i 结尾的最长严格递增子序列长度
    for i in range(n):
        for j in range(i):
            # 如果在 feature1 与 feature2 中都满足递增条件，则可以更新 dp_inc[i]
            if feature1[j] < feature1[i] and feature2[j] < feature2[i]:
                dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)
    
    lis_inc = max(dp_inc) if n > 0 else 0

    # 计算严格递减的最长子序列
    dp_dec = [1] * n  # dp_dec[i] 表示以索引 i 结尾的最长严格递减子序列长度
    for i in range(n):
        for j in range(i):
            # 如果在 feature1 与 feature2 中都满足递减条件，则可以更新 dp_dec[i]
            if feature1[j] > feature1[i] and feature2[j] > feature2[i]:
                dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)
    
    lis_dec = max(dp_dec) if n > 0 else 0
    
    # 返回两种情况中较大的一个
    return max(lis_inc, lis_dec)


# 以下是一个示例测试

if __name__ == "__main__":
    # 示例数据
    feature1 = [4, 5, 3, 1, 2]
    feature2 = [2, 1, 3, 4, 5]
    
    # 应该输出 2，对应的最优选择索引为 [3, 4] (feature1: [1,2], feature2: [4,5])
    result = getLargestIndexLen(feature1, feature2)
    print("最大子序列长度为:", result)
