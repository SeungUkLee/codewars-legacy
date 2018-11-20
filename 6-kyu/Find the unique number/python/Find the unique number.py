# My Solution
from collections import Counter
def find_uniq(arr):
    count_arr = Counter(arr)
    for k, v in count_arr.items():
        if v == 1:
            return k


# Best Practice & Clever 1
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


# Best Practice & Clever 2
from collections import Counter

def find_uniq(arr):
    return next(k for k,v in Counter(arr).items() if v == 1)


# Best Practice & Clever 3
def find_uniq(arr):
    arr.sort()
    return arr[0] if arr[0] != arr[1] else arr[-1]
