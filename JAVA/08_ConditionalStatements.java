import java.util.Scanner;

public class ConditionalStatements {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your mark: ");
        int mark = scanner.nextInt();

        if (mark >= 90) {
            System.out.println("Grade: A");
        } else if (mark >= 75) {
            System.out.println("Grade: B");
        } else if (mark >= 50) {
            System.out.println("Grade: C");
        } else {
            System.out.println("Grade: Fail");
        }

        scanner.close();
    }
}
