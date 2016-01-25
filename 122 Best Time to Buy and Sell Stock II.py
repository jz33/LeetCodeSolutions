'''
Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Unlimited transactions
'''
def maxProfit(prices):
    prices.append(-1)
    lo,profit = 0,0
    for i in xrange(1,len(prices)):
        if prices[i] < prices[i-1]:
            profit += prices[i-1] - prices[lo]
            lo = i
    return profit
