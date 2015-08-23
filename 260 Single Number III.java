/**
 * Single Number III
 * https://leetcode.com/problems/single-number-iii/
 * https://leetcode.com/discuss/52351/accepted-java-space-easy-solution-with-detail-explanations
 */
public class Solution {
    public int[] singleNumber(int[] arr)
    {
        int diff = 0;
        for(int i : arr)
            diff ^= i;
            
        // Get its last set bit
        diff &= -diff;

        int[] res = new int[]{0,0};
        for(int i : arr)
        {
            if ((i & diff) == 0) // the bit is not set
            {
                res[0] ^= i;
            }
            else // the bit is set
            {
                res[1] ^= i;
            }
        }
        return res;
    }
}
