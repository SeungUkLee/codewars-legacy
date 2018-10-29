# My Solution
def add(n):
    class Add(int):
        def __call__(self, x):
            return Add(self + x)
    return Add(n)


# Best Practice & Clerver
class add(int):
    def __call__(self,n):
        return add(self+n)


# Best Practice & Clerver 2
class CustomInt(int):
    def __call__(self, v):
        return CustomInt(self + v)

def add(num):
    return CustomInt(num)


# Best Practice & Clerver 3
class add(int):
    __call__ = lambda self, value: add(self + value)