import java.util.*;

public class find_leader {

    public static ArrayList<Integer> findLeaders(int[] arr) {

        ArrayList<Integer> leaders = new ArrayList<>();

        int maxRight = Integer.MIN_VALUE;

        for (int i = arr.length - 1; i >= 0; i--) {

            if (arr[i] > maxRight) {

                leaders.add(arr[i]);
                maxRight = arr[i];
            }
        }

        Collections.reverse(leaders);

        return leaders;
    }

    public static void main(String[] args) {

        int[] arr = {16, 17, 4, 3, 5, 2};

        System.out.println(findLeaders(arr));
    }
}