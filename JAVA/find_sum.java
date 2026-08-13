// Find the Sum of Digits
// Question

// Given an integer, find the sum of all its digits.

// Input

// 12345

// Output

// 15

public class find_sum {

    public static int sumOfDigits(int n) {

        int total = 0;

        while (n > 0) {
            int digit = n % 10;
            total += digit;
            n /= 10;
        }

        return total;
    }

    public static void main(String[] args) {

        int num = 12345;

        System.out.println(sumOfDigits(num));
    }
}