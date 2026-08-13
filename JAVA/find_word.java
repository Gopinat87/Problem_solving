// Find the Longest Word with Unique Characters
// Question

// Given a sentence, find the longest word that contains no repeated characters.

// Input

// "apple dog house banana"

// Output

// house

// Because:

// apple   → p repeats
// dog     → unique
// house   → unique
// banana  → a repeats

import java.util.*;

public class find_word {

    public static String longestUniqueWord(String sentence) {

        String[] words = sentence.split(" ");

        String longest = "";

        for (String word : words) {

            HashSet<Character> set = new HashSet<>();

            for (char ch : word.toCharArray()) {
                set.add(ch);
            }

            if (set.size() == word.length()) {

                if (word.length() > longest.length()) {
                    longest = word;
                }
            }
        }

        return longest;
    }

    public static void main(String[] args) {

        String sentence = "apple dog house banana";

        System.out.println(longestUniqueWord(sentence));
    }
}