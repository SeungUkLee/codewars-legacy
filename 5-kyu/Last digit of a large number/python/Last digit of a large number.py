# My Solution
# My Solution
def last_digit(n1, n2):
    if n2 == 0:
        return 1
    
    d = int(str(n1)[-1:])
    tmp = d
    d_cycle = []
    while True:
        d_cycle.append(tmp)
        tmp = (tmp * d) % 10
        if tmp == d:
            break
    index = n2 % len(d_cycle)
    return d_cycle[-1] if index == 0 else d_cycle[index - 1]

# Best Practice & Clever
def last_digit(n1, n2):
    return pow( n1, n2, 10 )


# Best Practice & Clever 2
def last_digit(n1, n2):
    return (n1 % 10) ** (n2 % 4 + 4 * bool(n2)) % 10

"https://www.codewars.com/kata/5511b2f550906349a70004e1/solutions/python"