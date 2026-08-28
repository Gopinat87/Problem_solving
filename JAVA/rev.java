public class rev {

    public static String reverseWords(String sentence) {

        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();

        for (int i = words.length - 1; i >= 0; i--) {

            result.append(words[i]);

            if (i != 0)
                result.append(" ");
        }

        return result.toString();
    }

    public static void main(String[] args) {

        String sentence = "I love Python";

        System.out.println(reverseWords(sentence));
    }
}