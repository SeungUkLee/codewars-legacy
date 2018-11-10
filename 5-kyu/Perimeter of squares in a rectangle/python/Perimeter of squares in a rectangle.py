# My Solution
def fib(n):
    pre, cur = 0, 1
    for _ in range(n + 1):
        yield cur
        pre, cur = cur, pre + cur

def perimeter(n):
    return 4 * sum(x for x in fib(n))
