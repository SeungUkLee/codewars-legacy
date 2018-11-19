# My Solution
from itertools import combinations
def choose_best_sum(t, k, ls):
    max_num = -1
    for l in combinations(ls, k):
        l_sum = sum(l)
        if l_sum <= t:
            max_num = max(l_sum, max_num)
    if max_num == -1:
        return None
    return max_num



# Best Practice & Clever
import itertools
def choose_best_sum(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None

# Best Practice & Clever 2
from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)

# Best Practice & Clever 3 
from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((sum(v) for v in combinations(ls,k) if sum(v)<=t), default=None)