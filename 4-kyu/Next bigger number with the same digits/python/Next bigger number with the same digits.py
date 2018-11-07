# My Solution using generator
def next_bigger(n):
    n_lst = list(str(n))
    i, j = len(n_lst) - 1, len(n_lst) - 1

    while i > 0 and n_lst[i - 1] >= n_lst[i]:
        i -= 1

    if i <= 0:
        return -1

    while n_lst[j] <= n_lst[i - 1]:
        j -= 1

    swap(n_lst, i - 1, j)
    j = len(n_lst) - 1
    while i < j:
        swap(n_lst, i, j)
        i += 1
        j -= 1
    return int("".join(c for c in n_lst))

def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


# Best Practice & Clever
import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1

"https://www.codewars.com/kata/55983863da40caa2c900004e/solutions/python"