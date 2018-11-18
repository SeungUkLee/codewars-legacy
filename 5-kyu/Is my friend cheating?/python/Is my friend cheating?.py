# My Solution
def removNb(n):
    n_sum = ((n + 1) * n) / 2
    res = []
    for x in range(1, n + 1):
        y = (int(n_sum) - x) // (x + 1)
        if y <= n and x * y == n_sum - (x + y):
            res.append((x, y))
    return res


# Best Practice & Clever
def removNb(n):
    total = n*(n+1)/2
    sol = []
    for a in range(1,n+1):
        b = (total-a)/(a+1.0)
        if b.is_integer() and b <= n:
            sol.append((a,int(b)))
    return sol

# Best Practice & Clever 2
def removNb(n):
    sum = n*(n + 1)/2  
    return [(x, (sum - x) / (x + 1)) for x in xrange(1, n+1) if (sum - x) % (x + 1) == 0 and 1 <= (sum - x) / (x + 1) <= n]