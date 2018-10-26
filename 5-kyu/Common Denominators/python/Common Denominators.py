# My Solution
from functools import reduce


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def convertFracts(lst):
    denom = reduce(lambda x, y: lcm(y[1], x), lst, 1)
    return [[x * denom // y, denom] for x, y in lst]


