# My Solution
from itertools import cycle

def make_looper(a):
    it = iter(cycle(a))

    def point():
        return it.__next__()

    return point

# Best Practice & Clever
from itertools import cycle

def make_looper(s):
    g = cycle(s)
    # return g.__next__
    return lambda: next(g)



# Best Practice & Clever 2
from itertools import cycle

class make_looper(cycle):
    
    def __call__(self):
        return self.__next__()