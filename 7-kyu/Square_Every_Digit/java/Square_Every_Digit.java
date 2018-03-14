/* My Soluction */
public class SquareDigit {

  public int squareDigits(int n) {
    StringBuffer sb = new StringBuffer();
      for (int i = n; i > 0; i /= 10) {
        int num = i % 10;
        sb.insert(0, num * num);
      }
    return Integer.parseInt(sb.toString());
  }
}

/* Best Practice */
public class SquareDigit {

	public int squareDigits(int n) {
		String result = ""; 
		          
		while (n != 0) {
			int digit = n % 10 ;
			result = digit*digit + result ;
			n /= 10 ;
		}	      
		return Integer.parseInt(result) ;
	}
}


/* Clever */
import java.util.stream.Collectors;

public class SquareDigit {
	public int squareDigits(int n) {
		return Integer.parseInt(String.valueOf(n)
					        .chars()
									.map(i -> Integer.parseInt(String.valueOf((char) i)))
									.map(i -> i * i)
									.mapToObj(String::valueOf)
									.collect(Collectors.joining("")));
	}
}


