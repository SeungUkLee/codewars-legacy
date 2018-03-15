/* My Soultion */
    private static int[] race(int v1, int v2, int g) {
        int h = 0;
        int m = 0;
        int s = 0;
        if(v1 >= v2) return null;
        
        s = 3600 * g / (v2 - v1);
        h = s / 3600;
        s = s - 3600 * h;
        m = s / 60;
        s = s - 60 * m;

        return new int[]{h,m,s};
    }

/* Best Practice & Clever */
public class Tortoise {
    public static int[] race(int v1, int v2, int g) {
      int totalSecondsTaken = 0;
      if (v2 > v1 ) {
        totalSecondsTaken = (g*3600) / (v2-v1) ;
      } else {
        return null;
      }
      return new int[] {totalSecondsTaken/3600, (totalSecondsTaken % 3600)/60, totalSecondsTaken % 60};

    }
}
