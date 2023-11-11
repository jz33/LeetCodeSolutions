'''
188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:

    1 <= k <= 100
    1 <= prices.length <= 1000
    0 <= prices[i] <= 1000

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
        if k >= len(prices) // 2 :
            return self.largeCase(prices)

        '''
        Similar to 123. Best Time to Buy and Sell Stock III
        @sells[i-1] is the largest gain when doing i times sell
        @buys[i-1] is the largest gain when doing i times buy
        '''
        sells = [0] * k
        buys = [float('-inf')] * k
        for price in prices:
            for i in range(k, 0, -1):
                sells[i-1] = max(sells[i-1], buys[i-1] + price)
                buys[i-1] = max(buys[i-1], sells[i-2] - price if i >= 2 else -price)
        return sells[k-1]
