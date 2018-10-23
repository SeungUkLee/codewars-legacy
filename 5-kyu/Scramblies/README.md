## Instructions

Complete the function `scramble(str1, str2)` that returns `true` if a portion of `str1` characters can be rearranged to match `str2`, otherwise returns `false`.

Notes:
- Only lower case letters will be used (a-z). No punctuation or digits will be included.
- Performance needs to be considered

Examples
~~~
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
~~~

## Sample Tests

### Python

~~~ py
Test.assert_equals(scramble('rkqodlw', 'world'),  True)
Test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
Test.assert_equals(scramble('katas', 'steak'), False)
Test.assert_equals(scramble('scriptjava', 'javascript'), True)
Test.assert_equals(scramble('scriptingjava', 'javascript'), True)
~~~