# My Solution
def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
        
    letter = ""
    for i in range(len(strarr)-k+1):
        next_letter = "".join(strarr[i:i+k])
        if len(letter) < len(next_letter):
            letter = next_letter
    return letter


# Best Practice & Clever 1
def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""


# Best Practice & Clever 2
def longest_consec(strarr, k):
    if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
        return ""
    lst = [''.join(strarr[i:i+k]) for i in xrange(len(strarr))]
    return max(lst, key= lambda x: len(x))