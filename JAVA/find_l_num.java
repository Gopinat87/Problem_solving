public class find_l_num {

    public static int largest(int[] arr) {

        int max = arr[0];

        for(int num : arr) {

            if(num > max)
                max = num;
        }

        return max;
    }

    public static void main(String[] args) {

        int[] arr = {5,12,9,30,18};

        System.out.println(largest(arr));
    }
}