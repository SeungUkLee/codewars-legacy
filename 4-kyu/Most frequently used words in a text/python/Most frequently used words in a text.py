# My Solution using generator
from collections import Counter
import re

def top_3_words(text):
    count = Counter(filter(re.compile(r"[A-Za-z]+").search, map(lambda x: x.lower(), re.split(r"[^A-Za-z']+", text.strip()))))
    return [x[0] for x in count.most_common(3)]


# Best Practice & Clever
from collections import Counter
import re


def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]

"https://www.codewars.com/kata/51e056fe544cf36c410000fb/solutions/python"