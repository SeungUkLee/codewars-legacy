# My Solution
import queue

def valid_parentheses(string):
    q = queue.Queue()
    for c in string:
        if c == '(':
            q.put('(')
        elif c == ')' and q.empty():
            return False
        elif c == ')' and not q.empty():
            q.get()
    if not q.empty():
        return False
    return True

# Best Practice & Clever
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

# Best Practice & Clever 2
def valid_parentheses(string):
    string = "".join(ch for ch in string if ch in "()")
    while "()" in string: string = string.replace("()", "")
    return not string