/* My Solution */
public class BitCounting {

    public static int countBits(int n) {
        int cnt = 0;
    
        for (int i=n;i>0;i/=2) {
            if(i%2 == 1) cnt ++;
        }
    
        return cnt;
    }    
}

/* Best Practice & Clever */
public class BitCounting {

    public static int countBits(int n){
      
      return Integer.bitCount(n);
    }
    
}

/* java8 */
public class BitCounting {

    public static int countBits(int n){
      return (int) Integer.toBinaryString(n).chars()
                .filter(c -> c == '1')
                .count();
    }
    
  }