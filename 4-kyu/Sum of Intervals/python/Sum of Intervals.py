# My Solution using generator
def sum_of_intervals(intervals):
    dy_list = [False] * 1000
    sort_intervlas = sorted(intervals)
    max_x, cnt = 0, 0
    for x1, x2 in sort_intervlas:
        if len(dy_list) <= x2:
            dy_list += [False] * (x2 - len(dy_list))
        max_x = max(max_x, x1)
        for i in range(max_x, x2):
            if not dy_list[i]:
                dy_list[i] = True
                cnt += 1
    return cnt


# Best Practice & Clever
def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top    = a
        if top < b: s, top = s+b-top, b
    return s

# Best Practice & Clever 2
def sum_of_intervals(intervals): 
    s = []
    for i in intervals:
        s += list(range(i[0],i[1]))
    return len(set(s))

"https://www.codewars.com/kata/52b7ed099cdc285c300001cd/solutions/python"