/* My Solution */
public class Kata {

    public static char findMissingLetter(char[] array)
    {
        int res=0;
        for (int i = 0; i < array.length - 1; i++) {
            int diff = array[i+1] - array[i];
            if (diff > 1) {
                res = array[i] + 1;
            }
        }

        return (char)res;
    }
}

/* Java 8 */
import java.util.stream.IntStream;

public class Kata
{
  public static char findMissingLetter(char[] array)
  {
      int index = IntStream.range(0, array.length-1).filter(i -> array[i] != array[i+1]-1).findFirst().getAsInt();
      return (char)(array[index] + 1);
  }
}