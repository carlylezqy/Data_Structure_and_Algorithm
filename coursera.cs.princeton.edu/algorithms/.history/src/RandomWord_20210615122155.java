import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String opt = "";
        int i = 0;
        while(!StdIn.isEmpty()){
            String ipt = StdIn.readString();
            i++;
            if(StdRandom.bernoulli((double) 1 / ++i)){
                opt = ipt;
                StdOut.println(opt);
            }
            
        }
          
        StdOut.println(opt);
        
        //StdOut.println(inputs[StdRandom.uniform(0, 1234)]);
    }
}
//RandomWord < animals8.txt