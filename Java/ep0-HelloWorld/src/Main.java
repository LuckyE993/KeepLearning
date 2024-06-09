public class Main {
    public static void main(String[] args) {
//        System.out.println("Hello, World!");
        greetUser("John","Doe");
        greetUser("Hello","World");
    }
    public static void greetUser(String firstname,String lastname){
        System.out.println("Hello "+firstname+" "+lastname);
    }
}