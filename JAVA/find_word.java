public class find_word {

    public static String largestWord(String sentence){

        String[] words = sentence.split(" ");

        String longest = words[0];

        for(String word : words){

            if(word.length() > longest.length())
                longest = word;
        }

        return longest;
    }

    public static void main(String[] args){

        String sentence = "Python Java FullStack Developer";

        System.out.println(largestWord(sentence));
    }
}