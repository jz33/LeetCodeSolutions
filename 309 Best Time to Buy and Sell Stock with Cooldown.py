'''
309. Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        sells = [0] * 3
        buys = [float('-inf')] * 2
        for i, p in enumerate(prices):
            si = i % 3
            bi = i % 2
            
            # sells[si] is the max of previous day sells (not sell today)
            # and previous day buy + today's price (sell today)
            sells[si] = max(sells[si-1], buys[bi-1] + p)
            
            # buys[si] is the max of previous day buys (not buy today)
            # and previous 2 day (because of the cooldown) buy + today's price (buy today)
            buys[bi] = max(buys[bi-1], sells[si-2] - p)
            
        return sells[(len(prices)-1) % 3]
