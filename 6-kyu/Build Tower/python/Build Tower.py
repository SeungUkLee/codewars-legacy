# My Solution
def tower_builder(n_floors):
    lst = [(n_floors - i - 1) * ' ' +
           '*' * (i * 2 + 1) +
           (n_floors - i - 1) * ' ' for i in range(n_floors)]
    return lst


# Best Practice & Clever
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]