# My Solution
def solution(number):
  res = 0
  
  for i in range(1, number):
    if i % 3 == 0:
      res += i
    elif i % 5 == 0:
      res += i
    
  return res
  

# Best Practice & Clever
def solution(number):
  return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)