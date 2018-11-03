# My Solution
def sum_dig_pow(a, b):
    return [n for n in range(a, b + 1) if is_eureka(n)]

def is_eureka(n):
    res = 0
    for i, c in enumerate(str(n)):
        res += pow(int(c), i + 1)
    if res == n:
        return True
    return False

# Best Practice & Clever
def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow(a, b):
    return filter(filter_func, range(a, b+1))