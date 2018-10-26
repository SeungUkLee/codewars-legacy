# My Solution 1
def gen_tribonacci(max, *args):
    a, b, c = args[0], args[1], args[2]
    for _ in range(max):
        yield a + b + c
        a, b, c = b, c, a + b + c

def tribonacci(signature, n):
    res = signature[:n]
    for v in gen_tribonacci(n - 3, *signature):
        res.append(v)
    return res

# My Solution 2
def tribonacci(signature, n):
    res = signature[:n]
    gen_tri = (sum(res[-3:]) for _ in range(n-3))
    for v in gen_tri:
        res.append(v)
    return res

# Best Practice & Clever
def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res

# Best Practice & Clever 2
def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]