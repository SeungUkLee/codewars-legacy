# My Solution using generator
def add_tmp_to_res(tmp, res):
    if len(tmp) >= 3:
        res.append(str(tmp[0]) + '-' + str(tmp[-1]))
    elif len(tmp) == 2:
        res.append(str(tmp[0]))
        res.append(str(tmp[1]))
    else:
        res.append(str(tmp[0]))


def solution(args):
    res = []
    i, j = 0, 0
    while True:
        tmp = [args[i]]
        for j in range(i+1, len(args) + 1):
            if j != len(args):
                if args[j-1] + 1 != args[j]:
                    break
                tmp.append(args[j])
        add_tmp_to_res(tmp, res)
        i = j
        if i == len(args):
            break

    return ','.join(res)
    
# Best Practice & Clever
"https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/solutions/python"