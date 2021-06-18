import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        if(args[0] == "<"){
            StdOut.println(args[1]);
        }

        String opt = "";
        int i = 0;
        while(!StdIn.isEmpty()){
            String ipt = StdIn.readString();
            if(StdRandom.bernoulli((double) 1 / ++i)){opt = ipt;}
        }
          
        StdOut.println(opt);
        

    }
}