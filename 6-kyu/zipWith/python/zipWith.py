# My Solution 1
def zip_with(fn,a1,a2):
    return [fn(x, y) for x, y in zip(a1, a2)]

# Best Practice & Clever
def zip_with(fn, a1, a2):
    return list(map(fn, a1, a2))
    