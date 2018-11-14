# My Solution using generator
def solution(string, markers):
    res = []
    for s in string.split('\n'):
        index = -1
        for i, c in enumerate(s):
            if c in markers:
                index = i
                break
        res.append(s[:index].rstrip()) if index != -1 else res.append(s)
    return '\n'.join(res)


# Best Practice & Clever
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)


# ------
def solution(string,markers):
    lst = string.split('\n')
    ans = []
    for line in lst:
        for m in markers:
            if m in line:
                line = line[: line.find(m)].strip()
        ans.append(line) 
    return '\n'.join(ans)