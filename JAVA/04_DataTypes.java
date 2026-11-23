public class Main {
    public static void main(String[] args) {
        String name = "Gopinath";
        int age = 24;
        double height = 5.8;
        boolean isDeveloper = true;

        System.out.println(name.getClass().getSimpleName());
        System.out.println(((Object) age).getClass().getSimpleName());
        System.out.println(((Object) height).getClass().getSimpleName());
        System.out.println(((Object) isDeveloper).getClass().getSimpleName());
    }
}
