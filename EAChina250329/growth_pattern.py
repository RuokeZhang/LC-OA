'''
You are an ecologist studying the growth patterns of a rare species in different environmental conditions. You've collected data points representing the height (in millimeters) of specimen samples at various locations along a habitat gradient.

Your research question: What is the maximum number of samples you can select that demonstrate a clear evolutionary adaptation to the gradient, shown by a strictly increasing height pattern?

Rules:

You can select samples from any location, but they must be arranged in order of the gradient

Each selected sample must be taller than the previous one

You want to find the longest possible sequence of samples showing this pattern
'''
sample_heights=[10,9,2,5,3,7,101,18]
#贪心+二分
#g[i]代表长度为i的递增序列的最后一个元素的最小值
#如果当前元素大于g[-1]，则g.append(x)
#否则，找到g中第一个大于等于x的元素，将其替换为x
def max_samples(sample_heights):
    g=[sample_heights[0]]
    for x in sample_heights[1:]:
        if x>g[-1]:
            g.append(x)
        else:
            l, r=0, len(g)-1
            while l<r:
                mid=(l+r)//2
                if g[mid]<x:
                    l=mid+1
                else:
                    r=mid
            g[l]=x
    return len(g)
print(max_samples(sample_heights))
