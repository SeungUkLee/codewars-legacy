## Instructions

There is an array of strings. All strings contains similar letters except one. Try to find it!

~~~
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
~~~

Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.

This is the second kata in series:

1. Find the unique number
2. Find the unique string (this kata)
3. Find The Unique

## Sample Tests

### Python

~~~ py
test.describe('should handle sample cases')
test.assert_equals(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]), 'BbBb')
test.assert_equals(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]), 'foo')
test.assert_equals(find_uniq([ '    ', 'a', '  ' ]), 'a')
~~~