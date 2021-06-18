import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String opt = "";
        int i = 1;
        while (!StdIn.isEmpty()) {
            String ipt = StdIn.readString();
            if (StdRandom.bernoulli((double) 1 / i)){opt = ipt; i++;}
        }
          
        StdOut.println(opt);
    }
}