import java.util.Scanner;

public class count_vowels {

    public static int count(String text) {

        int count = 0;

        text = text.toLowerCase();

        for(int i = 0; i < text.length(); i++) {

            char ch = text.charAt(i);

            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
                count++;
        }

        return count;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");

        String word = sc.nextLine();

        System.out.println(count(word));
    }
}