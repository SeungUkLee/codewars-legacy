/* My Solution */
public class Kata {
  public static String createPhoneNumber(int[] numbers) {
    String res = "";
    for (int i=0; i<numbers.length; i++) {
      if (i == 0) {
          res += "(";
      } else if (i == 3) {
          res += ") ";
      } else if (i == 6) {
          res += "-";
      }
      res += numbers[i];
    }
    return res;
  }
}

/* Best Pratice */
public class Kata {
  public static String createPhoneNumber(int[] numbers) {
    return String.format("(%d%d%d) %d%d%d-%d%d%d%d",numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5],numbers[6],numbers[7],numbers[8],numbers[9]);
  }
}

/* Clever */
public class Kata {
	public static String createPhoneNumber(int[] numbers) {
		return String.format("(%d%d%d) %d%d%d-%d%d%d%d", java.util.stream.IntStream.of(numbers).boxed().toArray());
	}
}
