import java.util.Scanner;

public class string_rev {

    public static String reverseString(String text) {
        String reverse = "";

        for(int i = text.length() - 1; i >= 0; i--) {
            reverse += text.charAt(i);
        }

        return reverse;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String word = sc.nextLine();

        System.out.println(reverseString(word));
    }
}