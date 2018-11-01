# My Solution using lambda & reduce

def compose(f,g):
    def com(*n):
        return f(g(*n))
    return com

# Best Practice & Clever
def compose(f,g):
    return lambda *x: f(g(*x))