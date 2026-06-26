public class string_comparision{
    public static void main(String[] args) {
        String s1 = "Java";
        String s2 = new String("Java");

        if (s1 == s2)
            System.out.println("Same");
        else
            System.out.println("Different");

        if (s1.equals(s2))
            System.out.println("Equal");
    }
}