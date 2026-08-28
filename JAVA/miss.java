import java.util.HashSet;

public class miss {

    public static int smallestMissingPositive(int[] arr) {

        HashSet<Integer> set = new HashSet<>();

        for (int num : arr) {

            if (num > 0)
                set.add(num);
        }

        int number = 1;

        while (set.contains(number)) {
            number++;
        }

        return number;
    }

    public static void main(String[] args) {

        int[] arr = {3, 4, -1, 1};

        System.out.println(smallestMissingPositive(arr));
    }
}