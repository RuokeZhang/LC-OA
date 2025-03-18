'''
Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
'''
num1 = "456"
num2 = "77"
m,n=len(num1),len(num2)
i,j=m-1,n-1
carry=0
res=""
while i>=0 or j>=0:
    x=int(num1[i]) if i>=0 else 0
    y=int(num2[j]) if j>=0 else 0
    t=x+y+carry
    carry=t//10
    cur=t%10
    res=str(cur)+res
    i-=1
    j-=1
print(res)
