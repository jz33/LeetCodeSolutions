/*
Perfect Squares
https://leetcode.com/problems/perfect-squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 */
class Solution {
    public int numSquares(int n) {
        // dp[i] records the smallest number
        int[] dp = new int[n+1];
        for (int i = 1; i < n+1; i++) {
            // worst case i is composed by all '1's
            dp[i] = i;
            
            int bound = (int)Math.sqrt(i);         
            for (int j = 1; j <= bound; j++) {
                dp[i] = Math.min(dp[i], dp[i- j*j] + 1);
            }
        }
        return dp[n];
    }
}
