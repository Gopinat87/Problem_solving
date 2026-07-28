public class find_num {

    public static int secondSmallest(int[] arr){

        int smallest = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;

        for(int num : arr){

            if(num < smallest){

                second = smallest;
                smallest = num;

            }else if(num > smallest && num < second){

                second = num;
            }
        }

        if(second == Integer.MAX_VALUE)
            return -1;

        return second;
    }

    public static void main(String[] args){

        int[] arr = {8,5,2,9,5,6};

        System.out.println(secondSmallest(arr));
    }
}