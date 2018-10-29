# My Solution
def zeros(n):
    res = 0
    n //= 5
    while n > 0:
        res += n
        n //= 5
    return res

def zeros_2(n):
    """
    Timeout
    """
    fac = str(math.factorial(n))
    return len(fac) - len(fac.rstrip('0'))

# Best Practice & Clever
def zeros(n):
    x = n/5
    return x+zeros(x) if x else 0

