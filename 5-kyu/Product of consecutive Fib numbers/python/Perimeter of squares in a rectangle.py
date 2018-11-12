# My Solution
def gen_fib():
    pre, cur = 0, 1
    while True:
        yield pre, cur
        pre, cur = cur, pre + cur
        
def productFib(prod):
    for pre, cur in gen_fib():
        if pre * cur > prod:
            return [pre, cur, False]
        elif pre * cur == prod:
            return [pre, cur, True]

# Best Practice & Clever
def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]
