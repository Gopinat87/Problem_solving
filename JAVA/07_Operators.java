public class Operators {
    public static void main(String[] args) {
        int a = 20;
        int b = 6;

        System.out.println("Addition: " + (a + b));
        System.out.println("Subtraction: " + (a - b));
        System.out.println("Multiplication: " + (a * b));
        System.out.println("Division: " + (a / b));
        System.out.println("Remainder: " + (a % b));
        System.out.println("Power: " + Math.pow(a, 2));

        System.out.println("Is a greater than b? " + (a > b));
        System.out.println("Are both positive? " + (a > 0 && b > 0));
    }
}
