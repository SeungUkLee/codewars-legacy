# Solution - 1 : Ref) https://www.programcreek.com/python/example/14603/heapq.merge - Example2
from itertools import tee, chain, groupby, islice
from heapq import merge

def hamming_numbers():
    # Generate "5-smooth" numbers, also called "Hamming numbers"
    # or "Regular numbers".  See: http://en.wikipedia.org/wiki/Regular_number
    # Finds solutions to 2**i * 3**j * 5**k  for some integers i, j, and k.

    def deferred_output():
        'Works like a forward reference to the "output" global variable'
        for i in output:
            yield i

    result, p2, p3, p5 = tee(deferred_output(), 4)
    m2 = (2*x for x in p2)                          # multiples of 2
    m3 = (3*x for x in p3)                          # multiples of 3
    m5 = (5*x for x in p5)                          # multiples of 5
    merged = merge(m2, m3, m5)
    combined = chain([1], merged)                   # prepend starting point
    output = (k for k, _ in groupby(combined))      # eliminate duplicates

    return result

def hamming(n):
    return list(islice(hamming_numbers(), n))[-1]

# Solution - 2 : Ref) https://github.com/8fdafs2/Codewars-Solu-Python/blob/master/src/kyu4_Hamming_Numbers.py

def hamming_numbers(n):
    """
    lazy, reliable
    """
    def recur():
        last = 1
        yield last
        a, b, c = tee(recur(), 3)
        for n in merge((2 * i for i in a), (3 * i for i in b), (5 * i for i in c)):
            if n != last:
                yield n
                last = n
    return list(islice(recur(), n))[-1]

# Best Practice & Clever

def hamming(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]

"https://www.codewars.com/kata/526d84b98f428f14a60008da/solutions/python"
