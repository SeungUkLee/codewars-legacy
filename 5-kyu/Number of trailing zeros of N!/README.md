## Instructions

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

`N! = 1 * 2 * 3 * ... * N`

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples

~~~
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
~~~

Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

## Sample Tests

### Python

~~~ py
test.describe("Sample Tests")
test.it("Should pass sample tests")
test.assert_equals(zeros(0), 0, "Testing with n = 0")
test.assert_equals(zeros(6), 1, "Testing with n = 6")
test.assert_equals(zeros(30), 7, "Testing with n = 30")
~~~