public class BreakContinue {
    public static void main(String[] args) {
        System.out.println("Break example:");
        for (int number = 1; number <= 5; number++) {
            if (number == 4) {
                break;
            }
            System.out.println(number);
        }

        System.out.println("Continue example:");
        for (int number = 1; number <= 5; number++) {
            if (number == 3) {
                continue;
            }
            System.out.println(number);
        }
    }
}
