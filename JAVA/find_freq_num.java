import java.util.HashMap;

public class find_freq_num {

    public static int mostFrequent(int[] arr) {

        HashMap<Integer, Integer> frequency = new HashMap<>();

        for (int num : arr) {
            frequency.put(
                num,
                frequency.getOrDefault(num, 0) + 1
            );
        }

        int maxCount = 0;
        int answer = arr[0];

        for (int num : arr) {

            if (frequency.get(num) > maxCount) {
                maxCount = frequency.get(num);
                answer = num;
            }
        }

        return answer;
    }

    public static void main(String[] args) {

        int[] arr = {4, 2, 4, 3, 2, 4, 2};

        System.out.println(mostFrequent(arr));
    }
}