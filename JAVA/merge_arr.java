import java.util.*;

public class merge_arr {

    public static List<Integer> merge(int[] a, int[] b){

        List<Integer> result = new ArrayList<>();

        int i=0;
        int j=0;

        while(i<a.length && j<b.length){

            if(a[i] < b[j]){
                result.add(a[i]);
                i++;
            }else{
                result.add(b[j]);
                j++;
            }

        }

        while(i<a.length)
            result.add(a[i++]);

        while(j<b.length)
            result.add(b[j++]);

        return result;
    }

    public static void main(String[] args){

        int[] a={1,3,5};
        int[] b={2,4,6};

        System.out.println(merge(a,b));

    }
}