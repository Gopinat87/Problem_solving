import java.util.*;

public class find_NPC {

    public static char firstNonRepeating(String str) {

        HashMap<Character, Integer> map = new HashMap<>();

        for(char ch : str.toCharArray()){
            map.put(ch, map.getOrDefault(ch,0)+1);
        }

        for(char ch : str.toCharArray()){
            if(map.get(ch)==1)
                return ch;
        }

        return '-';
    }

    public static void main(String[] args) {

        String text = "aabbcdeff";
        System.out.println(firstNonRepeating(text));

    }
}