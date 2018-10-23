# My Solution
def persistence(n):
    cnt = 0
    while n // 10 is not 0:
        cnt += 1
        n = mul(n)
    return cnt


def mul(n):
    res = 1
    while n is not 0:
        res *= n % 10
        n = n // 10
    return res

# Best Practice & Clever 1
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i