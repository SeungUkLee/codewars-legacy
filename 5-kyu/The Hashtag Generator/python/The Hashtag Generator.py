# My Solution
def generate_hashtag(s):
    if not s:
        return False
    res = ""
    for word in s.split():
        if len(word) >= 140:
            return False
        res += word[0].upper() + word[1:].lower()

    [word[0].upper() + word[1:].lower() for word in s.split() if len(word) < 140]
    return '#' + res


# Best Practice & Clever
def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False