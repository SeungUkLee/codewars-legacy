# My Soultion using reduce
def max_sequence(arr):
    cur_sum = 0

    def func(max_sum, cur_num):
        nonlocal cur_sum
        cur_sum = max(cur_sum + cur_num, 0)
        return max(max_sum, cur_sum)

    return reduce(func, arr, 0)


# My Soultion using generator
def gen(arr):
    cur_sum = 0
    max_sum = 0

    for cur_num in arr:
        cur_sum = max(cur_sum + cur_num, 0)
        yield max(cur_sum, max_sum)


def max_sequence(arr):
    if not arr:
        return 0

    return max(gen(arr))

# Best Practices & Clever
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

# Best Practices & Clever 2
def maxSequence(arr):
  lowest = ans = total = 0
  for i in arr:
    total += i
    lowest = min(lowest, total)
    ans = max(ans, total - lowest)
  return ans