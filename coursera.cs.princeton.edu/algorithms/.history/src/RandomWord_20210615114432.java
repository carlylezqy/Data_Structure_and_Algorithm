import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String opt;
        int i = 0;
        while(StdIn.isEmpty() == false){
            if(StdRandom.uniform() > (1/++i)){
                opt = StdIn.readString();
            }
            StdIn.readString();
        }
        
        StdOut.println(opt);
        
    }
}
RandomWord < animals8.txt