from sys import maxint
'''
Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Can complete at most k transactions
'''
def largeCase(prices):
    '''
    When k >= len(prices) / 2
    '''
    profit = 0
    for i in xrange(1,len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
    
def maxProfit(k,prices):
    if len(prices) < 2 or k <= 0: return 0
    if k >= len(prices) / 2 : return largeCase(prices)
    sold = [0]*(k+1)
    bought = [-maxint-1]*(k+1)
    for p in prices:
        for j in xrange(k,0,-1):
            sold[j] = max(sold[j], bought[j] + p)
            bought[j] = max(bought[j], sold[j-1] - p)
    return sold[k]
