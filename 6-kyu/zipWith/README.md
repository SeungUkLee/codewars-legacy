## Instructions

## Implement zip_with

zip_with takes a function and two arrays and zips the arrays together, applying the function to every pair of values.
The function value is one new array.

If the arrays are of unequal length, the output will only be as long as the shorter one.
(Values of the longer array are simply not used.)

Inputs should not be modified.

## Examples

~~~
zipWith( Math.pow, [10,10,10,10], [0,1,2,3] )      =>  [1,10,100,1000]
zipWith( Math.max, [1,4,7,1,4,7], [4,7,1,4,7,1] )  =>  [4,7,7,4,7,7]

zipWith( function(a,b) { return a+b; }, [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  Both forms are valid.
zipWith( (a,b) => a+b,                  [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  Both are functions.
~~~

##Input validation
Assume all input is valid.

## Sample Tests
### Python

~~~ js
Test.describe("Basic tests")
Test.assert_equals(zip_with(lambda a,b: a+b,[0,1,2,3,4,5],[6,5,4,3,2,1]),[6,6,6,6,6,6])
Test.assert_equals(zip_with(lambda a,b: a+b,[0,1,2,3,4  ],[6,5,4,3,2,1]),[6,6,6,6,6  ])
Test.assert_equals(zip_with(lambda a,b: a+b,[0,1,2,3,4,5],[6,5,4,3,2  ]),[6,6,6,6,6  ])
Test.assert_equals(zip_with(lambda a,b: a**b, [10,10,10,10], [0,1,2,3] ), [1,10,100,1000])
Test.assert_equals(zip_with(lambda a,b: max([a,b]), [1,4,7,1,4,7], [4,7,1,4,7,1] ), [4,7,7,4,7,7])
Test.assert_equals(zip_with(lambda a,b: a+b, [0,1,2,3], [0,1,2,3] ), [0,2,4,6])
Test.assert_equals(zip_with(lambda a,b: a+b, [0,1,2,3], [0,1,2,3] ), [0,2,4,6])
Test.assert_equals(zip_with(lambda a,b: a**b,[10,10,10,10,10,10,10],[0,1,2,3,4,5,6]),[1e0,1e1,1e2,1e3,1e4,1e5,1e6])
Test.assert_equals(zip_with(lambda a,b: a-b,[0,1,2,3,4,5],[6,5,4,3,2,1]),[-6,-4,-2,0,2,4])
Test.assert_equals(zip_with(lambda a,b: a*b,["a","b","c","d","e","f"],[6,5,4,3,2,1]),["aaaaaa","bbbbb","cccc","ddd","ee","f"])
~~~
