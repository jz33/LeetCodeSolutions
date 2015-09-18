import java.util.Arrays;

/**
 * Perfect Squares
 * https://leetcode.com/problems/perfect-squares/
 *
 */
public class _279 {

    public int numSquares(int n){
        if(n < 1) return 0;

        // Notice the different: 
        //java.util.List<Integer> buf = new java.util.Vector<Integer>(Arrays.asList(new Integer[n+1]));
        java.util.List<Integer> buf = java.util.Arrays.asList(new Integer[n+1]);
        
        for(int i = 0;i <= n;i++){
            
            // $i is upper bound of buf[i]
            buf.set(i, i);
            for(int j = 2; j <= (int)Math.sqrt(i);j++){
                buf.set(i, Math.min(buf.get(i), 1 + buf.get(i - j * j)));
            }
        }
        return buf.get(n);
    }
}
