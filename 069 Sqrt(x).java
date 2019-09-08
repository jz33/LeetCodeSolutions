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
