import java.util.*;

public class 2nd_freq_num {

    public static char secondMostFrequent(String s) {

        HashMap<Character, Integer> frequency = new HashMap<>();

        for (char ch : s.toCharArray()) {
            frequency.put(
                ch,
                frequency.getOrDefault(ch, 0) + 1
            );
        }

        ArrayList<Integer> counts =
            new ArrayList<>(new HashSet<>(frequency.values()));

        Collections.sort(counts, Collections.reverseOrder());

        if (counts.size() < 2)
            return '-';

        int secondCount = counts.get(1);

        for (char ch : s.toCharArray()) {
            if (frequency.get(ch) == secondCount)
                return ch;
        }

        return '-';
    }

    public static void main(String[] args) {

        String s = "banana";

        System.out.println(secondMostFrequent(s));
    }
}