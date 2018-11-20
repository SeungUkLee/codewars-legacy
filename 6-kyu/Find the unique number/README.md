## Instructions

There is an array with some numbers. All numbers are equal except for one. Try to find it!

~~~
findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
~~~

It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

1. Find the unique number (this kata)
2. Find the unique string
3. Find The Unique

## Sample Tests

### Python

~~~ py
test.describe("Basic Tests")
test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)
~~~