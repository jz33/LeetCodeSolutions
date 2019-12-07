'''
188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''
class Solution:
    def largeCase(self, prices: List[int]) -> int:
        '''
        For case when k is more than half of days
        '''
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2 or k <= 0:
            return 0

        if k >= len(prices) // 2 :
            return self.largeCase(prices)

        '''
        @sells[i] is the largest gain when doing i times sell
        @buys[i] is the largest gain when doing i times buy
        '''
        sells = [0] * (k + 1)
        buys = [float('-inf')] * (k + 1)
        for p in prices:
            # For sell[i], it is p + previous day buys[i], because you have to buy ith times before sell ith time
            # For buys[i], it is -p + previous day sells[i-1]
            # Iterate from right to left is a trick to avoid caching previous day buys and sells
            for j in range(k, 0, -1):
                sells[j] = max(sells[j], buys[j] + p)
                buys[j] = max(buys[j], sells[j-1] - p)
        return sells[k]
