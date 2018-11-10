# My Solution
# Ref) https://github.com/8fdafs2/Codewars-Solu-Python/blob/master/src/kyu5_Sum_of_Pairs.py
def sum_pairs(ints, s):
    i_set = set()
    for i in range(len(ints)):
        indic = s - ints[i]
        if indic in i_set:
            return [indic, ints[i]]
        i_set.add(ints[i])
    return None

# My Solution : This is Time Out.
def search_point(ints, s):
    for i in range(len(ints)):
        for j in range(i + 1, len(ints)):
            if ints[i] + ints[j] == s:
                return i, j
    return 0, 0

def sum_pairs(ints, s):
    p_i, p_j = search_point(ints, s)

    if p_i == 0 and p_j == 0:
        return None

    for i in range(p_i, p_j):
        for j in range(i + 1, p_j):
            if ints[i] + ints[j] == s:
                return [ints[i], ints[j]]

    return [ints[p_i], ints[p_j]]


# Best Practice & Clever
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)