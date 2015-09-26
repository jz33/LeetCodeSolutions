/*
07 Reverse Integer
https://oj.leetcode.com/problems/reverse-integer/
*/
public class Solution {
    /*
    No need to consider sign
    */
    public int reverse(int x) {
        long r = x % 10;
        x /= 10;
        while(x != 0){
            //System.out.println(r);
            r  = r * 10 + x % 10;
            x /= 10;
        }
        if(r > Integer.MAX_VALUE || r < Integer.MIN_VALUE){
            r = 0;
        }    
        return (int)r;
    }
}
