// count the number is odd or even in a list

public class countnum {

    public static void countEvenOdd(int[] arr){

        int even = 0;
        int odd = 0;

        for(int num : arr){

            if(num % 2 == 0)
                even++;
            else
                odd++;
        }

        System.out.println("Even = " + even);
        System.out.println("Odd = " + odd);
    }

    public static void main(String[] args){

        int[] arr = {10,15,8,21,14};

        countEvenOdd(arr);
    }
}