/*
Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
*/
public class Solution {
    public int maxProfit(int[] prices)
    {
        if(prices.length == 0) return 0;
        int k = 2;
        int[][] t = new int[k + 1][prices.length];
        for (int i = 1; i <= k; i++)
        {
            int outter = -prices[0];
            for (int j = 1; j < prices.length; j++)
            {
                t[i][j] = Math.max(t[i][j - 1], prices[j] + outter);
                outter =  Math.max(outter, t[i - 1][j - 1] - prices[j]);
            }
        }
        return t[k][prices.length - 1];
    }
}
