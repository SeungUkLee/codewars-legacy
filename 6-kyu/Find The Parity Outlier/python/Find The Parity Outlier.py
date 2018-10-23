# My Solution
def find_outlier(integers):
    d = {
        'odd': [],
        'even': []
    }
    for i, v in enumerate(integers):
        d['even'].append(i) if v % 2 is 0 else d['odd'].append(i)

    return integers[d['even'][0]] if d['odd'].__len__() > d['even'].__len__() else integers[d['odd'][0]]

# Best Practice & Clever 1
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

# Best Practice & Clever 2
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

# Best Practice & Clever 3
def find_outlier(integers):
    assert len(integers) >= 3

    bit = ((integers[0] & 1) +
           (integers[1] & 1) +
           (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n

    assert False