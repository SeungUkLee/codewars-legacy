## Instructions

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

~~~
apples, pears # and bananas
grapes
bananas !apples
~~~

The output expected would be:

~~~
apples, pears
grapes
bananas
~~~

The code would be called like so:

~~~
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
~~~

## Sample Tests

### Python
~~~ python
Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
~~~