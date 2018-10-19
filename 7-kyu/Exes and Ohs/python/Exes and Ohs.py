"""
my code
"""
def xo(s):
    s = s.upper()
    x_cnt = 0
    o_cnt = 0
    for c in s:
        if c is 'X':
            x_cnt += 1
        elif c is 'O':
            o_cnt += 1
    if x_cnt == o_cnt:
        return True
    return False


"""
Best Pratices & Clever
"""
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')