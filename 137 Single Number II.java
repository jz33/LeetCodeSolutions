/*
137. Single Number II
https://leetcode.com/problems/single-number-ii/

Given a non-empty array of integers, every element appears three times except for one,
which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
*/
class Solution {
    /**
    * The idea is to count '1' in each bits
    * This idea can extend to all similar questions
    */
    public int singleNumber(int[] nums) {      
        int res = 0;

        for (int b = 0; b < 32; ++b) {

            int sum = 0;
            for (int n : nums) {
                if ((n & (1 << b)) != 0) {
                    ++sum;
                }
            }

            sum %= 3; // for this question
            if (sum != 0) {
                res |= sum << b;
            }
        }

        return res;
    }
}
