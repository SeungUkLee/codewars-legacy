## Instructions
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same 

digits:
~~~
12 ==> 21
513 ==> 531
2017 ==> 2071
~~~

If no bigger number can be composed using those digits, return -1:

~~~
9 ==> -1
111 ==> -1
531 ==> -1
~~~

## Sample Tests

### Python
~~~ python
Test.assert_equals(next_bigger(12),21)
Test.assert_equals(next_bigger(513),531)
Test.assert_equals(next_bigger(2017),2071)
Test.assert_equals(next_bigger(414),441)
Test.assert_equals(next_bigger(144),414)
~~~