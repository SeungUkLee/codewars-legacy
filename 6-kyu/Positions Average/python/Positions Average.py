# My Solution
from itertools import combinations

def pos_average(s):
    count = 0
    s_split = s.split(', ')
    for s1, s2 in combinations(s_split, 2):
        for v1, v2 in zip(s1, s2):
            if v1 == v2:
                count += 1

    n = len(s_split)
    combi = (n * (n - 1)) / 2
    print(count)
    return count * 100 / (combi * len(s_split[0]))

# Best Practice & Clever
from statistics import mean
from itertools import combinations

def pos_average(s):
    return mean(a == b for combo in combinations(s.split(', '), 2) for a, b in zip(*combo)) * 100.

