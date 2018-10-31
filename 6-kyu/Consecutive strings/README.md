## Instructions

You are given an array `strarr` of strings and an integer k. Your task is to return the first longest string consisting of `k` consecutive strings taken in the array.

Example: 

~~~
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
~~~

`n` being the length of the string array, if `n = 0` or `k > n` or `k <= 0` return "".

## Sample Tests

### Python

~~~ py
def testing(actual, expected):
    Test.assert_equals(actual, expected)

Test.describe("longest_consec")
Test.it("Basic tests")
testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
testing(longest_consec([], 3), "")
testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
~~~