import edu.princeton.cs.algs4.StdOut;

public class HelloGoodbye {
    public static void main(String[] args) throws Exception {
        String employee1 = args[0];
        String employee2 = args[1];
        StdOut.println("Hello " + employee1 + " and " + employee2 + ".");
        StdOut.println("Goodbye " + employee2 + " and " + employee1 + ".");
    }
}
