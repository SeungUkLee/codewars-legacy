## Instructions
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

## Sample Tests

### JAVA
~~~ java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class SquareDigitTest {
    @Test
    public void test() {
      assertEquals(811181, new SquareDigit().squareDigits(9119));
    }
    
}
~~~
