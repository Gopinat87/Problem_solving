// Find the Intersection of Two Arrays
// Question

// Given two arrays, find the elements that appear in both arrays, including duplicates based on their frequency.

// Input

// arr1 = [1, 2, 2, 3, 4]
// arr2 = [2, 2, 4, 5]

// Output

// [2, 2, 4]

import java.util.*;

public class intersection {

    public static ArrayList<Integer> intersection(
            int[] arr1, int[] arr2) {

        HashMap<Integer, Integer> frequency = new HashMap<>();
        ArrayList<Integer> result = new ArrayList<>();

        for (int num : arr1) {
            frequency.put(
                num,
                frequency.getOrDefault(num, 0) + 1
            );
        }

        for (int num : arr2) {

            if (frequency.getOrDefault(num, 0) > 0) {

                result.add(num);

                frequency.put(
                    num,
                    frequency.get(num) - 1
                );
            }
        }

        return result;
    }

    public static void main(String[] args) {

        int[] arr1 = {1, 2, 2, 3, 4};
        int[] arr2 = {2, 2, 4, 5};

        System.out.println(intersection(arr1, arr2));
    }
}