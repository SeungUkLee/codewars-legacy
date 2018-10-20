# My Solution
def digital_root(n):
    res = n
    for i in gen_digital_root(n):
        res = i
    return res

def gen_digital_root(n):
    while True:
        if n < 10:
            break
        n = sum_num(n)
        yield n
    return n

def sum_num(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res

# Best Practice & Clever
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))