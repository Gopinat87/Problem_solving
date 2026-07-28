import java.util.HashSet;

public class find_dup {

    public static void findDuplicates(int[] arr) {

        HashSet<Integer> seen = new HashSet<>();
        HashSet<Integer> duplicate = new HashSet<>();

        for (int num : arr) {

            if (!seen.add(num))
                duplicate.add(num);
        }

        if (duplicate.isEmpty())
            System.out.println("No duplicates");
        else
            System.out.println(duplicate);
    }

    public static void main(String[] args) {

        int[] arr = {1,2,3,4,2,5,3,6};

        findDuplicates(arr);
    }
}