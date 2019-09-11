/*
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2

Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
             
*/
public class Solution {
    public int mySqrt(int x) 
    {
        if (x == 0)
        {
            return 0;
        }
        
        int lt = 1;
        int rt = Integer.MAX_VALUE; // 2 ^ 31 - 1
        
        while (lt <= rt)
        {
            // Not lt + rt >> 1, think integer overflow
            int mid = (lt + (rt - lt >> 1));
            
            // Not compare with mid * mid, think integer overflow
            int div = x / mid;
            
            if (mid ==  div)
            {
                return mid;
            }
            else if (mid < div)
            {
                lt = mid + 1;
            }
            else // mid > div
            {
                rt = mid - 1;
            }
        }
        // As the break of binary search now, lt =  rt + 1
        // Choose smaller rt
        return rt;
    }
}
