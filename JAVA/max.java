public class max {

    public static int maxDifference(int[] arr) {

        int minValue = arr[0];
        int maxDifference = arr[1] - arr[0];

        for (int i = 1; i < arr.length; i++) {

            int difference = arr[i] - minValue;

            if (difference > maxDifference)
                maxDifference = difference;

            if (arr[i] < minValue)
                minValue = arr[i];
        }

        return maxDifference;
    }

    public static void main(String[] args) {

        int[] arr = {7, 1, 5, 3, 6, 4};

        System.out.println(maxDifference(arr));
    }
}