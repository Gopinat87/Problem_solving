public class Main {
    public static void main(String[] args) {
        String age = "24";

        int convertedAge = Integer.parseInt(age);

        System.out.println("Original value: " + age);
        System.out.println("Converted value: " + convertedAge);
        System.out.println("After adding 5: " + (convertedAge + 5));
    }
}
