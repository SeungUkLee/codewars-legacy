# My Solution
"""
1. 문자열 길이 비교
2. 더 긴 문자열을 dict 으로 저장. (key는 문자. 문자가 중복으로 있을 수 있으니 value 는 문자 갯수)
3. 짧은 문자열을 for loop 로 문자 하나하나를 키로 사용하여 dict 에 조회
4. 하나라도 없으면 false or 값이 0 이하이면 false
"""
def compare_str_len(s1, s2):
    return (s2, s1) if s1.__len__() > s2.__len__() else (s1, s2)


def set_dict(s):
    s_dic = dict()
    for c in s:
        if c in s_dic:
            s_dic[c] += 1
        else:
            s_dic[c] = 1
    return s_dic


def scramble(s1, s2):
    (short_str, long_str) = compare_str_len(s1, s2)
    dic = set_dict(long_str)
    for c in short_str:
        if c in dic and dic[c] > 0:
            dic[c] -= 1
        else:
            return False
    return True


# Best Practice & Clever
from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0

# Best Practice & Clever 2
def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

# Best Practice & Clever 3
def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))

# Best Practice & Clever 4
def scramble(s1,s2):
    return all( s1.count(x) >= s2.count(x) for x in set(s2))