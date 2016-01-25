from sys import maxint
'''
Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    sold = [0]*2
    bought = [-maxint-1]*2
    for p in prices:
        sold[1] = max(sold[1], bought[1] + p)
        bought[1] = max(bought[1], sold[0] - p)
        sold[0] = max(sold[0], bought[0] + p)
        bought[0] = max(bought[0], -p)
    return sold[1]
