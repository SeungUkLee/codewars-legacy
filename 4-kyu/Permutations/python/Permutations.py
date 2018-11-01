# My Solution using generator
def gen_perms(elements):
    if len(elements) > 1:
        for perm in gen_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
    else:
        yield elements

def permutations(string):
    return list(set(s for s in gen_perms(string)))


# Best Practice & Clever
import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

# Use Recursion
def permutations(string):
  if len(string) == 1: return set(string)
  first = string[0]
  rest = permutations(string[1:])
  result = set()
  for i in range(0, len(string)):
    for p in rest:
      result.add(p[0:i] + first + p[i:])
  return result

# ----
from itertools import permutations as pm
permutations=lambda s: map(''.join, set(pm(s)))
