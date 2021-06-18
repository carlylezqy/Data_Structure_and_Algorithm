import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        //String[] inputs = new String[args.length];
        String inputs = StdIn.readString();
        StdOut.println(inputs[StdRandom.uniform(0, inputs.length)]);
    }
}
