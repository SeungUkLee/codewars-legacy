# My Solution
import re

def count_smileys(arr):
    cnt = 0
    p = re.compile('[:|;]+[-|~]*[)|D]+')  # 정규 표현식 잘못됨.....
    for s in arr:
        if p.match(s):
            cnt += 1

    return cnt


# Best Practice & Clever 1
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))


# Best Practice & Clever 2
def count_smileys(arr):
    import re
    smiley = re.compile(r"[:;][-~]?[)D]")
    return sum(bool(re.match(smiley, el)) for el in arr)


# Best Practice & Clever 3
import re

def count_smileys(arr):
    return sum(1 for s in arr if re.match(r'\A[:;][-~]?[)D]\Z',s))