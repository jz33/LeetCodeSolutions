import java.util.Arrays;

/**
 * Perfect Squares
 * https://leetcode.com/problems/perfect-squares/
 * Similar to "Coin Changes"
 */
public int numSquares(int n) {
    int[] buf = new int[n+1];
    for(int i = 1;i <= n;i++){
        buf[i]  = i;
        int bound = (int)Math.sqrt(i);
        for(int j = 2; j <= bound;j++){
            buf[i] = Math.min(buf[i], 1 + buf[i-j*j]);
        }
    }
    return buf[n];
}
