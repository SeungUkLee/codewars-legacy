# My Solution
import re

def change_pig_latin(s):
    if re.match('[a-zA-Z]+', s):
        return s[1:] + s[0] + "ay"
    return s

def pig_it(text):
    return ' '.join(list(map(change_pig_latin, text.split(' '))))


# Best Practice & Clever
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# Best Practice & Clever 2
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())