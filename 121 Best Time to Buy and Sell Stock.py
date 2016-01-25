'''
Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Only 1 transaction allowed
'''
def maxProfit(prices):
    if len(prices) < 2: return 0
    prices.append(-1)
    mp,lo = 0,0
    for i in xrange(1,len(prices)):
        if prices[i] < prices[i-1]:
            mp = max(mp,prices[i-1] - prices[lo])
            if prices[i] < prices[lo]: lo = i
    return mp
