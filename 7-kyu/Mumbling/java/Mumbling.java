/* My Solution */

public static String accum(String s) {
    String res="";

    for (int i = 0; i < s.length(); i++) {
        String lower = s.substring(i, i+1).toLowerCase();
        String upper = s.substring(i, i+1).toUpperCase();
        res += upper;
        for (int j = 1; j <= i; j++) {
            res += lower;
        }
        if (i != s.length()-1) {
            res += "-";
        }
    }
    return res;
}

/* Best Paratice & Clever */
public static String accum(String s) {
    StringBuilder bldr = new StringBuilder();
    int i = 0;
    for(char c : s.toCharArray()) {
      if(i > 0) bldr.append('-');
      bldr.append(Character.toUpperCase(c));
      for(int j = 0; j < i; j++) bldr.append(Character.toLowerCase(c));
      i++;
    }
    return bldr.toString();
}

/* java8 */
public static String accum(String s) {
    return IntStream.range(0, s.length())
            .mapToObj(i -> IntStream.range(0, i + 1)
                    .mapToObj(i1 -> i1 == 0 ? String.valueOf(s.charAt(i)).toUpperCase() : String.valueOf(s.charAt(i)).toLowerCase())
                    .collect(Collectors.joining())
            ).collect(Collectors.joining("-"));
}

/* --------- */
public static final String DELIMITER = "-";

public static String accum(String input) {
    List<String> stringList = IntStream.range(0, input.length())
            .mapToObj(i -> duplicateCharFirstUpper(input.charAt(i), i + 1))                
            .collect(Collectors.toList());

    return String.join(DELIMITER, stringList);
}

private static String duplicateCharFirstUpper(char c, int numberOfAppearances) {
    char upperCase = Character.toUpperCase(c);
    StringBuilder stringBuilder = new StringBuilder();
    stringBuilder.append(upperCase);

    for (int i = 1; i < numberOfAppearances; i++) {
        stringBuilder.append(Character.toLowerCase(c));
    }

    return stringBuilder.toString();
}

/* --------- */

public static String accum(String s) {
    char[] chars = s.toUpperCase().toCharArray();
    return IntStream.range(0, chars.length).mapToObj(index -> chars[index] + Stream.generate(() -> String.valueOf(chars[index])).limit(index).collect(Collectors.joining()).toLowerCase()).collect(Collectors.joining("-"));
}