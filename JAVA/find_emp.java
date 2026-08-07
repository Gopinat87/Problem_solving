public class find_emp {

    public static void main(String[] args) {

        int[] salary = {25000,30000,45000,28000};

        int highest = salary[0];
        int lowest = salary[0];
        int sum = 0;

        for(int s : salary){

            if(s > highest)
                highest = s;

            if(s < lowest)
                lowest = s;

            sum += s;
        }

        double avg = (double)sum / salary.length;

        System.out.println("Highest : " + highest);
        System.out.println("Lowest : " + lowest);
        System.out.println("Average : " + avg);

    }
}