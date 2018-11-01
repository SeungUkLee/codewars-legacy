# My Solution using lambda & reduce

def chained(functions):
    print(functions)
    return lambda f: reduce(lambda h, g: g(h), functions, f)

# My Solution using closure

def chained(functions):
    def func(x):
        for f in functions:
            x = f(x)
        return x
    return func
